from chatbot.vector_store import HashingVectorStore


def test_hashing_vector_store_returns_hits():
    store = HashingVectorStore()
    hits = store.similarity_search("visa travel documents", k=3)
    assert hits
    assert hits[0].score > 0
