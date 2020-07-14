import turtle as t
from math import *

def flyto(x,y): #抬笔到某个点
    t.penup()
    t.goto(x,y)
    t.pendown()

def eclipse(x,y,a,b,angle1,angle2,angle3):
    #(x,y)原点，(a,b)(长轴,短轴))，起画相对角度（指相对长轴夹角），斜度（长轴与x轴夹角），弧度
    step=360 #分割份数（可变）
    per=angle3/step
    x1=a*cos(radians(angle1))
    y1=b*sin(radians(angle1))
    flyto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))
    for i in range(1,step+1):
        x1=a*cos(radians(angle1+i*per))
        y1=b*sin(radians(angle1+i*per))
        t.goto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))


#测试区
eclipse(eclipse,20,40,30,40,90,15,360,(0,0,0),(0,0,0))
t.done()
