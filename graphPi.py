import turtle

screen=turtle.Screen()
scWidth=screen.window_width()
scHeight=screen.window_height()
plane=turtle.Turtle()

def drawXLines():
    for i in range(4):
        plane.up()
        plane.setpos(0, i)
        plane.down()
        plane.forward(100000)

def drawYLines():
    plane.setheading(90)
    for i in range (100):
        plane.up()
        plane.setpos(i*1000, 0)
        plane.down()
        plane.forward(10)
def label():
    plane.down
    plane.setpos(99000, 3)
    plane.color("black")
    plane.write(3, font=("Verdana", 12, "bold"))

screen.screensize(800,800)
turtle.setworldcoordinates(0,2,100000,4)
plane.speed(100)
plane.color("green")
drawXLines()
drawYLines()
plane.up()
label()

k=1
s=0

for i in range(100000):
    if(i%2==0):
        s+=4/k
    else:
        s-=4/k

    k+=2

    plane.setpos(i*100,s)
    plane.color("blue")
    plane.dot()
    print(s)
turtle.mainloop()


