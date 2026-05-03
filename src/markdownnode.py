from htmlnode import ParentNode
from textnode import TextNode, TextType
from splitnode import markdown_to_blocks, text_to_textnodes
from blocknode import BlockType, block_to_block_type
from textnode_to_htmlnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    markdown_split_blocks = markdown_to_blocks(markdown)
    collection = []
    for block in markdown_split_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            collection.append(header_to_html_node(block))
        elif block_type == BlockType.PARAGRAPH:
            collection.append(paragraph_to_html_node(block))
        elif block_type == BlockType.CODE:
            collection.append(code_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            collection.append(quote_to_html_node(block))
        elif block_type == BlockType.UNLIST:
            collection.append(unlist_to_html_node(block))
        elif block_type == BlockType.OLIST:
            collection.append(olist_to_html_node(block))
        else:
            raise ValueError(f"Unsupported block type: {block_type}")
    return ParentNode(tag="div", children=collection)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def paragraph_to_html_node(paragraph):
    paragraph = paragraph.replace("\n", " ")
    children = text_to_children(paragraph)
    return ParentNode(tag="p", children=children)

def header_to_html_node(header):
    for level in range(1, 7):
        if header.startswith("#" * level + " "):
            tag = f"h{level}"
            header = header[level + 1:]
            break
    else:        
        raise ValueError("Invalid header format")
    children = text_to_children(header)
    return ParentNode(tag=tag, children=children)

def code_to_html_node(code):
    text_node = TextNode(code[3:].lstrip("\n")[:-3], TextType.CODE_TEXT)
    html_node = text_node_to_html_node(text_node)
    return ParentNode(tag="pre", children=[html_node])

def quote_to_html_node(quote):
    lines = quote.split("\n")
    if not all(line.startswith(">") for line in lines):
        raise ValueError("Invalid quote format")
    quote = " ".join(line[1:].lstrip(" ") for line in lines)
    children = text_to_children(quote)
    return ParentNode(tag="blockquote", children=children)

def unlist_to_html_node(unlist):
    lines = unlist.split("\n")
    if not all(line.startswith("- ") for line in lines):
        raise ValueError("Invalid unordered list format")
    items = [line[2:].lstrip(" ") for line in lines]
    children = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
    return ParentNode(tag="ul", children=children)

def olist_to_html_node(olist):
    lines = olist.split("\n")
    if not all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        raise ValueError("Invalid ordered list format")
    items = [line[line.find(". ") + 2:].lstrip(" ") for line in lines]
    children = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
    return ParentNode(tag="ol", children=children)
