from turtle import *
speed(100)
up()
right(100)
forward(540)
left(100)
down()
def f(x):
    forward(x)
    left(20)
    if x>1:
        f(x-1)
f(200)
hideturtle()
exitonclick()