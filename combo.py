from tkinter import *
from tkinter.ttk import Combobox

def Clickme():
    value=l.get()
    print(value)

bob = Tk()
li=["Gkp","Ndls","lko","1","4","666"]
l = Combobox(bob,value=li)
l.set("select your city")
l.pack()


l.pack()
b=Button(bob,text="Display",command=Clickme)
b.pack()

bob.geometry("500x500+300+200")
bob.mainloop()