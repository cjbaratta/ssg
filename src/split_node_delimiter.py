from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        text_parts = node.text.split(delimiter)
        # If no delimiter found, keep original node
        if len(text_parts) == 1:
            new_nodes.append(node)
            continue
            
        # Handle alternating text/delimited sections
        for i in range(len(text_parts)):
            part = text_parts[i]
            if part:  # Skip empty strings
                if i % 2 == 0:
                    # Regular text sections
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    # Delimited sections
                    new_nodes.append(TextNode(part, text_type))
                    
    return new_nodes