from tkinter import *

def Clickme():
    s1=s.get()
    print(s1)

bob=Tk()
s=IntVar()
r1=Radiobutton(bob,text="Male",value=1,variable=s)
r2=Radiobutton(bob,text="Female",value=2,variable=s)
r1.pack()
r2.pack()
b=Button(bob,text="Message Box",command=Clickme)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()