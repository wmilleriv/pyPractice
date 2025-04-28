import turtle

trt=turtle.Turtle()

def drawTree(branchLength, angle, level, thickness):
    if level==0:
        trt.dot(10,"pink")
        return
    if level > 5:
        trt.color("brown")
    else:
        trt.color("green")
    
    trt.pensize(thickness)
    trt.left(angle)
    drawTree(branchLength*0.9, angle, level-1, thickness-1)
    trt.right(2*angle)
    drawTree(branchLength *0.9, angle, level-1, thickness-1)
    trt.left(angle)
    trt.backward(branchLength)

trt.up()
trt.speed(100)
trt.setpos(0,-250)
trt.color("brown")
trt.down()
trt.left(90)
drawTree(100,25,8,10)
turtle.done()
