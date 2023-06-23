from turtle import *
speed=('fastest')
size=10
angle=61
color=['red','yellow','blue','green','black','orange']
while True:
    pencolor(color[size%6])
    fd(size)
    lt(angle)
    size+=1
    