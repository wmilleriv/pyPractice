import turtle

screen=turtle.Screen()
scWidth=screen.window_width()
scHeight=screen.window_height()
plane=turtle.Turtle()

def drawLines(lineCount):
    for i in range(lineCount):
        plane.down()
        plane.forward(800)
        plane.right(90)
        plane.forward(800/lineCount)
        plane.right(90)
        plane.forward(800)
        plane.left(90)
        plane.forward(800/lineCount)
        plane.left(90)
        
        

screen.screensize(800,800)
turtle.setworldcoordinates(0,0,800,800)
plane.speed(10)
plane.left(90)

drawLines(10)
plane.up()
plane.setpos(800,0)
plane.left(90)
drawLines(10)
turtle.mainloop()


