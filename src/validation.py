
import re

def validate_invoice(data):

    errors = []

    if not data.get("Invoice Number"):
        errors.append("Invoice Number is missing")

    if not data.get("Invoice Date"):
        errors.append("Invoice Date is missing")

    if not data.get("Vendor Name"):
        errors.append("Vendor Name is missing")

    email = data.get("Email", "")

    if not email or not re.match(
        r"^[\w.-]+@[\w.-]+\.\w+$", email
    ):
        errors.append("Invalid Email Address")

    amount = data.get("Total Amount")

    try:
        if amount is None or float(amount) <= 0:
            errors.append("Invalid Invoice Amount")
    except (ValueError, TypeError):
        errors.append("Invoice Amount must be numeric")

    status = data.get("Payment Status")

    if status not in ["Paid", "Pending", "Unpaid"]:
        errors.append("Invalid Payment Status")

    return errors
