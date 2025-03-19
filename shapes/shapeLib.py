import turtle
import math

def drawQuadrilateral(turt,x1,y1,x2,y2,x3,y3,x4,y4):
    turt.up()
    turt.setpos(x1,y1)
    turt.down()
    turt.goto(x2,y2)
    turt.goto(x3,y3)
    turt.goto(x4,y4)
    turt.goto(x1,y1)

def drawTriangle(turt,x1,y1,x2,y2,x3,y3):
    turt.up()
    turt.setpos(x1,y1)
    turt.down()
    turt.goto(x2,y2)
    turt.goto(x3,y3)
    turt.goto(x1,y1)

def drawCircle(turt, radius, x, y):
    turt.up()
    turt.setpos(x,(y+radius))
    turt.down()
    for i in range(360):
        circumference=2*radius*math.pi
        turt.forward(circumference/360)
        turt.right(1)



