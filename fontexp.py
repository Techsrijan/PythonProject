from tkinter import *
from tkinter import font
bob = Tk()
fonts=list(font.families())
for item in fonts:
    print(item)
UserName =Label(bob,text="Enter User Name",font=("Comic Sans Ms",20,"bold"))
UserName.pack()
test=Text(bob,width=50,height=30,padx=10,pady=10,bd=15,selectbackground="red")
test.pack()
bob.geometry("500x500+300+200")
bob.mainloop()