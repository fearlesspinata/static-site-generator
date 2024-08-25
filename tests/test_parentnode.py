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
