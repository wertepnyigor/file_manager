from tkinter import *
from files_handling import *

loginWindow = Tk()
loginWindow.title("File Manager")
loginWindow.config(background="black")
loginWindow_width = 1000
loginWindow_height = 500
screen_width = loginWindow.winfo_screenwidth()
screen_height = loginWindow.winfo_screenheight()

x = int((screen_width / 2) - (loginWindow_width / 2))
y = int((screen_height / 2) - (loginWindow_height / 2))

loginWindow.geometry("{}x{}+{}+{}".format(loginWindow_width, loginWindow_height, x, y))

welcomeLabel = Label(loginWindow, text="Welcome in File Manager!", font=("Arial", 30, "bold"),
                     foreground='white', background='black', relief=RAISED, bd=10, padx=40, pady=40,
                     compound='top')
welcomeLabel.pack()

buttonsFrame = Frame(loginWindow)
buttonsFrame.pack()

open_finder_button = Button(buttonsFrame, text="Open Finder", command=open_finder, height=2, width=10)
open_finder_button.grid(row=0, column=0)
open_finder_button = Button(buttonsFrame, text="Open Finder", command=open_finder, height=2, width=10)
open_finder_button.grid(row=0, column=0)

open_file_button = Button(buttonsFrame, text="Open File", command=open_file, height=2, width=10)
open_file_button.grid(row=0, column=1)

move_file_button = Button(buttonsFrame, text="Move file", command=move_file, height=2, width=10)
move_file_button.grid(row=0, column=2)

delete_file_button = Button(buttonsFrame, text="Delete file", command=delete_file, height=2, width=10)
delete_file_button.grid(row=1, column=0)

change_name_button = Button(buttonsFrame, text="Change name", command=change_name, height=2, width=10)
change_name_button.grid(row=1, column=1)

make_directory_button = Button(buttonsFrame, text="Make directory", command=make_directory, height=2, width=10)
make_directory_button.grid(row=1, column=2)




loginWindow.mainloop()