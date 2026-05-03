
from htmlnode import LeafNode, ParentNode
from splitnode import text_to_textnodes
from textnode import TextType


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        split_text = text_to_textnodes(text_node.text)
        children = [text_node_to_html_node(node) for node in split_text]
        return ParentNode("b", children)
    elif text_node.text_type == TextType.ITALIC:
        split_text = text_to_textnodes(text_node.text)
        children = [text_node_to_html_node(node) for node in split_text]
        return ParentNode("i", children)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINKS:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")