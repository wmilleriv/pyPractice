import turtle
import treeParts

t=turtle.Turtle()
t.up()
t.setpos(-20,-50)
parts.drawTrunk(t,40, 60,"brown")
t.setpos(-100,-50)
t.setheading(0)
treeParts.drawIsoTriangle(t, 200, 100, "green")
t.setpos(-80,0)
t.setheading(0)
treeParts.drawIsoTriangle(t, 160, 100, "green")
t.setpos(-60,50)
t.setheading(0)
treeParts.drawIsoTriangle(t, 120, 100, "green")
t.setpos(-25,170)
t.setheading(0)
treeParts.drawStar(t, 50, 5, "yellow")

color=["red","blue","yellow","purple","pink","orange"]
for i in range(1,6):
    for j in range(0,i):
        y=140-(35*i)
        x=(((i-1)*-15)+(j*30))
        t.setpos(x,y)
        t.setheading(0)
        treeParts.drawCircle(t, 20, color[(i+j)%6])

turtle.done()
