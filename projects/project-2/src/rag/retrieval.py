import os
import chromadb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# define caminho absoluto do banco
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma")

# conecta no banco certo
client = chromadb.PersistentClient(path=CHROMA_PATH)

# pega a collection já criada na ingestion
collection = client.get_collection("docs")


def retrieve(query: str, top_k: int = 3):

    # buscar documentos e metadata
    data = collection.get(include=["documents", "metadatas"])

    docs = data["documents"]
    metas = data["metadatas"]

    print("Total de docs no banco:", len(docs))

    # proteção caso banco esteja vazio
    if not docs:
        return []

    # vetorizar docs + query
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs + [query]).toarray()

    query_vec = vectors[-1].reshape(1, -1)
    doc_vecs = vectors[:-1]

    # calcular similaridade
    scores = cosine_similarity(doc_vecs, query_vec).flatten()

    # pegar índices mais relevantes
    top_idx = scores.argsort()[-top_k:][::-1]

    # montar resposta estruturada
    results = [
        {
            "text": docs[i],
            "source": metas[i]["source"],
            "chunk_id": metas[i]["chunk_id"]
        }
        for i in top_idx
    ]

    return results