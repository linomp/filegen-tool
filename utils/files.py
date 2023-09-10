import random
import string
from io import BytesIO

from openpyxl import Workbook


def generate_random_data(size_bytes: int):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size_bytes))


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
