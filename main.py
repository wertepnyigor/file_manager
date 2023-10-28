import os
from tkinter import *


loginWindow = Tk()
loginWindow.geometry("1000x600")
loginWindow.title("File Manager")
loginWindow.config(background="black")

welcomeLable = Label(loginWindow, text="Welcome in File Manager!", font=("Arial", 30, "bold"),
                     foreground='white', background='black', relief=SUNKEN, bd=10, padx=40, pady=40,
                     compound='top')
welcomeLable.pack()


loginEntry = Entry(loginWindow, font=("Arial", 30, "bold"), background='black', foreground='white')
loginEntry.grid(row=0, column=1)

passwordEntry = Entry(loginWindow, font=("Arial", 30, "bold"), background='black',foreground='white', show="*")
passwordEntry.grid(row=1, column=1)

loginLabel = Label(loginWindow, text="Login: ")
loginLabel.grid(row=0, column=0)

passwordLabel = Label(loginWindow, text="Password: ")
passwordLabel.grid(row=1, column=0)

loginButton = Button(loginWindow, text="Login", bd=5, padx=5, pady=5)
loginButton.pack()

loginWindow.mainloop()