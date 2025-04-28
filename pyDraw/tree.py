import turtle

def drawTree(branchLength, angle, level, thickness):
    if level==0:
        turtle.dot(10,"pink")
        return
    if level > 5:
        turtle.color("brown")
    else:
        turtle.color("green")
    
    turtle.pensize(thickness)
    turtle.left(angle)

