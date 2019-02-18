from tkinter import *

def Clickme():
    s1=i.get()
    print(s1)

bob = Tk()
i=StringVar()

c= Checkbutton(bob,text="Hindi",variable=i,offvalue="unchecked",onvalue="checked")
c.pack()
b=Button(bob,text="Message Box",command=Clickme)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()