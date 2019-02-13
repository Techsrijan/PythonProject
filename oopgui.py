from tkinter import *

class Myform:
    def __init__(self,form):
        self.printButton=Button(form,text="Message Box",command=self.msg)
        self.printButton.pack(side=LEFT)
        self.quitbutton=Button(form,text="Exit",command=quit)
        self.quitbutton.pack(side=LEFT)
    def msg(self):
        print("Gui foorm Created")



bob=Tk()
test= Myform(bob)
bob.geometry("300x200+300+200")
bob.mainloop()