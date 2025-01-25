import os
import shutil

def copy_static(folder):
    public_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    shutil.copytree(folder, public_path)