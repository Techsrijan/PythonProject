from tkinter import *

def Delete():
    checked_item = l.curselection()
    for item in checked_item:
        print(l.delete(item))
def Clickme():
    checked_item=l.curselection()
    print(checked_item)
    for item in checked_item:
        print(l.get(item))

bob = Tk()
l= Listbox(bob,width=50,selectmode=EXTENDED)
l.insert(1,"apple")
l.insert(2,"orange")
l.insert(3,"orange")
l.insert(4,"orange")
l.pack()
b=Button(bob,text="Display",command=Clickme)
b.pack()
b1=Button(bob,text="Delete",command=Delete)
b1.pack()
bob.geometry("500x500+300+200")
bob.mainloop()