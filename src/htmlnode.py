
# This file defines the HtmlNode and LeafNode classes for representing HTML structures.
# The HtmlNode class represents an HTML element with a tag, value, children, and properties. 
# It includes a method to convert properties to HTML attributes and a placeholder for the to_html method, 
# which must be implemented by subclasses. 
# The LeafNode class represents a leaf node in the HTML structure, which contains a value, tag, and properties.
# It implements the to_html method to generate the HTML representation of the leaf node.


class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented by subclasses")
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        return f" {' '.join(f'{key}=\"{value}\"' for key, value in self.props.items())}"
    
    def __repr__(self):
        return f"HtmlNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode:
    def __init__(self, value, tag, props=None):
        self.value = value
        self.tag = tag
        self.props = props if props is not None else {}
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
            
        if self.tag is None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(value={self.value}, tag={self.tag}, props={self.props})"