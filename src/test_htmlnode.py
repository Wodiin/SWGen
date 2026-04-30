import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode, ParentNode

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
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div_with_props(self):
        node = LeafNode("div", "Content", {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container">Content</div>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", {"class": "child-class"})
        parent_node = ParentNode("div", [child_node], {"id": "parent-id"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="parent-id"><span class="child-class">child</span></div>',
        )
    def test_to_html_with_empty_props(self):
        child_node = LeafNode("span", "child", {})
        parent_node = ParentNode("div", [child_node], {})
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )
    def test_to_html_with_none_props(self):
        child_node = LeafNode("span", "child", None)
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )
    def test_to_html_with_none_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_none_tag(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()
    

    

if __name__ == "__main__":
    unittest.main()