from turtle import *

from random import randint
s = Screen()
a = Turtle()
a.speed(0)

s.bgcolor('black')

x = 1

while x < 400:

    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    s.colormode(255)

    a.pencolor(r,g,b)

    a.fd(50 + x)
    a.rt(90.911)


    x = x+1

done()