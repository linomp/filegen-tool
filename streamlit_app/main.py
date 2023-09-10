import streamlit as st

from utils.files import estimate_excel_size, generate_random_data, generate_excel_file


def main():
    st.title("File Generator App")

    extension = st.selectbox("Select File Extension", ["xlsx", "txt"])
    size = rows = columns = 0

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
            data = generate_random_data(size * 1024 * 1024).encode()
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
