from tempfile import template
from copy_static import copy_static
import os
from generate_page import generate_page_recursive


def main():
    static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
    copy_static(static_path)
    root_dir = os.path.dirname(os.path.dirname(__file__))
    content = f"{root_dir}/content"
    template = f"{root_dir}/template.html"
    destination= f"{root_dir}/public"
    generate_page_recursive(content, template, destination)


main()