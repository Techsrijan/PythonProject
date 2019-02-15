from tkinter import *

def Clickme():
    s1=s.get()
    print(s1)

bob=Tk()
s=StringVar()
en=Entry(bob, textvariable= s)
s.set("Hello")
en.pack()
b=Button(bob,text="Message Box",command=Clickme)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()