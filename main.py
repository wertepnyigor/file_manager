import os
from tkinter import *
from GUI_handling import *

def new_window():

    new_window = Toplevel()
    # loginWindow.destroy()

    new_window.title("Login passed")
    new_window.geometry("1000x600")
    new_window.config(background="black")

    passed_Label = Label(new_window, text="PASSED", relief=SUNKEN)
    passed_Label.pack()

    new_window.mainloop()


loginWindow = Tk()
loginWindow.geometry("1000x600")
loginWindow.title("File Manager")
loginWindow.config(background="black")

welcomeLable = Label(loginWindow, text="Welcome in File Manager!", font=("Arial", 30, "bold"),
                     foreground='white', background='black', relief=RAISED, bd=10, padx=40, pady=40,
                     compound='top')
welcomeLable.pack()

loginFrame = Frame(loginWindow)
loginFrame.pack()

loginEntry = Entry(loginFrame, font=("Arial", 30, "bold"), background='black', foreground='white')
loginEntry.grid(row=0, column=1)

passwordEntry = Entry(loginFrame, font=("Arial", 30, "bold"), background='black',foreground='white', show="*")
passwordEntry.grid(row=1, column=1)

loginLabel = Label(loginFrame, text="Login: ")
loginLabel.grid(row=0, column=0)

passwordLabel = Label(loginFrame, text="Password: ")
passwordLabel.grid(row=1, column=0)

loginButton = Button(loginWindow, text="Login", bd=5, padx=5, pady=5, command=new_window)
loginButton.pack()

loginWindow.mainloop()