# loginFrame = Frame(loginWindow)
# loginFrame.pack()
#
# loginEntry = Entry(loginFrame, font=("Arial", 30, "bold"), background='black', foreground='white')
# loginEntry.grid(row=0, column=1)
# loginEntry.focus_set()
#
# passwordEntry = Entry(loginFrame, font=("Arial", 30, "bold"), background='black', foreground='white', show="*")
# passwordEntry.grid(row=1, column=1)
#
# loginLabel = Label(loginFrame, text="Login: ")
# loginLabel.grid(row=0, column=0)
#
# passwordLabel = Label(loginFrame, text="Password: ")
# passwordLabel.grid(row=1, column=0)
#
# loginButton = Button(loginWindow, text="Login", bd=5, padx=5, pady=5)
# loginButton.pack()

# def logging():
#     user_login = loginEntry.get()
#     user_password = passwordEntry.get()
#
#     if len(user_login) > 0 and len(user_password) > 0:
#
#         new_window = Toplevel()
#         new_window.title("File Manager")
#         new_window.config(background="black")
#         new_window_width = 1000
#         new_window_height = 500
#         new_screen_width = new_window.winfo_screenwidth()
#         new_screen_height = new_window.winfo_screenheight()
#
#         x1 = int((new_screen_width / 2) - (new_window_width / 2))
#         y1 = int((new_screen_height / 2) - (new_window_height / 2))
#
#         new_window.geometry("{}x{}+{}+{}".format(new_window_width, new_window_height, x1, y1))
#         new_window.mainloop()
#
#         if loginButton["state"] == NORMAL:
#             loginButton["state"] = DISABLED
#         else:
#             loginButton["state"] = NORMAL
#
#     elif len(user_login) == 0 and len(user_password) == 0:
#         messagebox.showerror(title="Logging error", message="Login and/or password blank, please type proper value")
#
#     else:
#         messagebox.showerror(title="Unknown error")