""" Le lettere dell’alfabeto possono essere costruite con un moderato
    numero di elementi di base, come linee orizzontali e verticali e alcune curve.
    Progettate un alfabeto che possa essere disegnato con un numero minimo di elementi di base
    e poi scrivete delle funzioni che disegnino le lettere
"""

import turtle
import math

# LEVEL 0 PRIMITIVES 
# fd, bk, lt, rt, pu, pd

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()


# LEVEL 1 PRIMITIVES are simple combinations of Level 0 primitives.
# They have no pre- or post-conditions.

def fdlt(t, n, angle=90):
    """forward and left"""
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    """forward and back, ending at the original position"""
    fd(t, n)
    bk(t, n)

def skip(t, n):
    """lift the pen and move"""
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    """Makes a vertical line and leave the turtle at the top, facing right"""
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    """move the turtle vertically and leave it at the top, facing right"""
    lt(t)
    skip(t, n)
    rt(t)


# LEVEL 2 PRIMITIVES use primitives from Levels 0 and 1
# to draw posts (vertical elements) and beams (horizontal elements)
# Level 2 primitives ALWAYS return the turtle to the original
# location and direction.

def post(t, n):
    """Makes a vertical line and return to the original position"""
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Makes a horizontal line at the given height and return."""
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def hangman(t, n, height):
    """Makes a vertical line to the given height and a horizontal line
    at the given height and then return.
    This is efficient to implement, and turns out to be useful, but
    it's not so semantically clean."""
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t, x, y):
    """Makes a diagonal line to the given x, y offsets and return"""
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """Makes a bump with radius n at height*n 
    """
    stump(t, n*height)
    drawArch(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

    
def drawCircle(t,r):
    """ draw a circle
    """
    drawArch(t, r, 360)

def drawArch(t, r, angle):
    """ draw a arch
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    
def drawPolygon(t,lenght,n):
    angle=360/n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)



"""
The letter-drawing functions all have the precondition
that the turtle is in the lower-left corner of the letter,
and postcondition that the turtle is in the lower-right
corner, facing in the direction it started in.

They all take a turtle as the first argument and a size (n)
as the second.  Most letters are (n) units wide and (2n) units
high.

"""

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_j(t, n):
    beam(t, n, 2)
    drawArch(t, n/2, 90)
    fd(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    fd(t, n)

def draw_n(t, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_m(t, n):
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_o(t, n):
    skip(t, n)
    drawCircle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    fd(t, n/2)
    drawArch(t, n/2, 180)
    drawArch(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, 2*n)
    fd(t, n)
    post(t, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def draw_(t, n):
    # draw a space
    skip(t, n)

if __name__ == '__main__':

    # create and position the turtle
    size = 20
    pippo = turtle.Turtle()

    pippo.pu()
    pippo.bk(180)
    pippo.pd()

    for f in [draw_d, draw_o, draw_m, draw_e, draw_n, draw_i, draw_c, draw_o]:
        f(pippo, size)
        skip(pippo, size)

    turtle.mainloop()
