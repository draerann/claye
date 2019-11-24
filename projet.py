from turtle import *
from la import *

Tour0=[1]
Tour1=[2]
Tour2=[3]
p=[Tour0,Tour1,Tour2]

setup(1500,600)

def dessine_plateau(n):
    up()
    goto(-600,0)
    down()
    n2=n*30+40
    for i in range(0,4,1):
        if i%2==0:
            forward(3*n2+4*20)            
        else:
            forward(20)            
        left(90)
    up()
    for i in range(0,3,1):
        x=(1+i)*20+(1+i*2)*(n2/2)-3
        goto(x-600,20)
        down()
        for i in range(0,4,1):
            if i%2==0:
                forward(6)
            else:
                forward(n*20+40)
            left(90)
        up()

def dessine_disque(nd,plateau,n):
    color("black")
    t=position_disque(p,nd)
    if t==0:
        r=Tour0.index(nd)    
    elif t==1:
        r=Tour1.index(nd)
    elif t==2:
        r=Tour2.index(nd)
    
    goto((t+1)*(20+15*(n-nd)+(n*30+20)*t+(t*6)-601,r*20+20))
    down()
    for i in range(0,4,1):
            if i%2==0:
                forward(nd*30+40)
            else:
                forward(20)
            left(90)
    forward(nd*15+17)
    for i in range(0,4,1):
        if i%2==0:
            forward(6)            
        else:
            down()
            forward(1)
            color("white")
            forward(19)
            color("black")
            up()            
        left(90)
    forward(-nd*15-17)

   
    
    
    

dessine_plateau(3)

dessine_disque(2,p,3)
dessine_disque(3,p,3)

