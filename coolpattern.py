from turtle import *
s = Screen()
a = Turtle()
a.speed(0)
a.pencolor('white')
s.bgcolor('black')

x = 0
a.up()



a.rt(45)
a.fd(90)
a.rt(135)

a.down()
while x < 120:
    a.fd(200)
    a.rt(61)
    a.fd(200)
    a.rt(61)
    a.fd(200)
    a.rt(61)
    a.fd(200)
    a.rt(61)
    a.fd(200)
    a.rt(61)
    a.fd(200)
    a.rt(61)

    a.rt(11.1111)
    x = x+1

done()
