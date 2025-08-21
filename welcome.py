import turtle
import os
import sys,time,random

typing_speed = 50 #wpm

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def draw_w(t):
    t.pendown()
    t.right(70)
    t.forward(150)
    t.left(130)
    t.forward(100)

    t.right(120)
    t.forward(100)
    t.left(130)
    t.forward(150)

def draw_e(t):
    t.right(90)
    t.forward(20)
    t.setheading(0)
    t.pendown()
    t.forward(60)
    t.backward(60)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.backward(60)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(60)

def draw_l(t):
    t.right(90)
    t.forward(20)
    t.pendown()
    t.forward(120)

    t.right(-90)
    t.forward(70)

def draw_c(t):
    t.forward(50)
    t.sety(40)
    t.pendown()
    t.right(180)
    t.circle(70,180)

def draw_o(t):
    t.forward(80)
    t.sety(-90)
    t.setheading(0)
    t.pendown()
    t.circle(60,None,60)

def draw_m(t):
    t.forward(50)
    t.sety(-90)
    t.pendown()
    t.left(70)
    t.forward(100)
    t.right(130)
    t.forward(60)

    t.left(120)
    t.forward(60)
    t.right(130)
    t.forward(100)

def space(t):
    t.penup()
    t.sety(50)
    t.setheading(0)
    t.forward(20)

while True:
    print()
    print()
    print()
    slow_type("                   Welcome to Mr. Miller's class")
    print(" --------------------------------------------------------------------------")
    slow_type("     Subjects include:")
    print()
    slow_type("         1) Technology - students will learn to use technology safely and effectively")
    slow_type("         2) Coding - students will learn to write computer programs (like this one)")
    slow_type("         3) Pre-Algebra - Students will begin their journey on an exciting branch of mathematics") 
    

    t=turtle.Turtle()
    t.screen.setup(width=1000, height=300, startx=300, starty=300) 
    t.pensize(10)
    t.penup()
    t.goto(-450, 50)
    t.pencolor("blue")
    draw_w(t)
    space(t)
    t.pencolor("red")
    draw_e(t)
    space(t)
    t.pencolor("yellow")
    draw_l(t)
    space(t)
    t.pencolor("purple")
    draw_c(t)
    space(t)
    t.pencolor("green")
    draw_o(t)
    space(t)
    t.pencolor("blue")
    draw_m(t)
    space(t)
    t.pencolor("red")
    draw_e(t)
    t.penup()
    t.goto(0,100)
    t.right(1800)
    t.screen.clear()

    os.system('clear') 
