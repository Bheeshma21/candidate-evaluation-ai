from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.store = VectorStore()

    def retrieve(
        self,
        query: str
    ):

        result = self.store.search(query)

        return result["documents"][0]