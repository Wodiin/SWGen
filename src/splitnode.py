from textnode import TextNode, TextType
from regexextract import extract_markdown_images, extract_markdown_links

# The split_nodes_delimiter function takes a list of TextNode instances, a delimiter string, and a TextType for the new nodes.
# It splits the text of each TextNode that contains the delimiter into parts and creates new TextNode instances based on the specified TextType for the parts between the delimiters.

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT and delimiter in node.text:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Invalid Markdown: Unmatched delimiter")
            for i, part in enumerate(parts):
                if part == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes
    
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_images(node.text)
            remainder = node.text
            if len(matches) == 0:
                new_nodes.append(node)
                continue
            for alt_text, url in matches:
                parts = remainder.split(f"![{alt_text}]({url})", 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                remainder = parts[1] if len(parts) > 1 else ""
            if remainder:
                new_nodes.append(TextNode(remainder, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes
                 

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_links(node.text)
            remainder = node.text
            if len(matches) == 0:
                new_nodes.append(node)
                continue
            for link_text, url in matches:
                parts = remainder.split(f"[{link_text}]({url})", 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINKS, url))
                remainder = parts[1] if len(parts) > 1 else ""
            if remainder:
                new_nodes.append(TextNode(remainder, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes


def text_to_textnodes(text):
    if text is None or text == "":
        raise ValueError("Input text cannot be None or empty")
    result = [TextNode(text, TextType.TEXT)]
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    result = split_nodes_delimiter(result, "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE_TEXT)
    return result  

    
def markdown_to_blocks(text):
    return_list = []
    blocks = text.split("\n\n")
    blocks = [block.strip() for block in blocks]
    for block in blocks:
        if block == "":
            continue
        return_list.append(block)
    return return_list