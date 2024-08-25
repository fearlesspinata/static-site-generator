import functools

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            prop_string = []
            for key, value in self.props.items():
                prop_string.append(f'{key}="{value}"')
            return ' '.join(prop_string)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node requires a value")
        elif not self.tag:
            return self.value
        else:
            if not self.props:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if not self.children:
            raise ValueError("Invalid HTML: no children")
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
