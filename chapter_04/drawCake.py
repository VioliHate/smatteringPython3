"""Scrivete un insieme di funzioni, generali in modo appropriato, che disegni delle
forme a torta come in Figura 4.2."""

import math
import turtle


def draw_cake(t, n, r):
    """Disegna una torta fetta per fetta e si sposta verso destra.

    t: Turtle
    n: numero dei segmenti
    r: lunghezza del raggio
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()


def isosceles(t, r, angle):
    """Disegna un triangolo isoscele.

    t: Turtle
    r: lunghezza del raggio (i due lati coincidenti del triangolo)
    angle: angolatura in gradi
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

# draw cake with various number of sides
size = 60
draw_cake(bob, 5, size)
draw_cake(bob, 6, size)
draw_cake(bob, 7, size)
draw_cake(bob, 8, size)

bob.hideturtle()
turtle.mainloop()
