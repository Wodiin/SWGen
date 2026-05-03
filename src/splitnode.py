from textnode import TextNode, TextType

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
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes
    