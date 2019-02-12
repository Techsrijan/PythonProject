from tkinter import *

bob=Tk()
def msg1(event):
    print("Left button is clicked")

def msg2(event):
    print("Middle button is clicked")

def msg3(event):
    print("right button is clicked")
frame=Frame(bob)
#user = Label(frame,text="Enter User Name")
button1=Button(frame,text="Left Click",bg="red",fg="white")
button1.bind("<Button-1>",msg1)
button2=Button(frame,text="Middle click")
button2.bind("<Button-2>",msg2)
button3=Button(frame,text="Right Click")
button3.bind("<Button-3>",msg3)
#user.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
frame.pack()

bottomframe =Frame(bob)
entry=Entry(bottomframe)
button4=Button(bottomframe,text="Button4",bg="yellow")

entry.pack()
button4.pack(fill=X)
bottomframe.pack(side=BOTTOM)
bob.geometry("300x200+300+200")
bob.mainloop()