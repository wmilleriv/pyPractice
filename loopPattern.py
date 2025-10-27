import turtle as t

def draw(distance,angle):
    t.forward(distance)
    t.right(angle)

for i in range(0,100):
    for theta in range(0,180):
        draw(i,theta)
