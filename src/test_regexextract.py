import unittest

from regexextract import extract_markdown_images, extract_markdown_links

class TestRegexExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "Here is an image: ![alt text](https://www.example.com/image.png)"
        matches = extract_markdown_images(text)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0][0], "alt text")
        self.assertEqual(matches[0][1], "https://www.example.com/image.png")

    def test_extract_markdown_links(self):
        text = "Here is a link: [link text](https://www.example.com)"
        matches = extract_markdown_links(text)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0][0], "link text")
        self.assertEqual(matches[0][1], "https://www.example.com")

    def test_extract_markdown_links_no_image(self):
        text = "Here is a link: [link text](https://www.example.com) and an image: ![alt text](https://www.example.com/image.png)"
        matches = extract_markdown_links(text)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0][0], "link text")
        self.assertEqual(matches[0][1], "https://www.example.com")
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()