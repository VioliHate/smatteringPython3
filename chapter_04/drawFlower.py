import turtle
import math

def arc(t, r, angle):
    arcLenght = 2 * math.pi * r * abs(angle) / 360
    n = int(arcLenght / 4) + 3
    stepLenght = arcLenght / n
    stepRadius = float(angle) / n
    t.lt(stepRadius/2)
    for i in range(n):
        t.fd(stepLenght)
        t.lt(stepRadius)
    t.rt(stepRadius/2)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)
        
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """
    Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()
move(bob, -200)
flower(bob, 10, 60, 60)
move(bob, 200)
flower(bob, 12, 40, 80)
move(bob, 200)
flower(bob, 20, 140, 20)

bob.hideturtle()



turtle.mainloop()


