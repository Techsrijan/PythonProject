from tkinter import *
import pymysql

bob=Tk()
def Clickme():
    con = pymysql.connect(host="localhost", user="root", db="pythongui")
    mycursor = con.cursor()
    a=5
    s=en.get()
    #mycursor.execute("INSERT INTO detail VALUES ( %s,%s)", (a,s))
    mycursor.execute("INSERT INTO detail(name) VALUES ( %s)", (s))
    print("data inserted successfully")
    con.commit()
    # to close the connection
    con.close()
    print(s)

en=Entry(bob)
en.pack()
b=Button(bob,text="Message Box",command=Clickme)
b.pack()
bob.geometry("300x200+300+200")
bob.mainloop()