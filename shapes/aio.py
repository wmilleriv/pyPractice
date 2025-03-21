import turtle

def drawSquare(turt, width):
    turt.forward(width)
    turt.left(90)
    turt.forward(width)
    turt.left(90)
    turt.forward(width)
    turt.left(90)
    turt.forward(width)


def drawTriangle(turt,x1,y1,x2,y2,x3,y3):
    turt.setpos(x1,y1)
    turt.down()
    turt.goto(x2,y2)
    turt.goto(x3,y3)
    turt.goto(x1,y1)


t=turtle.Turtle()
t.fillcolor("blue")
t.begin_fill()
drawSquare(t,10)
t.end_fill()
