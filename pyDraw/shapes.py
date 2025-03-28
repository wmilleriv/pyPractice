#import turtle

#parameters: turtle, top left corner tuple, sideLength,  border color, fill color
def drawSquare(trt, tlCorner, length, border="#000000", fill="#FFFFFF"):
    trt.up()
    trt.pencolor(border)
    trt.fillcolor(fill)
    trt.setpos(tlCorner[0],tlCorner[1])
    trt.down()
    trt.begin_fill()
    for i in range(4):
        trt.forward(length)
        trt.right(90)
    trt.end_fill()

#parameters: turtle, points as tuples, borde color, fill color
def drawTriangle(trt, p1,p2,p3, border="#000000", fill="#FFFFFF"):
    trt.up()
    trt.pencolor(border)
    trt.fillColor(fill)
    trt.setpos(p1[0],p1[1])
    trt.down()
    trt.begin_fill()
    trt.goto(p2[0],p2[1])
    trt.goto(p3[0],p3[1])
    trt.goto(p1[0],p1[1])
    trt.end_fill()
