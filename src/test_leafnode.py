import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_a_tag(self):
        node1 = LeafNode('a', 'apply', {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), '<a href="https://www.google.com">apply</a>')

    def test_p_tag(self):
        node1 = LeafNode('p', 'testing p tag')
        self.assertEqual(node1.to_html(), '<p>testing p tag</p>')

    def test_children(self):
        node1 = LeafNode('a', 'testing children', {"href": "https://www.google.com"})
        self.assertEqual(node1.children, None)
