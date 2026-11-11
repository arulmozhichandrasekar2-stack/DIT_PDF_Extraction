
from pathlib import Path
import pandas as pd

from pdf_reader import read_pdf
from data_extraction import extract_invoice_data
from validation import validate_invoice


def main():

    base_path = Path(__file__).parent.parent

    input_folder = base_path / "data" / "input"
    output_folder = base_path / "data" / "output"

    input_folder.mkdir(parents=True, exist_ok=True)
    output_folder.mkdir(parents=True, exist_ok=True)

    valid_records = []
    error_records = []

    pdf_files = list(input_folder.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in data/input folder!")
        return

    for pdf_file in pdf_files:

        print(f"\nProcessing: {pdf_file.name}")

        try:
            extracted_text = read_pdf(pdf_file)

            if not extracted_text:
                raise ValueError("PDF contains no extractable text")

            invoice_data = extract_invoice_data(extracted_text)

            errors = validate_invoice(invoice_data)

            invoice_data["Source File"] = pdf_file.name

            if errors:
                invoice_data["Errors"] = "; ".join(errors)
                error_records.append(invoice_data)
                print("Validation: FAILED")

            else:
                valid_records.append(invoice_data)
                print("Validation: PASSED")

        except Exception as error:
            error_records.append({
                "Source File": pdf_file.name,
                "Errors": str(error)
            })
            print("Processing Error:", error)

    if valid_records:
        pd.DataFrame(valid_records).to_excel(
            output_folder / "validated_invoices.xlsx",
            index=False
        )

    if error_records:
        pd.DataFrame(error_records).to_excel(
            output_folder / "exception_report.xlsx",
            index=False
        )

    print("\n========== FINAL SUMMARY ==========")
    print("Total PDFs:", len(pdf_files))
    print("Valid Records:", len(valid_records))
    print("Error Records:", len(error_records))
    print("Processing Completed!")


if __name__ == "__main__":
    main()
