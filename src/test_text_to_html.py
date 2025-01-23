import unittest
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextToHTML(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        self.assertEqual(
            text_node_to_html_node(node).to_html(),
            "Hello, world!",
        )
        node = TextNode("Hello, world!", TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(node).to_html(),
            "<b>Hello, world!</b>",
        )
        node = TextNode("Hello, world!", TextType.ITALIC)
        self.assertEqual(
            text_node_to_html_node(node).to_html(),
            "<i>Hello, world!</i>",
        )
        node = TextNode("Hello, world!", TextType.CODE)
        self.assertEqual(
            text_node_to_html_node(node).to_html(),"<code>Hello, world!</code>",)
        node = TextNode("Hello, world!", TextType.LINK, "https://boot.dev")
        self.assertEqual(
            text_node_to_html_node(node).to_html(),
            '<a href="https://boot.dev">Hello, world!</a>',
        )
        node = TextNode("Hello, world!", TextType.IMAGE, "https://boot.dev")
        self.assertEqual(
            text_node_to_html_node(node).to_html(),
            '<img src="https://boot.dev" alt="Hello, world!"></img>',
        )

    def test_invalid_text_to_html(self):  
        with self.assertRaises(ValueError):
                text_node_to_html_node(TextNode(TextType.LINK, "Hello, world!"))
        with self.assertRaises(ValueError):
                text_node_to_html_node(TextNode(TextType.IMAGE, "Hello, world!"))