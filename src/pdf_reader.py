
import pymupdf
from pathlib import Path

def read_pdf(pdf_path):
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print("Error: PDF file not found!")
        return ""

    doc = pymupdf.open(pdf_path)

    extracted_text = ""

    for page in doc:
        extracted_text += page.get_text()

    doc.close()

    return extracted_text


if __name__ == "__main__":
    file_path = Path(__file__).parent.parent / "data" / "sample" / "sample_invoice.pdf"

    text = read_pdf(file_path)

    print("PDF DATA EXTRACTION")
    print("-------------------")
    print(text)
