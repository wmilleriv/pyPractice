import turtle


t=turtle.Turtle()

def goRight():
    t.setheading(0)
    t.forward(10)

while(True):
    x=input()
    if(x=='d'):
        goRight()
turtle.mainloop()

