from copy_static import copy_static
import os


def main():
    static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
    copy_static(static_path)


main()