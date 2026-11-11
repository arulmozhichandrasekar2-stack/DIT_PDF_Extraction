
import pymupdf
from pathlib import Path

output_folder = Path(__file__).parent.parent / "data" / "input"
output_folder.mkdir(parents=True, exist_ok=True)

pdf_path = output_folder / "invalid_invoice.pdf"

doc = pymupdf.open()
page = doc.new_page()

content = """
SAMPLE INVALID INVOICE

Invoice Number: 
Invoice Date: 03-11-2026
Vendor Name: XYZ Company
Customer Name: Test Customer
Email: invalid-email
Total Amount: 0
Payment Status: Unknown
"""

page.insert_text((70, 80), content, fontsize=14)

doc.save(str(pdf_path))
doc.close()

print("Invalid test PDF created successfully!")
