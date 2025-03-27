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


