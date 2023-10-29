
#This file will be responsible for actions with files. Different functions of module os will help to create,
#open, close etc. files between locations. In text files it will be also possible to open file in chosen
#program (Word, Pages etc." and makes changes.


from tkinter import *
count = 0


def click():
    global count
    count += 1
    print(f"You clicked the button {count} times. ")