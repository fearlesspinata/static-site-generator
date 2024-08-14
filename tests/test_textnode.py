import unittest

from src.textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url(self):
        node1 = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold", "http://www.test.com")
        self.assertIsNotNone(node2.url)
        self.assertIsNone(node1.url)

    def test_false_eq(self):
        node1 = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
