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
frame=Frame(bob)
frame.pack()
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)
l = Listbox(frame,width=50,selectmode=EXTENDED,yscrollcommand=scroll.set)
for i in range(1,100):
    l.insert(END,"Element"+str(i))
l.pack(side=LEFT)
scroll.config(command=l.yview)
scroll.pack(side=RIGHT,fill=Y)
b=Button(bob,text="Display",command=Clickme)
b.pack()
b1=Button(bob,text="Delete",command=Delete)
b1.pack()
bob.geometry("500x500+300+200")
bob.mainloop()