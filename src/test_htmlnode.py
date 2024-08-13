import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("h1", "Test Header", [], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), f'href="https://www.google.com" target="_blank"')

    def test_to_html(self):
        node1 = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node1.to_html()

    def test_default(self):
        node1 = HTMLNode()
        self.assertEqual(node1.tag, None)

if __name__ == "__main__":
    unittest.main()
