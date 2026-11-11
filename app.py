
import streamlit as st
import pymupdf
import pandas as pd
import re
from io import BytesIO

st.set_page_config(
    page_title="Automated PDF Data Extraction",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Automated PDF Data Extraction")
st.write(
    "Upload different types of PDF documents and automatically "
    "extract text, tables and important fields."
)

uploaded_file = st.file_uploader(
    "Upload any PDF document",
    type=["pdf"]
)


def extract_key_values(text):
    results = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        match = re.match(r"^([^:]{2,80}):\s*(.+)$", line)

        if match:
            results.append({
                "Field": match.group(1).strip(),
                "Value": match.group(2).strip()
            })

    return results


if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Extract Data", type="primary"):

        try:
            pdf_bytes = uploaded_file.getvalue()

            document = pymupdf.open(
                stream=pdf_bytes,
                filetype="pdf"
            )

            page_results = []
            all_text = []
            all_tables = []
            all_fields = []

            with st.spinner("Extracting PDF data..."):

                for page_number, page in enumerate(document, start=1):

                    page_text = page.get_text("text")
                    all_text.append(page_text)

                    page_results.append({
                        "Page": page_number,
                        "Extracted Text": page_text
                    })

                    for item in extract_key_values(page_text):
                        item["Page"] = page_number
                        all_fields.append(item)

                    try:
                        table_finder = page.find_tables()

                        for table_number, table in enumerate(
                            table_finder.tables, start=1
                        ):
                            table_data = table.extract()

                            if table_data:
                                df = pd.DataFrame(table_data)
                                all_tables.append(
                                    (page_number, table_number, df)
                                )

                    except Exception:
                        pass

            document.close()

            combined_text = "\n\n".join(all_text)

            st.success("PDF extraction completed!")

            st.subheader("Extraction Summary")
            col1, col2, col3 = st.columns(3)

            col1.metric("Total Pages", len(page_results))
            col2.metric("Extracted Fields", len(all_fields))
            col3.metric("Extracted Tables", len(all_tables))

            st.subheader("Full Extracted Text")

            for page in page_results:
                with st.expander(f"Page {page['Page']}"):
                    st.text(page["Extracted Text"] or
                            "No readable text found on this page.")

            if all_fields:
                st.subheader("Automatically Identified Fields")
                fields_df = pd.DataFrame(all_fields)
                st.dataframe(fields_df, use_container_width=True)
            else:
                fields_df = pd.DataFrame(
                    columns=["Field", "Value", "Page"]
                )
                st.info(
                    "No label-value fields detected. "
                    "Full extracted text is available above."
                )

            if all_tables:
                st.subheader("Extracted Tables")

                for page_no, table_no, table_df in all_tables:
                    st.write(
                        f"Page {page_no} - Table {table_no}"
                    )
                    st.dataframe(table_df, use_container_width=True)

            else:
                st.info("No structured tables detected in this PDF.")

            excel_buffer = BytesIO()

            with pd.ExcelWriter(
                excel_buffer, engine="openpyxl"
            ) as writer:

                pd.DataFrame(page_results).to_excel(
                    writer, sheet_name="Page Text", index=False
                )

                fields_df.to_excel(
                    writer, sheet_name="Extracted Fields", index=False
                )

                for index, (page_no, table_no, table_df) in enumerate(
                    all_tables, start=1
                ):
                    table_df.to_excel(
                        writer,
                        sheet_name=f"Table {index}"[:31],
                        index=False
                    )

            excel_buffer.seek(0)

            st.download_button(
                "Download Extracted Excel",
                data=excel_buffer.getvalue(),
                file_name="extracted_pdf_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            st.download_button(
                "Download Extracted Text",
                data=combined_text,
                file_name="extracted_pdf_text.txt",
                mime="text/plain"
            )

        except Exception as error:
            st.error(f"PDF Processing Error: {error}")
