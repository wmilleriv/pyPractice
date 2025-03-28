import turtle
import shapes

t=turtle.Turtle()
#t.speed(100)
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
    shapes.drawSquare(t,(x,y+20),20,"yellow","yellow")
y+=20
for i in range(4):
    x-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
y-=20
for i in range(3):
    x-=20
    shapes.drawSquare(t,(x,y),20,"black","black")
    shapes.drawSquare(t,(x,y+20),20,"yellow","yellow")
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
y=130
shapes.drawSquare(t,(x,y),80,"grey","grey")
y-=20
x-=40
shapes.drawSquare(t,(x,y),80,"grey","grey")
x+=80
shapes.drawSquare(t,(x,y),80,"grey","grey")
y-=60
x+=40
shapes.drawSquare(t,(x,y),80,"grey","grey")
x-=160
shapes.drawSquare(t,(x,y),80,"grey","grey")
y-=60
shapes.drawSquare(t,(x,y),60,"grey","grey")
x+=180
shapes.drawSquare(t,(x,y),60,"grey","grey")
x=-20
y=30
shapes.drawSquare(t,(x,y),80,"grey","grey")
y-=40
for i in range(4):    
    shapes.drawSquare(t,(x,y),20,"yellow","yellow")
    x+=20
x-=40
y-=20
shapes.drawSquare(t,(x,y),20,"yellow","yellow")
x-=20
shapes.drawSquare(t,(x,y),20,"yellow","yellow")
x-=40
y+=60
shapes.drawSquare(t,(x,y),40,"black","black")
x+=80
shapes.drawSquare(t,(x,y),40,"black","black")
shapes.drawSquare(t,(x,y),20,"white","white")
x-=80
shapes.drawSquare(t,(x,y),20,"white","white")
y-=60
shapes.drawSquare(t,(x,y),20,"grey","grey")
x+=100
shapes.drawSquare(t,(x,y),20,"grey","grey")
x+=40
y+=120
shapes.drawSquare(t,(x,y-20),20,"grey","grey")
shapes.drawSquare(t,(x,y),20,"grey","grey")
x-=180
shapes.drawSquare(t,(x,y-20),20,"grey","grey")
shapes.drawSquare(t,(x,y),20,"grey","grey")
y-=160
shapes.drawSquare(t,(x,y),20,"grey","grey")
x-=40
shapes.drawSquare(t,(x,y),20,"grey","grey")
y+=20
shapes.drawSquare(t,(x,y),20,"grey","grey")
y+=20
shapes.drawSquare(t,(x,y),20,"grey","grey")
x+=260
shapes.drawSquare(t,(x,y),20,"grey","grey")
y-=20
shapes.drawSquare(t,(x,y),20,"grey","grey")
y-=20
shapes.drawSquare(t,(x,y),20,"grey","grey")
x-=40
shapes.drawSquare(t,(x,y),20,"grey","grey")
turtle.done()

