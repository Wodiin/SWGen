import unittest
from createpage import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_valid(self):
        markdown = "# This is a title"
        expected_title = "This is a title"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_extract_title_invalid(self):
        markdown = "This is not a title"
        with self.assertRaises(ValueError):
            extract_title(markdown)