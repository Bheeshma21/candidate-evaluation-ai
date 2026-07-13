import fitz  # PyMuPDF
from docx import Document


class ResumeParser:

    @staticmethod
    def extract_text(file_path: str) -> str:

        if file_path.endswith(".pdf"):

            doc = fitz.open(file_path)

            text = ""

            for page in doc:
                text += page.get_text()

            return text

        elif file_path.endswith(".docx"):

            doc = Document(file_path)

            return "\n".join(
                p.text for p in doc.paragraphs
            )

        else:
            raise Exception("Unsupported file format.")