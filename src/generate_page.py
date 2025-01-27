from markdown_to_html_node import markdown_to_html_node
from extract_markdown import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        source_file = file.read()
    with open(template_path, 'r') as file:
        template = file.read()
    
    conversion = markdown_to_html_node(source_file)
    converted_file = conversion.to_html()
    page_title = extract_title(source_file)
    mod_template = template.replace("{{ Title }}", page_title)
    completed_page = mod_template.replace("{{ Content }}", converted_file)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(completed_page)
        
def generate_page_recursive(from_path, template_path, dest_path):
    if os.path.isfile(from_path):
        generate_page(from_path, template_path, dest_path)
    else:
        for root, dirs, files in os.walk(from_path):
            for file in files:
                if file.endswith(".md"):
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, from_path)
                    dest_file = os.path.splitext(relative_path)[0] + ".html"
                    dest_file_path = os.path.join(dest_path, dest_file)
                    generate_page(source_path, template_path, dest_file_path)
    
    
    