
# This module defines the HtmlNode class and its subclasses LeafNode and ParentNode, which represent nodes in an HTML document structure.
# The HtmlNode class serves as a base class for both leaf and parent nodes, containing common attributes such as tag, value, children, and props.
# tag represents the HTML tag (e.g., "p", "b", "i"), value holds the text content for leaf nodes, children is a list of child nodes for parent nodes, and props is a dictionary of HTML attributes. 
# The LeafNode class represents a node that contains a value and has no children, while the ParentNode class represents a node that can have children.


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
    
    def __eq__(self, other):
        if not isinstance(other, HtmlNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def __repr__(self):
        return f"HtmlNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
            
        if self.tag is None:
            return self.value
        
        if self.tag in ["img"]:
            return f"<{self.tag}{self.props_to_html()}>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(value={self.value}, tag={self.tag}, props={self.props})"

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have at least one child")
        
        else:
            children_html = "".join(child.to_html() for child in self.children)
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"