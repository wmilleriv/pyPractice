import turtle
import os
import sys,time,random

typing_speed = 500 #wpm

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
    t.forward(10)
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
    t.pendown()
    t.right(90)
    t.forward(150)

    t.right(-90)
    t.forward(70)

def draw_c(t):
    t.pendown()
    t.right(180)
    t.circle(50,180)

def draw_o(t):
    t.pendown()
    t.circle(50,None,50)

def draw_m(t):
    t.pendown()
    t.right(65)
    t.forward(150)
    t.left(130)
    t.forward(100)

    t.right(120)
    t.forward(100)
    t.left(130)
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
    t.screen.setup(width=800, height=300, startx=500, starty=300) 
    t.pensize(10)
    t.penup()
    t.goto(-350, 50)
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
    t.screen.clear()

    os.system('clear') 
