from tkinter import *
bob=Tk()
def Clickme():
    s=en.get()
    print(s)

en=Entry(bob)
en.pack()
b=Button(bob,text="Message Box",command=Clickme)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()