import shapeLib
import turtle

turt=turtle.Turtle()
turt.shape("turtle")
turt.speed(1000)
turt.fillcolor("red")
turt.begin_fill()
shapeLib.drawQuadrilateral(turt,-200,-250,-200,150,200,150,200,-250)
turt.end_fill()
turt.fillcolor("blue")
turt.begin_fill()
shapeLib.drawTriangle(turt,200,150,-200,150,0,250)
turt.end_fill()
turt.fillcolor("#8B4513")
turt.begin_fill()
shapeLib.drawQuadrilateral(turt,0,-250,0,-100,100,-100,100,-250)
turt.end_fill()
turt.fillcolor("yellow")
turt.begin_fill()

turt.end_fill()

turt.screen.mainloop()
