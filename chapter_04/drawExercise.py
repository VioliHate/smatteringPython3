#4.3
import turtle
import math
#.1
"""
Scrivete una funzione di nome quadrato che richieda un parametro di nome t, che è
una tartaruga. La funzione deve usare la tartaruga per disegnare un quadrato.
"""
def drawSquare(t):
    t.clear()
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
    t.reset()

"""
Scrivete una chiamata alla funzione quadrato che passi bob come argomento, ed
eseguite nuovamente il programma.
"""
bob =turtle.Turtle()
bob.reset()
drawSquare(bob)


#2
"""
Aggiungete a quadrato un nuovo parametro di nome lunghezza
"""
def drawSquare(t,lenght):
    t.clear()
    for i in range(4):
        bob.fd(lenght)
        bob.lt(90)
    t.reset()

    
drawSquare(bob,50)
drawSquare(bob,55)


#3
"""
Fate una copia di quadrato e cambiate il nome in poligono. Aggiungete un altro
parametro di nome n e modificate il corpo in modo che sia disegnato un poligono
regolare di n lati. Suggerimento: gli angoli esterni di un poligono regolare di n lati
misurano 360/n gradi.
"""

def drawPolygon(t,lenght,n):
    t.clear()
    angle=360/n
    for i in range(n):
        bob.fd(lenght)
        bob.lt(angle)
    t.reset()

drawPolygon(bob,40,8)


#4
"""
Scrivete una funzione di nome cerchio che prenda come parametri una tartaruga,
t, e un raggio, r, e che disegni un cerchio approssimato chiamando poligono con
un’appropriata lunghezza e numero di lati. Provate la funzione con diversi valori di r.

Suggerimento: pensate alla circonferenza del cerchio e accertatevi che lunghezza *
n = circonferenza.
"""

def drawCircle(t,r):
    circle= 2*r*math.pi
    n = circle/3 + 3
    lenght=circle/n
    drawPolygon(t,int(lenght),int(n))

drawCircle(bob,50)


#5
"""
Create una versione più generale della funzione cerchio, di nome arco, che richieda
un parametro aggiuntivo angolo, il quale determina la porzione di cerchio da disegnare.
angolo è espresso in gradi, quindi se angolo=360, arco deve disegnare un
cerchio completo.
"""

def drawArch(t, r, radius):
    archLenght = 2 * math.pi * r * abs(radius) / 360
    n = int(archLenght / 4) + 3
    stepLenght = archLenght / n
    stepRadius = radius / n
    t.lt(stepRadius/2)
    for i in range(n):
        t.fd(stepLenght)
        t.lt(stepRadius)
    t.rt(stepRadius/2)

drawArch(bob,50,360)




turtle.mainloop()
