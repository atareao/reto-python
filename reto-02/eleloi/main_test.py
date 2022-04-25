from dataclasses import dataclass
from typing import Any
import unittest
import main


@dataclass
class SampleData:
    data: Any
    expected: Any


class MainTest(unittest.TestCase):
    def test_get_user_directory(self):
        user_download_dir = main._get_user_download_directory()
        self.assertIsInstance(user_download_dir, str)
        self.assertTrue("downloads" in user_download_dir.lower())

    def test_jpg_files_in_dir(self):
        jpg_files = main._jpg_files_in_dir("./sample_dir")
        self.assertIsInstance(jpg_files, list)
        self.assertTrue(len(jpg_files) > 0)

    def test_str_list_formatter(self):
        sample_data = SampleData(
            data=[
                "with_number1.jpg",
                "whithout_number.jpg",
                "WITH_NUMBER2.JPG",
                "WITHOUT_NUMBER.JPG",
                "other_extension.jpeg",
                "upper_extension.JPG",
            ],
            expected=[
                "0 => with_number1.jpg",
                "1 WHITHOUT_NUMBER.JPG",
                "2 => with_number2.jpg",
                "3 WITHOUT_NUMBER.JPG",
                "4 => OTHER_EXTENSION.JPEG",
                "5 UPPER_EXTENSION.JPG",
            ],
        )

        results = main._str_list_formatter(sample_data.data)

        for idx, result in enumerate(results):
            expected = sample_data.expected[idx]
            self.assertTrue(result == expected)
