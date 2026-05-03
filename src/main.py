import os
import shutil
import createpage
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    create_folder("docs")
    copy_folder_and_files("static", "docs")
    createpage.generate_pages_recursive("content", "template.html", "docs", basepath)


def create_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    os.makedirs(folder_name)

def copy_folder_and_files(src, dest):
    os.makedirs(dest, exist_ok=True)
    for item in os.listdir(src):
        path = os.path.join(src, item)
        if os.path.isfile(path):
            shutil.copy(path, dest)
        else:
            copy_folder_and_files(path, os.path.join(dest, item))
    


if __name__ == "__main__":
    main()