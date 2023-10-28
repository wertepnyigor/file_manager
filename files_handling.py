
#This file will be responsible for actions with files. Different functions of module os will help to create,
#open, close etc. files between locations. In text files it will be also possible to open file in chosen
#program (Word, Pages etc." and makes changes.


from tkinter import *

# button - you clik it, then it does stuff

count = 0


def click():
    global count
    count += 1
    print(f"You clicked the button {count}times. ")


window = Tk()

# photo = PhotoImage(file=" ") # name of file or path to file OR image name if we past it in

button = Button(window,
                text="Click it!",
                command=click,
                font=("Comic Sans", 40),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                # image=photo,
                # compound= "bottom",

                )
button.pack()

window.mainloop()