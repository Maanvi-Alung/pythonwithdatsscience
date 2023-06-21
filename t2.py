
from turtle import *

speed('slow')
distance=100
side=6
fillcolor('cyan')   
begin_fill()

for i in range(side):
    pencolor('red')
    fd(distance)
    rt(120)
    bk(100)
    lt(60)
end_fill()    
hideturtle()
mainloop()
