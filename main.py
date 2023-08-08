from io import BytesIO
from openpyxl import Workbook

import streamlit as st
import random
import string


def generate_random_data(size: int):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size * 1024 * 1024))


def generate_excel_file(rows: int, columns: int) -> BytesIO:
    excel_data = BytesIO()

    wb = Workbook()
    ws = wb.active

    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(columns)]
        ws.append(row)

    wb.save(excel_data)
    excel_data.seek(0)

    return excel_data


def estimate_excel_size(rows: int, columns: int):
    int_size_bytes = 4
    estimated_size_bytes = rows * columns * int_size_bytes
    estimated_size_mb = estimated_size_bytes / (1024 * 1024)

    return estimated_size_mb


def main():
    st.title("File Generator App")

    extension = st.selectbox("Select File Extension", ["xlsx", "txt"])

    if extension == "xlsx":
        rows = st.number_input("Enter Desired Number of Rows", min_value=1, step=1)
        columns = st.number_input("Enter Desired Number of Columns", min_value=1, step=1)
        estimated_size = estimate_excel_size(rows, columns)
        st.text(f"Estimated Excel file size: {estimated_size:.2f} MB")
    else:
        size = st.number_input("Enter Desired File Size (MB)", min_value=1, step=1)

    if st.button("Generate"):
        data = None
        mime = None

        if extension == "txt":
            data = generate_random_data(size).encode()
            mime = "text/plain"
        elif extension == "xlsx":
            data = generate_excel_file(rows, columns).read()
            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        filename = f"generated_file.{extension}"

        if data:
            st.download_button(
                label="Click to Download",
                data=data,
                file_name=filename,
                mime=mime
            )


if __name__ == "__main__":
    main()
