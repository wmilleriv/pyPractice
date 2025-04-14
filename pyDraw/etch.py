import turtle


t=turtle.Turtle()
t.color="purple"


def goRight():
    t.setheading(0)
    t.forward(10)

def goUp():
    t.setheading(90)
    t.forward(10)

def goLeft():
    t.setheading(180)
    t.forward(10)

def goDown():
    t.setheading(270)
    t.forward(10)

while(True):
    x=input()
    if(x=='d'):
        goRight()
    elif(x=='w'):
        goUp()
    elif(x=='a'):
        goLeft()
    elif(x=='s'):
        goDown()

turtle.mainloop()

