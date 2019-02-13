from tkinter import *

bob=Tk()
canvas = Canvas(bob,width=500,height=500,bg="yellow")
canvas.pack()
line = canvas.create_line(0,0,300,300)
line1 = canvas.create_line(0,150,300,150,fill="red")
rect = canvas.create_rectangle(100,100,200,200,fill="blue")
cir = canvas.create_oval(100,100,200,200,fill="red")
#rect1 = canvas.create_rectangle(100,100,300,250,fill="white")
#cir2 = canvas.create_oval(100,100,300,250,fill="red")
arc = canvas.create_arc(100,100,200,200,extent=120,fill="yellow")
point=[250,110,480,200,280,280,250,110]
poly= canvas.create_polygon(point,fill="white",outline="red",width=5)
bob.geometry("800x800+300+200")
bob.mainloop()