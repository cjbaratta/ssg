import unittest
from split_node_delimiter import split_node_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_note_delimiter(self):
        nodes = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("world!", TextType.BOLD),
        ]
        new_nodes = split_node_delimiter(nodes, ", ", TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "world!")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
    
    def test_auto_append_if_not_text(self):
        nodes = [TextNode("`def hello() `", TextType.CODE)]
        new_nodes = split_node_delimiter(nodes, "`", TextType.TEXT)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "`def hello() `")
        self.assertEqual(new_nodes[0].text_type, TextType.CODE)

    def test_longer_nodes(self):
        nodes = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("world!", TextType.BOLD),
            TextNode("Hello, ", TextType.TEXT),
            TextNode("world!", TextType.BOLD),
        ]
        new_nodes = split_node_delimiter(nodes, ", ", TextType.BOLD)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "world!")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, "Hello")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "world!")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)


