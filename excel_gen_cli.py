import os

from main import estimate_excel_size, generate_excel_file

if __name__ == "__main__":
    num_rows = int(input("Enter number of rows: "))
    num_columns = int(input("Enter number of columns: "))
    print(f"Estimated Excel file size: {estimate_excel_size(num_rows, num_columns):.2f} MB")
    stop = input("Continue? (y/n): ")

    excel_data = generate_excel_file(num_rows, num_columns)
    filename = "generated_file.xlsx"

    with open(filename, "wb") as f:
        f.write(excel_data.read())

    print(f"File saved as {filename}")
    print(f"File size: {os.path.getsize(filename) / (1024 * 1024):.2f} MB")
