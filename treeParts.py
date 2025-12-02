import turtle
import math

t=turtle.Turtle()

def drawTrunk(t, width, height, color="brown"):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.end_fill()

def drawIsoTriangle(t, width, height, color="green"):
    hypotenuse=((((0.5*width)**2)+(height**2))**(1/2))
    baseAngle=(math.asin(height/hypotenuse)*(180/math.pi))
    topAngle=90-baseAngle
    t.fillcolor(color)
    t.begin_fill()
    t.fd(width)
    t.left(90-baseAngle+90)
    t.fd(hypotenuse)
    t.left((90+baseAngle)-topAngle)
    t.fd(hypotenuse)
    t.end_fill()

def drawStar(t,span,color="yellow"):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.fd(span/3)
        t.left(72)
        t.fd(span/3)
        t.right(126)
    t.end_fill()

def drawCircle(t,diameter,color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(diameter/2)
    t.end_fill()
    

drawCircle(t,100,"red")
turtle.done()
