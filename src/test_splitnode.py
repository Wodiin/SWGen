import unittest

from splitnode import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        from textnode import TextNode, TextType
        old_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_unmatched(self):
        from textnode import TextNode, TextType
        old_nodes = [TextNode("This is **bold text", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)