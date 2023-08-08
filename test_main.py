import unittest
from main import generate_random_data


class TestGenerateExcelFile(unittest.TestCase):

    # def test_generate_excel_file(self):
    #     size_mb = 5  # Test with a desired size of 5 MB
    #     excel_data = generate_excel_file(size_mb)
    #
    #     self.assertIsInstance(excel_data, bytes)
    #     self.assertGreaterEqual(len(excel_data), size_mb * 1024 * 1024)

    def test__generate_random_data(self):
        size_mb = 5
        random_data = generate_random_data(size_mb)
        self.assertIsInstance(random_data, str)
        self.assertGreaterEqual(len(random_data), size_mb * 1024 * 1024)


if __name__ == '__main__':
    unittest.main()
