import pytest
from main import generate_random_data, generate_excel_file, estimate_excel_size


def test_generated_file_size():
    rows = 1000
    columns = 20
    estimated_size = estimate_excel_size(rows, columns)

    tolerance = 0.1
    generated_file = generate_excel_file(rows, columns)

    generated_file_data = generated_file.read()
    generated_file_size_mb = len(generated_file_data) / (1024 * 1024)

    assert abs(generated_file_size_mb - estimated_size) < tolerance


@pytest.mark.parametrize("size_mb", [5])
def test_generate_random_data(size_mb):
    random_data = generate_random_data(size_mb)

    assert isinstance(random_data, str)
    assert len(random_data) >= size_mb * 1024 * 1024
