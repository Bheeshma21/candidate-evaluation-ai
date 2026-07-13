from pathlib import Path

from rag.document_loader import DocumentLoader
from rag.embedding_service import EmbeddingService
from rag.vector_store import VectorStore


loader = DocumentLoader()
embedder = EmbeddingService()
store = VectorStore()

docs_path = Path("rag/documents/knowledge")

for file in docs_path.glob("*.txt"):

    text = loader.load(str(file))

    embedding = embedder.embed(text)

    store.add_document(
        text=text,
        embedding=embedding,
        metadata={
            "file": file.name
        }
    )

print("All documents indexed successfully.")