import os
import shutil
import createpage

def main():
    create_folder("public")
    copy_folder_and_files("static", "public")
    createpage.generate_pages_recursive("content", "template.html", "public")


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