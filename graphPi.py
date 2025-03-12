import turtle

screen=turtle.Screen()
scWidth=screen.window_width()
scHeight=screen.window_height()
plane=turtle.Turtle()

def drawXLines():
    for i in range(6):
        plane.up()
        plane.setpos(0, i*2)
        plane.down()
        plane.forward(100000)

def drawYLines():
    plane.setheading(90)
    for i in range (100):
        plane.up()
        plane.setpos(i*1000, 0)
        plane.down()
        plane.forward(10)

screen.screensize(800,800)
turtle.setworldcoordinates(0,0,100000,10)
plane.speed(100)
plane.color("green")
drawXLines()
drawYLines()
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
