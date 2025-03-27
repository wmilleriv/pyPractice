import turtle
import shapes

t=turtle.Turtle()
x=-40
y=150
for i in range(4):
    x+=20
    shapes.drawSquare(t, ((x),y),20, "black","black")
x+=20
y-=20
shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
y-=20
shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
y-=20
shapes.drawSquare(t,(x,y),20,"black","black")
y-=20
shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
for i in range(4):
    y-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
for i in range(3):
    y-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
x-=20
y-=20
shapes.drawSquare(t,(x,y),20,"black","black")
x-=20
y+=40
for i in range(4):
    y-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
y-=20
for i in range(3):
    x-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
y+=20
for i in range(4):
    x-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
y-=20
for i in range(3):
    x-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
x-=20
for i in range(4):
    y+=20
    shapes.drawSquare(t,(x,y),20,"black","black")
x-=20
y-=20
shapes.drawSquare(t,(x,y),20,"black","black")
x-=20
for i in range(3):
    y+=20
    shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
for i in range(4):
    y+=20
    shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
y+=20
shapes.drawSquare(t,(x,y),20,"black","black")
y+=20
shapes.drawSquare(t,(x,y),20,"black","black")
y+=20
x+=20
shapes.drawSquare(t,(x,y),20,"black","black")
y+=20
x+=20
shapes.drawSquare(t,(x,y),20,"black","black")
x+=20
shapes.drawSquare(t,(x,y),20,"black","black")
x=-20
y=150
shapes.drawSquare(t,(x,y),"grey","grey")

turtle.done()
