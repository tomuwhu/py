from turtle import *
speed("fastest")
color("red","blue")
def k(x):
    for i in range(6):
        forward(x)
        left(60)
    left(10)
    if x>8:
        k(34*x/35)
begin_fill()
k(250)
end_fill()
mainloop()