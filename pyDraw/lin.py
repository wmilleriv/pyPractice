import turtle
t = turtle.Turtle()

def drawHeart():
    t.fillcolor("red")
    t.begin_fill()
    t.left(50)
    t.fd(120)
    t.circle(45,200)
    t.lt(221)
    t.circle(45,200)
    t.fd(130)
    t.end_fill()

t.pencolor("red")
t.speed(80)
t.down()
drawHeart()
turtle.done()
