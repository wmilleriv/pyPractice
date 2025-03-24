import turtle


def drawQuadrilateral(turt,x1,y1,x2,y2,x3,y3,x4,y4):
    turt.up()
    turt.setpos(x1,y1)
    turt.down()
    turt.goto(x2,y2)
    turt.goto(x3,y3)
    turt.goto(x4,y4)
    turt.goto(x1,y1)

def drawTriangle(turt,x1,y1,x2,y2,x3,y3):
    turt.up()
    turt.setpos(x1,y1)
    turt.down()
    turt.goto(x2,y2)
    turt.goto(x3,y3)
    turt.goto(x1,y1)
    
class Square()
    def __init__(self,length, x, y):

