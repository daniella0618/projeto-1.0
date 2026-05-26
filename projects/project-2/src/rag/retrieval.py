import chromadb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ✅ usa o mesmo banco do ingestion

client = chromadb.PersistentClient(path="./chroma")

collection = client.get_or_create_collection("docs")


def retrieve(query: str, top_k: int = 3):

    # ✅ pega os documentos do banco
    data = collection.get(include=["documents"])
    docs = data["documents"]

    print("📊 Total de docs no banco:", len(docs))

    if not docs:
        print("❌ Banco vazio!")
        return []

    # ✅ cria embeddings juntos (docs + query)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs + [query]).toarray()

    query_vec = vectors[-1].reshape(1, -1)
    doc_vecs = vectors[:-1]

    # ✅ usa similaridade REAL (melhor que antes)
    scores = cosine_similarity(doc_vecs, query_vec).flatten()

    # ✅ pega os top resultados
    top_idx = scores.argsort()[-top_k:][::-1]

    results = [docs[i] for i in top_idx]

    return results