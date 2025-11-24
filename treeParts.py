import turtle

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

drawTrunk(t,20,100,"brown")
