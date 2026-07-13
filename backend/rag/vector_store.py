import chromadb

from rag.embedding_service import EmbeddingService


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="rag/vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="candidate_knowledge"
        )

        self.embedding = EmbeddingService()

    def add_document(
        self,
        doc_id: str,
        text: str
    ):

        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[
                self.embedding.embed(text)
            ]
        )

    def search(
        self,
        query: str,
        k: int = 3
    ):

        return self.collection.query(
            query_embeddings=[
                self.embedding.embed(query)
            ],
            n_results=k
        )