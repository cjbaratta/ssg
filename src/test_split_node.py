import unittest
from split_node import split_node_delimiter, split_node_image, split_node_link
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
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

    def test_split_node_image(self):
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        ]
        new_nodes = split_node_image(nodes)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "rick roll")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "https://i.imgur.com/aKaOqIh.gif")

    def test_split_node_link(self):
        nodes = (TextNode("This is text with a [link](https://boot.dev)", TextType.TEXT))
        new_nodes = split_node_link([nodes])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "link")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].url, "https://boot.dev")

    def test_multiple_links(self):
        nodes = (TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,))
        new_nodes = split_node_link([nodes])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with a link ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "to boot dev")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "to youtube")
        self.assertEqual(new_nodes[3].text_type, TextType.LINK)
        self.assertEqual(new_nodes[3].url, "https://www.youtube.com/@bootdotdev")
        



