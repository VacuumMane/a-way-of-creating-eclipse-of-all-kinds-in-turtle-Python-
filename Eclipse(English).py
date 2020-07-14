import turtle as t
from math import *

def flyto(x,y): #funtioned as "t.goto(x,y)" without actual marks
    t.penup()
    t.goto(x,y)
    t.pendown()

def eclipse(x,y,a,b,angle1,angle2,angle3):
    '''(x,y) the center, (a,b)(the mayjor axis, the minor axis))，relative angle(the angle between the major axis and where you start to draw)),
    slope(the angle between the major axis and "x" axis), radian'''
    step=360 #cut into pieces(changeable)
    per=angle3/step
    x1=a*cos(radians(angle1))
    y1=b*sin(radians(angle1))
    flyto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))
    for i in range(1,step+1):
        x1=a*cos(radians(angle1+i*per))
        y1=b*sin(radians(angle1+i*per))
        t.goto(x+x1*cos(radians(angle2))-y1*sin(radians(angle2)),y+x1*sin(radians(angle2))+y1*cos(radians(angle2)))


#Test Zone
eclipse(eclipse,20,40,30,40,90,15,360,(0,0,0),(0,0,0))
t.done()