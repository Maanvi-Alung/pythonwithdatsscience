

from turtle import *

speed('fast')
distance=100
side=6
for i in range(side):
    pencolor('red')
    fd(distance)
    rt(360/side)
    circle(distance/2)
    for i in range(side):
        fd(distance/2)
        rt(360/side)
        dot(10)
        write(i)
hideturtle()
mainloop()
