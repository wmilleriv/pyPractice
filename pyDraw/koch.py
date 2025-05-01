import turtle

t=turtle.Turtle()

def koch(length, level):
    if level==0:
        t.forward(length)
        return
    koch(length/3, level-1)
    t.left(60)
    koch(length/3, level-1)
    t.right(120)
    koch(length/3, level-1)
    t.left(60)
    koch(length/3, level-1)

t.pencolor("blue")
t.speed(0)
t.up()
t.setpos(-600,0)
t.down()
for i in range(3):
    koch(300.0,4)
    t.left(120)
turtle.done()
