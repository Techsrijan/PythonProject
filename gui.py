from tkinter import *

test = Tk()
test.geometry("300x200+200+300")
UserName =Label(test,text="Enter User Name",bg="black",fg="white")
UserName.pack(side=LEFT)
entry=Entry(test,bg="black",fg="white")
entry.pack(side=LEFT)
btn=Button(test,text="Login")
btn.pack(side=LEFT)
test.mainloop()