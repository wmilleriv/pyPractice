import turtle
t = turtle.Turtle()

def drawHeart(size):
    t.fillcolor("red")
    t.begin_fill()
    t.left(50)
    t.fd(120)
    t.circle(45,200)
    t.lt(221)
    t.circle(45,200)
    t.fd(130)
    t.end_fill()
def drawAi(size):
    t.left(190)
    t.fd(size)
    
t.pencolor("red")
t.speed(80)
t.down()
drawAi(120)
turtle.done()
