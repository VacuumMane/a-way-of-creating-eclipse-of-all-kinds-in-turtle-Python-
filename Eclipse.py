import turtle as t
from math import *

def flyto(x,y): #抬笔到某个点
    t.penup()
    t.goto(x,y)
    t.pendown()

def eclipse(x,y,a,b,angle1,angle2,angle3): #原点，半径，起画相对角度，斜度，弧度
    step=360 #分割份数
    per=angle3/step
    x1=a*cos(radians(angle1))
    y1=b*sin(radians(angle1))
    flyto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))
    for i in range(1,step+1):
        x1=a*cos(radians(angle1+i*per))
        y1=b*sin(radians(angle1+i*per))
        t.goto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))

def filleclipse(function,x,y,a,b,angle1,angle2,angle3,color1,color2): #上色的椭圆
    t.colormode(255)
    t.pencolor(color1)
    t.fillcolor(color2)
    t.begin_fill()
    function(x,y,a,b,angle1,angle2,angle3)
    t.end_fill()


filleclipse(eclipse,20,40,30,40,90,15,360,(45,30,71),(75,33,45))
t.done()
