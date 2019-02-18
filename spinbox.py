from tkinter import *
import cx_Freeze


def Clickme():
   print(spin1.get())


bob=Tk()
spin1 = Spinbox(bob,from_=1, to=12)
spin1.pack()
b=Button(bob,text="Get spin Box value",command=Clickme)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()