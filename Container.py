import os
import shutil

def create_ft1(path, type):
    name = input("Enter person " + type)
    if not os.path.isdir(name):
        os.mkdir(name)
    current_path = os.path.join(path, name)
    os.chdir(current_path)
    return current_path

def create_ft2(name):
    if not os.path.isdir(name):
        os.mkdir(name)

def show_content(path):
     print(os.listdir(path), end="\n")

def remove_item(path):
    shutil.rmtree(path)
