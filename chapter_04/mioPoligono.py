import turtle
bob = turtle.Turtle()
print (bob)


#draw a square
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

#draw with for
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()

