import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    image = re.findall(pattern, text)
    return image

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links = re.findall(pattern, text)
    return links

def extract_title(text):
    pattern = r"^#\s+(.*?)\s*$"
    title = re.findall(pattern, text, re.MULTILINE)
    if title == []:
        raise Exception("No title found")
    result = str(title)
    return result