import unittest
from src.htmlnode import ParentNode, LeafNode

class TestParent(unittest.TestCase):
    def test_three_child(self):
        node1 = ParentNode(
                "p",
                [
                    LeafNode("i", "child1"),
                    LeafNode("b", "child2"),
                    LeafNode(None, "child3"),
                    ParentNode("p",
                               [
                                   LeafNode("i", "child1 of child4"),
                                   LeafNode(None, "child2 of child4"),
                                   LeafNode("b", "child3 of child4"),
                               ],
                           )
                ],
            )
        self.assertEqual(node1.to_html(), "<p><i>child1</i><b>child2</b>child3<p><i>child1 of child4</i>child2 of child4<b>child3 of child4</b></p></p>")

    def test_none_tag(self):
        node1 = ParentNode(
                None,
                [
                    LeafNode("i", "italics"),
                    LeafNode("b", "bold"),
                    LeafNode(None, "Normal"),
                    LeafNode("b", "bold"),
                ]
            )

        with self.assertRaises(ValueError):
            node1.to_html()

    def test_multiple_parent(self):
        node1 = ParentNode(
                "p",
                [
                    ParentNode("p",
                               [
                                   LeafNode("i", "italics"),
                                ]
                               ),
                    ParentNode("p",
                               [
                                   LeafNode("b", "bold"),
                               ]
                               ),
                    ParentNode("p",
                               [
                                   LeafNode(None, "Normal"),
                               ]
                               ),
                ],
            )

        self.assertEqual(node1.to_html(), "<p><p><i>italics</i></p><p><b>bold</b></p><p>Normal</p></p>")

    def test_leaf_child(self):
        node1 = ParentNode(
                "p",
                [
                    LeafNode("i", "italics"),
                    LeafNode("b", "bold"),
                    LeafNode(None, "normal"),
                    LeafNode("li", "ordered list"),
                    LeafNode("ul", "unordered list"),
                ]
                )
        self.assertEqual(node1.to_html(), "<p><i>italics</i><b>bold</b>normal<li>ordered list</li><ul>unordered list</ul></p>")

    def test_no_children(self):
        node1 = ParentNode("p", 'no children')
        with self.assertRaises(ValueError):
            node1.to_html()



