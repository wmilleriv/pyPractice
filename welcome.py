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
    t.pensize(10)
    t.right(65)
    t.forward(150)
    t.left(130)
    t.forward(100)

    t.right(120)
    t.forward(100)
    t.left(130)
    t.forward(100)

def draw_e(t):
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

def draw_l():
    t.pendown()
    t.right(90)
    t.forward(150)

    t.right(-90)
    t.forward(70)

    #draw straight line
    t.pendown()
    t.pensize(10)
    t.right(180)
    t.circle(50,180)

def draw_o(t):
    t.pendown()
    t.pensize(10)
    t.circle(100,None,100)

def draw_m(t):
    t.pendown()
    t.pensize(10)

    t.right(90)
    t.forward(150)

    t.goto(-30,50)
    t.goto(20,-20)
    t.goto(65,50)
    t.goto(65,-100)

while True:
    slow_type("                   Welcome to Mr. Miller's class")
    print(" --------------------------------------------------------------------------")
    slow_type("     Subjects include:")
    print()
    slow_type("         1) Technology - students will learn to use technology safely and effectively")
    slow_type("         2) Coding - students will learn to write computer programs (like this one)")
    slow_type("         3) Pre-Algebra - Students will begin their journey on an exciting branch of mathematics") 
    os.system('clear') 
 
    

    #t=turtle.Turtle()
    #t.penup()
    #t.goto(-300, 50)
    #draw_w(t)
    #t.penup()
    #draw_e(t)
    #draw_l(t)
    #draw_c(t)
    #draw_o(t)
    #draw_m(t)
    #draw_e(t)
