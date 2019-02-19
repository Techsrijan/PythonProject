from tkinter import *
from tkinter import filedialog


def openfile():
    f=filedialog.askopenfile(initialdir="/",title="Select file",filetypes=(("text file","*.txt"),("all files","*.*")))
    for value in f:
        print(value)

bob = Tk()

b=Button(bob,text="Open File",command=openfile)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()