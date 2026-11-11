
import pymupdf
from pathlib import Path

output_folder = Path(__file__).parent.parent / "data" / "sample"
output_folder.mkdir(parents=True, exist_ok=True)

pdf_path = output_folder / "sample_invoice.pdf"

doc = pymupdf.open()
page = doc.new_page()

content = """
SAMPLE INVOICE

Invoice Number: INV-2026-001
Invoice Date: 03-11-2026
Vendor Name: ABC Technologies
Customer Name: Arulmozhi
Email: abc@example.com
Total Amount: 15000
Payment Status: Paid
"""

page.insert_text((70, 80), content, fontsize=14)

doc.save(str(pdf_path))
doc.close()

print("Sample PDF created successfully!")
print("Location:", pdf_path)
