import turtle
ht=turtle.Turtle()

def drawHeart(branchLength, angle, level):
    if level == 0:
        return
    ht.forward(branchLength)
    ht.left(angle)
    drawHeart(branchLength*.9,angle, level -1)
    ht.right(2*angle)
    drawHeart(branchLength*.9,angle, level -1)
    ht.left(angle)
    ht.backward(branchLength)
ht.up()
ht.pencolor("red")
ht.speed(0)
ht.setpos(0,-200)
ht.down()
ht.left(90)
drawHeart(100, 25, 10)
ht.pencolor("black")
ht.write("Happy birthday")
turtle.done()
