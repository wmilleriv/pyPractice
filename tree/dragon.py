import treeParts
import turtle

t=turtle.Turtle()
t.up()

t.setpos(-100,0)
treeParts.drawTrunk(t,200,100,"green")
t.setheading(0)
t.setpos(100,20)
treeParts.drawTrunk(t,75,50,"green")
t.setpos(-90,-20)
t.setheading(225)
treeParts.drawTrunk(t,100,20,"green")

treeParts.drawTrunk(t,100,20,"green")
treeParts.drawTrunk(t,100,20,"green")
treeParts.drawTrunk(t,100,20,"green")
treeParts.drawTrunk(t,100,20,"green")
treeParts.drawTrunk(t,100,20,"green")
treeParts.drawTrunk(t,100,20,"green")






turtle.done()
