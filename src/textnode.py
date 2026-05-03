from enum import Enum


# This file defines the TextNode class, which represents a piece of text with a specific formatting type (e.g., bold, italic, code, link, image). 
# The TextType enum is used to specify the type of formatting for the text. Each TextNode instance contains the text content, its formatting type, 
# and an optional URL for links and images. The class also includes methods for equality comparison and string representation.

class TextType(Enum):
    TEXT = "Plain text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE_TEXT = "`Code text`"
    LINKS = "[link text](url)"
    IMAGE = "![alt text](url)"

# The TextNode class represents a piece of text with a specific formatting type. It includes the text content, its formatting type, 
# and an optional URL for links and images.
class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # The __eq__ method allows for comparison between two TextNode instances, checking if their text, text type, and URL are the same.
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    
    # The __repr__ method provides a string representation of the TextNode instance, which is useful for debugging and logging purposes.
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, '{self.url}')"

