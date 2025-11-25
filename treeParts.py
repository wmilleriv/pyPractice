import turtle
import math

t=turtle.Turtle()

def drawTrunk(t, width, height,color):
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.fillcolor(color)

def drawIsoTriangle(t, width, height, color):
    hypotenuse=((((0.5*width)**2)+(height**2))**(1/2))
    baseAngle=(math.asin(height/hypotenuse)*(180/math.pi))
    topAngle=90-baseAngle
    t.fd(width)
    t.left(90-baseAngle+90)
    t.fd(hypotenuse)
    t.left((90+baseAngle)-topAngle)
    t.fd(hypotenuse)
   # t.left(180-baseAngle)
    #t.fd(


drawIsoTriangle(t,20,100,"brown")
turtle.done()
