import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import LeafNode, ParentNode

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_empty_markdown(self):
        node = markdown_to_html_node("")
        self.assertEqual(node.to_html(), "<div></div>")

    def test_single_paragraph(self):
        markdown = "This is a paragraph with **bold** and *italic* text."
        node = markdown_to_html_node(markdown)
        expected = '<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p></div>'
        self.assertEqual(node.to_html(), expected)

    def test_multiple_paragraphs(self):
        markdown = "First paragraph.\n\nSecond paragraph."
        node = markdown_to_html_node(markdown)
        expected = '<div><p>First paragraph.</p><p>Second paragraph.</p></div>'
        self.assertEqual(node.to_html(), expected)

    def test_headings(self):
        markdown = "# Heading 1\n\n## Heading 2\n\n### Heading 3"
        node = markdown_to_html_node(markdown)
        expected = '<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>'
        self.assertEqual(node.to_html(), expected)

    def test_code_block(self):
        markdown = "```\ndef hello():\n    print('Hello, world!')\n```"
        node = markdown_to_html_node(markdown)
        expected = '<div><pre><code>def hello():\n    print(\'Hello, world!\')</code></pre></div>'
        self.assertEqual(node.to_html(), expected)

    def test_blockquote(self):
        markdown = ">This is a quote\n>With multiple lines\n>And more text"
        node = markdown_to_html_node(markdown)
        expected = '<div><blockquote>This is a quote\nWith multiple lines\nAnd more text</blockquote></div>'
        self.assertEqual(node.to_html(), expected)

    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2\n* Item 3"
        node = markdown_to_html_node(markdown)
        expected = '<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>'
        self.assertEqual(node.to_html(), expected)

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item\n3. Third item"
        node = markdown_to_html_node(markdown)
        expected = '<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>'
        self.assertEqual(node.to_html(), expected)