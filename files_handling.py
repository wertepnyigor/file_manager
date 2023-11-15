#This file will be responsible for actions with files. Different functions of module os will help to create,
#open, close etc. files between locations. In text files it will be also possible to open file in chosen
#program (Word, Pages etc." and makes changes.

import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

def open_finder():
    read = easygui.fileopenbox()
    return read

def open_file():
    file_name = open_finder()
    try:
        os.startfile(file_name)
    except:
        mb.showinfo("Confirm", "File not found.")
    pass

def move_file():
    old_path = open_finder()
    new_path = filedialog.askdirectory()
    if old_path == new_path:
        mb.showinfo("Confirm", "Old path and new path are the same, nothing done")
    else:
        shutil.move(old_path, new_path)
        mb.showinfo("Confirm", "File is in new path")
    pass

def delete_file():
    file_to_delete = open_finder()
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
    else:
        mb.showinfo("Confirm", "File does not exist!")
def change_name():
    file_to_change = open_finder()
    old_name = os.path.dirname(file_to_change)
    extension = os.path.splitext(file_to_change)[1]
    print("What is the name for new file?: ")
    new_name = input()
    new_path = os.path.join(old_name, new_name + extension)
    print(new_path)
    os.rename(file_to_change, new_name)
    mb.showinfo("Confirm", "File name changed.")

def make_directory():
    directory_path = filedialog.askdirectory()
    print("Enter name of new directory")
    directory_name = input()
    new_directory_path = os.path.join(directory_path, directory_name)

    os.mkdir(new_directory_path)
    mb.showinfo("Confirm", "New directory created!")



