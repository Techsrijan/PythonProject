from tkinter import *

bob=Tk()
def msg():
    print("button is clicked")
frame=Frame(bob,width=400,height=400)
user = Label(frame,text="Enter User Name")
user.grid(row=0)
pas = Label(frame,text="Enter User Password")
pas.grid(row=1,column=0)
#user.pack()
#pas.pack()

entry=Entry(frame)
entry.grid(row=0,column=1)
entry1=Entry(frame)
entry1.grid(row=1,column=1)
button1=Button(frame,text="Login and Save",bg="red",fg="white",command=msg)
button1.grid(columnspan=2)
#entry.pack()
#entry1.pack()
frame.pack()
bob.geometry("300x200+300+200")
bob.mainloop()