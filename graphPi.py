import turtle

screen=turtle.Screen()
scWidth=screen.window_width()
scHeight=screen.window_height()
plane=turtle.Turtle()

def drawVerticalLines(lineCount):
    plane.setpos(0,0)
    plane.down()
    for i in range(int(lineCount/2)):
        plane.forward(800)
        plane.right(90)
        plane.forward(scWidth/lineCount)
        plane.right(90)
        plane.forward(scHeight)
        plane.right(90)
        plane.forward(scWidth/lineCount)
        


screen.screensize(800,800)
turtle.setworldcoordinates(0,0,800,800)
plane.speed(100)
plane.left(90)

drawVerticalLines(50)

turtle.mainloop()
