
import re

def extract_invoice_data(text):

    def get_value(pattern):
        match = re.search(pattern, text)
        return match.group(1).strip() if match else None

    invoice_data = {
        "Invoice Number": get_value(r"Invoice Number:\s*(.+)"),
        "Invoice Date": get_value(r"Invoice Date:\s*(.+)"),
        "Vendor Name": get_value(r"Vendor Name:\s*(.+)"),
        "Customer Name": get_value(r"Customer Name:\s*(.+)"),
        "Email": get_value(r"Email:\s*(.+)"),
        "Total Amount": get_value(r"Total Amount:\s*(\d+(?:\.\d{1,2})?)"),
        "Payment Status": get_value(r"Payment Status:\s*(.+)")
    }

    return invoice_data
