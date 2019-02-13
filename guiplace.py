from tkinter import *

bob=Tk()
def msg():
    print("button is clicked")
frame=Frame(bob,width=400,height=400)
user = Label(frame,text="Enter User Name")
user.place(x=10,y=10)
pas = Label(frame,text="Enter User Password")
pas.place(x=10,y=40)
#user.pack()
#pas.pack()


#entry.pack()
#entry1.pack()
frame.pack()
bob.geometry("300x200+300+200")
bob.mainloop()