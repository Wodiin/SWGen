import unittest

from splitnode import markdown_to_blocks, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextNode, TextType

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.example.com/second)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINKS, "https://www.example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINKS, "https://www.example.com/second"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links_no_image(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and an image ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINKS, "https://www.example.com"),
                TextNode(" and an image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_links_no_link(self):
        node = TextNode(
            "This is text with an image ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_text_to_textnode(self):
        text = "This is **bold** text and _italic_ text with a `code` snippet."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " text and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " text with a ")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)
        self.assertEqual(nodes[5].text, "code")
        self.assertEqual(nodes[5].text_type, TextType.CODE_TEXT)
        self.assertEqual(nodes[6].text, " snippet.")
        self.assertEqual(nodes[6].text_type, TextType.TEXT)
    
    def test_text_to_textnode_with_links_and_images(self):
        text = "This is a [link](https://www.example.com) and an image ![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].text_type, TextType.LINKS)
        self.assertEqual(nodes[1].url, "https://www.example.com")
        self.assertEqual(nodes[2].text, " and an image ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "image")
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[3].url, "https://i.imgur.com/zjjcJKZ.png")
    
    def test_text_to_textnode_empty(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("")
        with self.assertRaises(ValueError):
            text_to_textnodes(None)
    
    def test_text_to_textnode_no_formatting(self):
        text = "This is plain text with no formatting."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, text)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    
    def test_text_to_textnode_only_formatting(self):
        text = "**Bold** _Italic_ `Code` [Link](https://www.example.com) ![Image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 9)
        self.assertEqual(nodes[0].text, "Bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text, " ")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text, "Italic")
        self.assertEqual(nodes[2].text_type, TextType.ITALIC)
        self.assertEqual(nodes[3].text, " ")
        self.assertEqual(nodes[3].text_type, TextType.TEXT)
        self.assertEqual(nodes[4].text, "Code")
        self.assertEqual(nodes[4].text_type, TextType.CODE_TEXT)
        self.assertEqual(nodes[5].text, " ")
        self.assertEqual(nodes[5].text_type, TextType.TEXT)
        self.assertEqual(nodes[6].text, "Link")
        self.assertEqual(nodes[6].text_type, TextType.LINKS)
        self.assertEqual(nodes[6].url, "https://www.example.com")
        self.assertEqual(nodes[7].text, " ")
        self.assertEqual(nodes[7].text_type, TextType.TEXT)
        self.assertEqual(nodes[8].text, "Image")
        self.assertEqual(nodes[8].text_type, TextType.IMAGE)
        self.assertEqual(nodes[8].url, "https://i.imgur.com/zjjcJKZ.png")

    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
    
if __name__ == "__main__":
    unittest.main()