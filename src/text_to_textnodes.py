from textnode import TextNode, TextType
from split_node import split_node_delimiter, split_node_image, split_node_link

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_node_image(nodes)
    nodes = split_node_link(nodes)
    nodes = split_node_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_node_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_node_delimiter(nodes, "`", TextType.CODE)
    return nodes
