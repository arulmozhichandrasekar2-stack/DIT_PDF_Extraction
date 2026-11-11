# DIT-P11 – Automated PDF Data Extraction

## 1. Project Overview

The Automated PDF Data Extraction project is designed to extract important information from PDF invoice documents automatically. The system reads PDF files, identifies required invoice details, validates the extracted information, and stores the results in Excel files.

It also identifies invalid or incomplete records and generates a separate exception report for further review.

## 2. Project Objectives

- To automate invoice data extraction from PDF documents.
- To reduce manual data entry.
- To extract important invoice fields accurately.
- To validate the extracted information.
- To identify missing and invalid data.
- To generate structured Excel output files.
- To maintain a separate report for invalid records.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PyMuPDF | Reading PDF documents |
| Pandas | Processing extracted data |
| OpenPyXL | Excel file support |
| Regular Expressions | Extracting invoice fields |
| Python Unittest | Unit testing |
| Visual Studio Code | Development environment |

## 4. System Workflow

1. Collect PDF invoice documents.
2. Read PDF files using PyMuPDF.
3. Extract text from PDF documents.
4. Identify invoice details using regular expressions.
5. Validate the extracted fields.
6. Separate valid and invalid records.
7. Export valid records to Excel.
8. Generate an exception report for invalid records.

## 5. Modules Description

### 5.1 PDF Reader Module

The PDF reader module reads PDF documents and extracts their text using the PyMuPDF library.

### 5.2 Data Extraction Module

The data extraction module identifies important invoice details using regular expressions.

### 5.3 Validation Module

The validation module checks the extracted information, including invoice number, date, vendor name, email, total amount, and payment status.

### 5.4 Main Processing Module

The main module processes multiple PDF files, performs extraction and validation, and generates the output Excel files.

### 5.5 Sample PDF Creation Module

This module creates sample invoice PDF documents for testing the extraction process.

## 6. Extracted Invoice Fields

The system extracts the following information:

1. Invoice Number
2. Invoice Date
3. Vendor Name
4. Customer Name
5. Email
6. Total Amount
7. Payment Status

## 7. Data Validation

The system performs the following validation checks:

- Checks whether the invoice number is available.
- Checks whether the invoice date is available.
- Checks whether the vendor name is available.
- Validates the email format.
- Checks whether the total amount is numeric and greater than zero.
- Checks whether the payment status is Paid, Pending, or Unpaid.

Invalid records are moved to the exception report.

## 8. Output Files

The project generates the following Excel output files:

- **validated_invoices.xlsx** – Contains successfully extracted and validated invoice records.
- **exception_report.xlsx** – Contains invalid records and their validation errors.
- **extracted_invoice.xlsx** – An additional extracted invoice output file present in the project output folder.

## 9. Testing

Unit testing is performed using Python's unittest framework.

The following test cases were executed:

| Test Case | Result |
|---|---|
| Valid Invoice | Passed |
| Invalid Email | Passed |
| Invalid Amount | Passed |

**Total Test Cases:** 3

**Passed:** 3

**Failed:** 0

## 10. Final Execution Results

The system was tested using three PDF invoice documents.

| Processing Result | Count |
|---|---:|
| Total PDFs Processed | 3 |
| Valid Records | 2 |
| Error Records | 1 |

The system successfully processed the PDF documents, validated the extracted information, and generated the Excel output files.

## 11. Conclusion

The Automated PDF Data Extraction project successfully demonstrates the automation of invoice data extraction and validation using Python. It reduces manual data entry, organizes extracted information, and identifies invalid records through an exception report.

The project provides a structured approach to processing multiple PDF invoice documents and exporting the results into Excel format.

## 12. Future Enhancements

- Support for scanned PDF documents using OCR.
- Support for different invoice formats.
- Improved extraction accuracy.
- Additional validation rules.
- Database integration for storing extracted invoice information.