from tkinter import *


def Clickme():
   print(spin1.get())
   print(s.get())


bob=Tk()
frame= LabelFrame(bob,text="Label frame",padx=15,pady=15)

spin1 = Spinbox(frame,from_=1, to=12)
spin1.pack()

s= Scale(frame,from_=0,to=100,orient=HORIZONTAL,length=200,width=10,sliderlength=50)
s.set(10)
s.pack()
b=Button(frame,text="Get spin Box value",command=Clickme)
b.pack()
frame.pack()
bob.geometry("300x200+300+200")
bob.mainloop()