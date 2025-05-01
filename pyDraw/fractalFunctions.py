import turtle
t=turtle.Turtle()
def terDragon(length,angle, iteration):
    if(iteration==0):
        t.fd(length)
        return
    terDragon(length/3,angle,iteration-1)
    t.left(angle)
    terDragon(length/3,angle,iteration-1)
    t.right(angle)
    terDragon(length/3,angle,iteration-1)


t.speed(0)
t.pencolor("red")
terDragon(30000,120,5)
turtle.done()
