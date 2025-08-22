import turtle as t
from random import random

t.speed(10)
t.goto(0,0)
t.clear()
for i in range(100):
    steps=int(random()*1000)
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(random()*100)
        t.right(60)

t.screen.mainloop()
