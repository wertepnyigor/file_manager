import os
from tkinter import *
from tkinter import messagebox
from GUI_handling import *
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


loginWindow.mainloop()