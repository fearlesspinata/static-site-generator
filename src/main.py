#!/usr/bin/python3
from textnode import TextNode
from htmlnode import ParentNode, LeafNode

text_node = TextNode("testing", "text")
print(text_node)
def main():
    node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode("b", "Bold Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
                ParentNode("p",
                           [
                               LeafNode("i", "child1 of child4"),
                               LeafNode(None, "child2 of child4"),
                               LeafNode("b", "child3 of child4"),
                           ],
                       )
            ],
        )

if __name__ == "__main__":
    main()
