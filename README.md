# AUTOMATED PDF DATA EXTRACTION

## 1. Project Overview

Automated PDF Data Extraction is a Python-based project designed to extract important information from PDF documents automatically. The system reads PDF invoices, extracts selected fields, validates the extracted data, and stores the results in Excel files.

This project reduces manual data entry and improves the accuracy and efficiency of document processing.

## 2. Project Objectives

- To automate PDF text extraction.
- To extract important invoice information.
- To validate the extracted data.
- To identify missing or invalid information.
- To process multiple PDF files.
- To generate Excel output files.
- To create exception reports for invalid records.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PyMuPDF | PDF text extraction |
| Pandas | Data processing |
| OpenPyXL | Excel file generation |
| Python Unittest | Testing |

## 4. Main Features

1. PDF Text Extraction
2. Automatic Invoice Data Extraction
3. Data Validation
4. Multiple PDF Processing
5. Error Handling
6. Excel Report Generation
7. Exception Report Generation
8. Automated Testing

## 5. Extracted Invoice Fields

The system extracts the following information:

- Invoice Number
- Invoice Date
- Vendor Name
- Customer Name
- Email Address
- Total Amount
- Payment Status

## 6. Project Folder Structure

```text
DIT_PDF_Extraction/
│
├── data/
│   ├── input/
│   ├── output/
│   └── sample/
│
├── src/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── data_extraction.py
│   ├── validation.py
│   ├── create_sample_pdf.py
│   └── create_invalid_pdf.py
│
├── tests/
│   └── test_extraction.py
│
├── reports/
├── screenshots/
├── docs/
├── requirements.txt
└── README.md
```

## 7. Required Libraries

Install the following Python libraries:

```bash
pip install PyMuPDF pandas openpyxl
```

## 8. How to Execute the Project

**Step 1:** Activate the virtual environment.

```powershell
.\.venv\Scripts\Activate.ps1
```

**Step 2:** Place PDF files inside the `data/input` folder.

**Step 3:** Run the main program.

```powershell
python src/main.py
```

**Step 4:** Check the generated Excel files inside `data/output`.

## 9. Output Files

**validated_invoices.xlsx**

Stores successfully extracted and validated invoice records.

**exception_report.xlsx**

Stores invalid records and their corresponding error details.

## 10. Testing

The project uses Python Unittest for testing.

Execute the test cases using:

```powershell
python -m unittest discover -s tests -v
```

### Test Results

| Test Case | Result |
|---|---|
| Valid Invoice | PASS |
| Invalid Email | PASS |
| Invalid Amount | PASS |

Total Test Cases: 3

Passed: 3

Failed: 0

## 11. Expected Benefits

- Reduces manual data entry.
- Saves processing time.
- Improves data accuracy.
- Identifies invalid invoice information.
- Supports processing multiple PDF documents.
- Generates structured Excel reports.

## 12. Conclusion

The Automated PDF Data Extraction project successfully automates the process of reading PDF invoices, extracting important information, validating records, and generating Excel reports.

The system also identifies invalid records and generates exception reports. This project demonstrates how Python-based automation can simplify document processing and reduce manual work.

## 13. Future Enhancements

- Support for scanned PDF documents using OCR.
- Support for different invoice formats.
- Graphical user interface.
- Database integration.
- Advanced reporting and analytics.