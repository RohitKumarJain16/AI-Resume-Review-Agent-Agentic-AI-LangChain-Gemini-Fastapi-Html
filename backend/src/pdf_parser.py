from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class ResumeParser:
    """
    Parses a PDF resume and extracts its text.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def extract_text(self) -> str:
        """
        Extract text from the uploaded PDF.

        Returns:
            str: Complete resume text.
        """

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"Resume not found: {self.pdf_path}"
            )

        loader = PyPDFLoader(str(self.pdf_path))

        documents = loader.load()

        resume_text = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        return resume_text.strip()