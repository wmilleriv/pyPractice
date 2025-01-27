import turtle as t
from random import random

t.speed(10)
t.goto(-500.00,50.00)
t.clear()
for i in range(100):
    steps=int(random()*1000)
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(1000)
        t.right(175)

t.screen.mainloop()
