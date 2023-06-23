
from turtle import *

speed('slow')
side=6
fillcolor('cyan')   
begin_fill()

for i in range(side):
    pencolor('red')
    fd(100)
    rt(120)
    bk(100)
    lt(60)
end_fill()    
hideturtle()
mainloop()
