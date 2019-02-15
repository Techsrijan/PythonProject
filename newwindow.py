from tkinter import *

def newwindow():
    root=Toplevel()
    root.title("child window")
    btn=Button(root,text="close",command=root.destroy )
    btn.pack()
    root.geometry("300x200+300+200")
    root.mainloop()


bob=Tk()
bob.title("Registration form")
b=Button(bob,text="Message Box",command=newwindow)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()