import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node4)
        
        node5 = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        self.assertNotEqual(node, node5)

        node6 = TextNode("this is to test url with no url input", TextType.LINKS)
        node7 = TextNode("this is to test url with no url input", TextType.LINKS, None)
        node8 = TextNode("this is to test url with no url input", TextType.LINKS, "")
        node9 = TextNode("this url should work", TextType.LINKS, "https://www.example.com")
        self.assertNotEqual(node9, node7)
        self.assertNotEqual(node9, node8)
        self.assertNotEqual(node9, node6)

        node10 = TextNode("this is to test code text", TextType.CODE_TEXT)
        node11 = TextNode("this is to test code text", TextType.CODE_TEXT)
        self.assertEqual(node10, node11)
        

if __name__ == "__main__":
    unittest.main()