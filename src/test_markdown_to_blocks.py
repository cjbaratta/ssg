import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        md = "This is a single block."
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0], "This is a single block.")

    def test_multiple_blocks(self):
        md = """
This is the first block.

This is the second block.
This is still the second block.

* List item 1
* List item 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "This is the first block.")
        self.assertEqual(blocks[1], "This is the second block.\nThis is still the second block.")
        self.assertEqual(blocks[2], "* List item 1\n* List item 2")

    def test_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_only_whitespace(self):
        md = "    \n\n   \n\t   \n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_line_blocks(self):
        md = "Block 1\n\nBlock 2\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "Block 1")
        self.assertEqual(blocks[1], "Block 2")
        self.assertEqual(blocks[2], "Block 3")

    def test_mixed_whitespace_separators(self):
        md = "Block 1\n  \n\nBlock 2\n\n  \nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "Block 1")
        self.assertEqual(blocks[1], "Block 2")
        self.assertEqual(blocks[2], "Block 3")


    def test_multiple_consecutive_newlines(self):
        md = "Block 1\n\n\n\nBlock 2\n\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "Block 1")
        self.assertEqual(blocks[1], "Block 2")
        self.assertEqual(blocks[2], "Block 3")

if __name__ == "__main__":
    unittest.main()