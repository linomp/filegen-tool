import streamlit as st
import random
import string


def generate_random_data(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size * 1024 * 1024))


def main():
    st.title("File Generator App")

    # TODO: support excel and others
    extension = st.selectbox("Select File Extension", ["txt"])
    size = st.number_input("Enter Desired File Size (MB)", min_value=1, step=1)

    if st.button("Generate"):
        random_data = generate_random_data(size)
        filename = f"generated_file.{extension}"

        st.download_button(
            label="Click to Download",
            data=random_data.encode(),
            file_name=filename,
            mime="text/plain"
        )


if __name__ == "__main__":
    main()
