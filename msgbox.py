from tkinter import *
from tkinter import messagebox

bob=Tk()
def msg():
    ans=messagebox.showinfo("Question Box","Do you want to close?")
    print(ans)
    if ans=="yes":
        print("thank you")
    else:
        bob.quit()


b=Button(bob,text="Message Box",command=msg)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()