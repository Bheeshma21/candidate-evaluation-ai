from pathlib import Path

from rag.vector_store import VectorStore


class DocumentLoader:

    def __init__(self):
        self.store = VectorStore()

    def load_documents(self):

        folder = Path("rag/documents")

        for file in folder.glob("*.txt"):

            text = file.read_text(
                encoding="utf-8"
            )

            self.store.add_document(
                file.stem,
                text
            )

        print("Documents indexed successfully.")