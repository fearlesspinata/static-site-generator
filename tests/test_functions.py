import unittest
from src.functions import *
from src.textnode import TextNode

class testTextToHTML(unittest.TestCase):
    def test_text_type(self):
        text_node = TextNode("test text", "text")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.value, "test text")
        self.assertEqual(converted_node.tag, None)

    def test_bold_type(self):
        text_node = TextNode("test bold", "bold")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.value, "test bold")
        self.assertEqual(converted_node.tag, "b")

    def test_italic_type(self):
        text_node = TextNode("test italic", "italic")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.value, "test italic")
        self.assertEqual(converted_node.tag, "i")

    def test_code_type(self):
        text_node = TextNode("test code", "code")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.value, "test code")
        self.assertEqual(converted_node.tag, "code")

    def test_link_type(self):
        text_node = TextNode("anchor text", "link", "https://testlink.com")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.value, "anchor text")
        self.assertEqual(converted_node.props, {"href": "https://testlink.com"})
        self.assertEqual(converted_node.tag, "a")

    def test_image_type(self):
        text_node = TextNode("source image", "image", "source.png")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node.props, {"src": "source.png", "alt": "source image"})
        self.assertEqual(converted_node.tag, "img")

    def test_invalid_type(self):
        text_node = TextNode("invalid tag", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)
