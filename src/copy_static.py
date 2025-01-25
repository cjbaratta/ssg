import os
import shutil

def copy_static(folder):
    if os.path.exists("/Users/cjbaratta/Projects/BootDev/ssg/public"):
        shutil.rmtree("/Users/cjbaratta/Projects/BootDev/ssg/public")
    shutil.copytree(folder, "/Users/cjbaratta/Projects/BootDev/ssg/public")