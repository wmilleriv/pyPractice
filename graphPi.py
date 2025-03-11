import turtle

screen=turtle.Screen()
scWidth=screen.window_width()
scHeight=screen.window_height()
plane=turtle.Turtle()

def drawYLines():
    for i in range(6):
        plane.down()
        plane.forward(100000)
        plane.left(90)
        plane.forward(2)
        plane.left(90)
        plane.forward(100000)
        plane.right(90)
        plane.forward(2)
        plane.right(90)

def drawXLines():
    for i in range (10):
        plane.down()
        plane.forward(100)
        plane.left(90)
        plane.forward(2)
        plane.left(90)
        plane.forward(100)
        plane.right(90)
        plane.forward(2)
        plane.right(90)

screen.screensize(800,800)
turtle.setworldcoordinates(0,0,100000,10)
plane.speed(100)
plane.color("green")
drawYLines()
plane.up()
plane.setpos(800,0)
plane.setheading(0)
drawXLines()
turtle.mainloop()

k=1
s=0

for i in range(1000000):
    if(i%2==0):
        s+=4/k
    else:
        s-=4/k
        plane.setpos(i*10,s)
        plane.down()
