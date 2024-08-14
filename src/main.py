#!/usr/bin/python3
from textnode import TextNode
from htmlnode import ParentNode, LeafNode

def main():
    node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode("b", "Bold Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
    html_string = node1.to_html()
    print(html_string)


if __name__ == "__main__":
    main()
