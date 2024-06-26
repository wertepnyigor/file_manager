#This file will be responsible for actions with files. Different functions of module os will help to create,
#open, close etc. files between locations. In text files it will be also possible to open file in chosen
#program (Word, Pages etc." and makes changes.

import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

def open_finder():
    read = easygui.fileopenbox() #open a file dialog window, helpful in files research
    return read #returns a opened file

def open_file():
    file_name = open_finder() #enables opening a Finder in every button usage
    try:
        os.startfile(file_name) #opens a file from chosen path
    except:
        mb.showinfo("Action done", "File not found.")
    pass

def move_file():
    old_path = open_finder()
    new_path = filedialog.askdirectory() #filedialog from tkinter lib, selection of path where to move a file
    if old_path == new_path:
        mb.showinfo("Action done", "Old path and new path are the same, nothing done")
    else:
        shutil.move(old_path, new_path) #shutil enables possibility for copying and archiving files
        mb.showinfo("Action done", "File is in new path")
    pass

def delete_file():
    file_to_delete = open_finder()
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
    else:
        mb.showinfo("Action done", "File does not exist!")

def change_name():
    file_to_change = open_finder()
    old_name = os.path.dirname(file_to_change)
    print("What is the name for new file?: ")
    new_name = input()
    new_path = os.path.join(old_name, new_name)
    print(new_path)
    os.rename(file_to_change, new_name)
    mb.showinfo("Action done", "File name changed.")

def make_directory():
    directory_path = filedialog.askdirectory()
    print("Enter name of new directory")
    directory_name = input()
    new_directory_path = os.path.join(directory_path, directory_name)

    os.mkdir(new_directory_path)
    mb.showinfo("Action done", "New directory created!")



