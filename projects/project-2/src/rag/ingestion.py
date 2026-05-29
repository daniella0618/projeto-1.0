import os
import chromadb
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma")

client = chromadb.PersistentClient(path=CHROMA_PATH)

try:
    client.delete_collection("docs")
except:
    pass

collection = client.create_collection("docs")


def run_ingestion():
    print("INICIANDO INGESTÃO")

    base_path = os.path.join(os.getcwd(), "knowledge_base")

    all_chunks = []
    ids = []
    metadata = []

    for file in os.listdir(base_path):
        if file.endswith(".txt"):

            print("Processando:", file)

            with open(os.path.join(base_path, file), "r", encoding="utf-8") as f:
                text = f.read()

                for i, chunk in enumerate(text.split("\n")):
                    if chunk.strip() == "":
                        continue

                    all_chunks.append(chunk)
                    ids.append(f"{file}_{i}")
                    metadata.append({
                        "source": file,
                        "chunk_id": f"{file}_{i}"
                    })

    if not all_chunks:
        print("Nenhum texto encontrado!")
        return

    vectorizer = TfidfVectorizer()
    embeddings = vectorizer.fit_transform(all_chunks).toarray()

    collection.add(
        documents=all_chunks,
        embeddings=embeddings.tolist(),
        ids=ids,
        metadatas=metadata
    )


    print("Ingestão concluída!")
    print("Total:", len(all_chunks))


if __name__ == "__main__":
    run_ingestion()
