import unittest
from src.htmlnode import ParentNode, LeafNode

class TestParent(unittest.TestCase):
    def test_three_child(self):
        node1 = ParentNode(
                "p",
                [
                    LeafNode("i", "Italic Text"),
                    LeafNode("b", "Bold Text"),
                    LeafNode("b", "Bold Text"),
                ],
            )
        self.assertEqual(node1.to_html(), None)
