import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a normal paragraph with text."
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_heading(self):
        blocks = [
            "# Heading 1",
            "## Heading 2",
            "### Heading 3",
            "#### Heading 4",
            "##### Heading 5",
            "###### Heading 6",
        ]
        for block in blocks:
            self.assertEqual(block_to_block_type(block), "heading")

    def test_not_heading(self):
        blocks = [
            "#Not a heading",  # No space after #
            "####### Too many #s",  # More than 6 #s
        ]
        for block in blocks:
            self.assertEqual(block_to_block_type(block), "paragraph")

    def test_code(self):
        block = "```\ndef hello():\n    print('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_quote(self):
        blocks = [
            ">Single line quote",
            ">First line\n>Second line\n>Third line",
        ]
        for block in blocks:
            self.assertEqual(block_to_block_type(block), "quote")

    def test_unordered_list(self):
        blocks = [
            "* First item\n* Second item\n* Third item",
            "- First item\n- Second item\n- Third item",
        ]
        for block in blocks:
            self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_not_ordered_list(self):
        blocks = [
            "1. First item\n3. Third item\n2. Second item",  # Wrong order
            "0. First item\n1. Second item\n2. Third item",  # Starts with 0
            "2. First item\n3. Second item\n4. Third item",  # Starts with 2
        ]
        for block in blocks:
            self.assertEqual(block_to_block_type(block), "paragraph")

if __name__ == "__main__":
    unittest.main()