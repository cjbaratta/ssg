from htmlnode import HTMLNode, LeafNode, ParentNode
from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        match block_type:
            case "paragraph":
                node = ParentNode("p", "", text_to_children(block))
            case "heading":
                level = 0
                for char in block:
                    if char == "#":
                        level += 1
                    else:
                        break
                text = block[level:].strip()
                node = ParentNode(f"h{level}", "", text_to_children(text))
            case "code":
                text = block.strip("```").strip()
                node = ParentNode("pre", "", [LeafNode("code", text)])
            case "quote":
                text = "\n".join(line[1:].strip() for line in block.split("\n"))
                node = ParentNode("blockquote", "", text_to_children(text))
            case "unordered_list":
                items = []
                for line in block.split("\n"):
                    text = line.strip("* -").strip()
                    items.append(ParentNode("li", "", text_to_children(text)))
                node = ParentNode("ul", "", items)
            case "ordered_list":
                items = []
                for line in block.split("\n"):
                    text = line.split(". ", 1)[1].strip()
                    items.append(ParentNode("li", "", text_to_children(text)))
                node = ParentNode("ol", "", items)
        
        children.append(node)
    
    return ParentNode("div", "", children)