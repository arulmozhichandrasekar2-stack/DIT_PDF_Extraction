
import sys
import unittest
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "src")
)

from data_extraction import extract_invoice_data
from validation import validate_invoice


class TestInvoiceExtraction(unittest.TestCase):

    def test_valid_invoice(self):
        text = """
        Invoice Number: INV-101
        Invoice Date: 03-11-2026
        Vendor Name: ABC Technologies
        Customer Name: Test Customer
        Email: test@example.com
        Total Amount: 15000
        Payment Status: Paid
        """

        data = extract_invoice_data(text)
        errors = validate_invoice(data)

        self.assertEqual(data["Invoice Number"], "INV-101")
        self.assertEqual(data["Total Amount"], "15000")
        self.assertEqual(errors, [])

    def test_invalid_email(self):
        data = {
            "Invoice Number": "INV-102",
            "Invoice Date": "03-11-2026",
            "Vendor Name": "ABC Technologies",
            "Email": "invalid-email",
            "Total Amount": "15000",
            "Payment Status": "Paid"
        }

        errors = validate_invoice(data)

        self.assertIn("Invalid Email Address", errors)

    def test_invalid_amount(self):
        data = {
            "Invoice Number": "INV-103",
            "Invoice Date": "03-11-2026",
            "Vendor Name": "ABC Technologies",
            "Email": "test@example.com",
            "Total Amount": "0",
            "Payment Status": "Paid"
        }

        errors = validate_invoice(data)

        self.assertIn("Invalid Invoice Amount", errors)


if __name__ == "__main__":
    unittest.main()
