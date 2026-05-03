import unittest

from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.children, [text_node_to_html_node(TextNode("This is bold text", TextType.TEXT))])
    
    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.children, [text_node_to_html_node(TextNode("This is italic text", TextType.TEXT))])
    
    def test_code_text(self):
        node = TextNode("This is code text", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")

    def test_links(self):
        node = TextNode("This is a link", TextType.LINKS, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.example.com/image.png", "alt": "This is an image"})
        


if __name__ == "__main__":
    unittest.main()