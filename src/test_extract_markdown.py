import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title

class TestExtractMarkdown(unittest.TestCase):
    def test_no_images(self):
        text = "Hello, world!"
        self.assertEqual(extract_markdown_images(text), [])

    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_links(self):
        text = "This is text with a [link](https://boot.dev) and [another link](https://boot.dev)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link", "https://boot.dev"),
                ("another link", "https://boot.dev"),
            ],
        )
        
    def test_title(self):
        text = "# This is a title"
        self.assertEqual(extract_title(text), ["This is a title"])
        
    def test_title_no_title(self):
        text = "This is text with no title"
        self.assertRaises(Exception, extract_title, text)
        
    