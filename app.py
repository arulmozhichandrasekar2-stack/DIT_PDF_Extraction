
import streamlit as st
import pymupdf
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Automated PDF Data Extraction",
    page_icon="📄",
    layout="wide"
)

# -------------------- LOAD EXTERNAL CSS --------------------

with open("style.css", "r", encoding="utf-8") as css_file:
    st.markdown(
        f"<style>{css_file.read()}</style>",
        unsafe_allow_html=True
    )


# -------------------- HEADER --------------------

header_left, header_right = st.columns([3, 2])

with header_left:
    try:
        st.image("assets/logo.png", width=190)
    except Exception:
        st.markdown("### Define InfoTech")

with header_right:
    st.markdown("""
    <div class="project-id">
        DIT-P11<br>
        TEAM T11
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------------------- HERO --------------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">SMART DOCUMENT AUTOMATION</div>
    <h1>Automated PDF Data Extraction</h1>
    <p>
        Extract readable text, important fields and tables
        from your PDF documents quickly and easily.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------- PDF UPLOAD --------------------

st.markdown('<div class="upload-title">Upload Your PDF</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="upload-subtitle">
    Choose a PDF document to extract its text, fields and tables.
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Browse PDF",
    type=["pdf"],
    help="Upload a text-based PDF document"
)

# -------------------- EXTRACTION --------------------

if uploaded_file is not None:

    st.success(f"Selected file: {uploaded_file.name}")

    if st.button("Extract PDF", use_container_width=True):

        try:
            document = pymupdf.open(
                stream=uploaded_file.getvalue(),
                filetype="pdf"
            )

            all_text = []
            all_fields = []
            all_tables = []

            for page_number, page in enumerate(document, start=1):

                page_text = page.get_text("text")

                all_text.append({
                    "Page": page_number,
                    "Text": page_text
                })

                for line in page_text.splitlines():
                    if ":" in line:
                        key, value = line.split(":", 1)
                        key = key.strip()
                        value = value.strip()

                        if key and value:
                            all_fields.append({
                                "Page": page_number,
                                "Field": key,
                                "Value": value
                            })

                try:
                    found_tables = page.find_tables()

                    for table_number, table in enumerate(
                        found_tables.tables, start=1
                    ):
                        table_data = table.extract()

                        if table_data:
                            all_tables.append({
                                "Page": page_number,
                                "Table": table_number,
                                "Data": table_data
                            })

                except Exception:
                    pass

            st.session_state["extracted_text"] = all_text
            st.session_state["extracted_fields"] = all_fields
            st.session_state["extracted_tables"] = all_tables

            st.success("PDF extraction completed successfully!")

        except Exception as error:
            st.error(f"Error while extracting PDF: {error}")

# -------------------- EXTRACTION RESULTS --------------------

if "extracted_text" in st.session_state:

    texts = st.session_state["extracted_text"]
    fields = st.session_state["extracted_fields"]
    tables = st.session_state["extracted_tables"]

    st.markdown("## Extraction Results")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Pages", len(texts))
    col2.metric("Extracted Fields", len(fields))
    col3.metric("Tables Found", len(tables))

    with st.expander("View Extracted Text", expanded=True):
        for item in texts:
            st.markdown(f"**Page {item['Page']}**")
            st.text_area(
                "Extracted content",
                item["Text"],
                height=180,
                key=f"text_{item['Page']}"
            )

    with st.expander("View Extracted Fields"):
        if fields:
            st.dataframe(
                pd.DataFrame(fields),
                use_container_width=True
            )
        else:
            st.info("No key-value fields were detected.")

    with st.expander("View Extracted Tables"):
        if tables:
            for item in tables:
                st.markdown(
                    f"**Page {item['Page']} - Table {item['Table']}**"
                )
                st.dataframe(
                    pd.DataFrame(item["Data"]),
                    use_container_width=True
                )
        else:
            st.info("No tables were detected.")

    # Excel download
    excel_buffer = BytesIO()

    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:

        pd.DataFrame(texts).to_excel(
            writer, sheet_name="Page Text", index=False
        )

        pd.DataFrame(fields).to_excel(
            writer, sheet_name="Extracted Fields", index=False
        )

        for index, item in enumerate(tables, start=1):
            pd.DataFrame(item["Data"]).to_excel(
                writer,
                sheet_name=f"Table {index}"[:31],
                index=False
            )

    st.download_button(
        "Download Excel Report",
        data=excel_buffer.getvalue(),
        file_name="extracted_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    text_output = "\n\n".join(
        f"PAGE {item['Page']}\n{item['Text']}" for item in texts
    )

    st.download_button(
        "Download Extracted Text",
        data=text_output,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

# -------------------- TEAM MEMBERS --------------------

st.markdown("""
<div class="team-heading">Team Members</div>

<div class="team-card">
    <div class="team-member">
        Anu Keerthana R S - DIT2026S1103
    </div>
    <div class="team-member">
        Arulmozhi C - DIT2026S1104
    </div>
    <div class="team-member">
        Riyaa Shree K - DIT2026S1106
    </div>
</div>
""", unsafe_allow_html=True)
