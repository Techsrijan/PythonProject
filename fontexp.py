from tkinter import *
from tkinter import font


def Clickme():
    value=test.get(1.0,END)
    print(value)

def clear():
    test.delete(1.0,END)

def dis():
    result=test.selection_get()
    print(result)


def search():
    result = test.selection_get()
    pos=test.search(result,1.0,stopindex=END)
    print(pos)


bob = Tk()
fonts=list(font.families())
for item in fonts:
    print(item)
UserName =Label(bob,text="Enter User Name",font=("Comic Sans Ms",20,"bold"))
UserName.pack()
test=Text(bob,width=20,height=10,wrap=WORD,padx=10,pady=10,bd=15,selectbackground="red")
test.insert(INSERT,"Hello")
test.pack()
b=Button(bob,text="Display",command=Clickme)
b.pack()

b1=Button(bob,text="Clear", command=clear)
b1.pack()

b2=Button(bob,text="Selcted display", command=dis)
b2.pack()

b3=Button(bob,text="Search", command=search)
b3.pack()
bob.geometry("500x500+300+200")
bob.mainloop()