import unittest
import markdownnode

class TestMarkdownNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "This is a paragraph.\n\nThis is another paragraph.\n\nThis is a third paragraph."
        expected = ["This is a paragraph.", "This is another paragraph.", "This is a third paragraph."]
        result = markdownnode.markdown_to_blocks(text)
        self.assertEqual(result, expected)
    
    def test_markdown_to_blocks_with_empty_blocks(self):
        text = "This is a paragraph.\n\n\n\nThis is another paragraph.\n\n\n\nThis is a third paragraph."
        expected = ["This is a paragraph.", "This is another paragraph.", "This is a third paragraph."]
        result = markdownnode.markdown_to_blocks(text)
        self.assertEqual(result, expected)
    
    def test_markdown_to_html_node(self):
        markdown = "# Header\n\nThis is a paragraph with **bold** text and _italic_ text.\n\n- Item 1\n- Item 2\n- Item 3"
        html_node = markdownnode.markdown_to_html_node(markdown)
        expected_html = "<div><h1>Header</h1><p>This is a paragraph with <b>bold</b> text and <i>italic</i> text.</p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        self.assertEqual(html_node.to_html(), expected_html)
    
    def test_markdown_to_html_node_with_code_and_quote(self):
        markdown = "```\nCode block\n```\n\n> This is a quote."
        html_node = markdownnode.markdown_to_html_node(markdown)
        expected_html = "<div><pre><code>Code block\n</code></pre><blockquote>This is a quote.</blockquote></div>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_with_links_and_images(self):
        markdown = "This is a [link](https://example.com) and this is an image: ![alt text](https://example.com/image.jpg)"
        html_node = markdownnode.markdown_to_html_node(markdown)
        expected_html = "<div><p>This is a <a href=\"https://example.com\">link</a> and this is an image: <img src=\"https://example.com/image.jpg\" alt=\"alt text\"></p></div>"
        self.assertEqual(html_node.to_html(), expected_html)
    
    def test_markdown_to_html_node_with_nested_formatting(self):
        markdown = "This is a paragraph with **bold and _italic_ text**."
        html_node = markdownnode.markdown_to_html_node(markdown)
        expected_html = "<div><p>This is a paragraph with <b>bold and <i>italic</i> text</b>.</p></div>"
        self.assertEqual(html_node.to_html(), expected_html)
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdownnode.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdownnode.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()