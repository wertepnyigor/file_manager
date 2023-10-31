import os
from tkinter import *
from tkinter import messagebox
from GUI_handling import *
from files_handling import *


def logging():
    correct_login = "igor"
    correct_pass = "dupa"
    user_login = loginEntry.get()
    user_password = passwordEntry.get()

    if len(user_login) > 0 and len(user_password) > 0:
        if user_login == correct_login and correct_pass == user_password:
            new_window = Toplevel()
            new_window.title("File Manager")
            new_window.mainloop()
        elif user_login != correct_login:
            messagebox.showerror(title="Your login is incorrect or not known")
        elif user_password != correct_pass:
            messagebox.showerror(title="Your password is incorrect or not known")

        # if loginButton["state"] == NORMAL:
        #     loginButton["state"] = DISABLED
        # else:
        #     loginButton["state"] = NORMAL

    elif len(user_login) == 0 and len(user_password) == 0:
        messagebox.showerror(title="Logging error", message="Login and/or password blank, please type proper value")

    else:
        messagebox.showerror(title="Unknown error")


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

loginFrame = Frame(loginWindow)
loginFrame.pack()

loginEntry = Entry(loginFrame, font=("Arial", 30, "bold"), background='black', foreground='white')
loginEntry.grid(row=0, column=1)
loginEntry.focus_set()

passwordEntry = Entry(loginFrame, font=("Arial", 30, "bold"), background='black', foreground='white', show="*")
passwordEntry.grid(row=1, column=1)

loginLabel = Label(loginFrame, text="Login: ")
loginLabel.grid(row=0, column=0)

passwordLabel = Label(loginFrame, text="Password: ")
passwordLabel.grid(row=1, column=0)

loginButton = Button(loginWindow, text="Login", bd=5, padx=5, pady=5, command=logging)
loginButton.pack()

loginWindow.mainloop()