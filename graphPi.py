import turtle

screen=turtle.Screen()
scWidth=screen.window_width()
scHeight=screen.window_height()
plane=turtle.Turtle()

def drawLines(lineCount):
    loopCount=int(lineCount/2)+1#two lines per loop
    for i in range(loopCount):
        plane.down()
        plane.forward(800)
        plane.right(90)
        plane.forward(800/(lineCount))
        plane.right(90)
        plane.forward(800)
        plane.left(90)
        plane.forward(800/(lineCount))
        plane.left(90)
        
        

screen.screensize(800,800)
turtle.setworldcoordinates(0,0,800,800)
plane.speed(100)
plane.left(90)
plane.color("green")

drawLines(100)
plane.up()
plane.setpos(800,0)
plane.left(90)
drawLines(100)
turtle.mainloop()


