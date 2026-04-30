import unittest

from htmlnode import HtmlNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_init(self):
        node = HtmlNode("div", "Hello World", [HtmlNode("span", "Nested")], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "span")
        self.assertEqual(node.children[0].value, "Nested")
        self.assertEqual(node.props, {"class": "container"})

    def test_props_to_html(self):
        node = HtmlNode(props={"class": "container", "id": "main"})
        props_html = node.props_to_html()
        self.assertIn('class="container"', props_html)
        self.assertIn('id="main"', props_html)

    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div_with_props(self):
        node = LeafNode("Content", "div", {"class": "container"})
        self.assertNotEqual(node.to_html(), '<div class="container">Content</div>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode("Just text", None)
        self.assertEqual(node.to_html(), "Just text")
    

if __name__ == "__main__":
    unittest.main()