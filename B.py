from turtle import *

def init(n):
    Tour0=[]
    Tour1=[]
    Tour2=[]

    Tour0=list(range (1,n+1))
    Plateau=[Tour0,Tour1,Tour2]
    return Plateau


def nombre_disques(plateau,numtour):
    c=len(plateau[numtour])
    return c


def disque_superieur(plateau,numtour):
    c=nombre_disques(plateau,numtour)
    if c ==0:
        return-1
    else:
        return plateau[numtour][c-1]
    #l=plateau[0]
    #n-l[C]
    #return c


    
def position_disque(plateau, numdisque):
    for l in range (0,3):
        print(l)
        plateau[l]
        try:
            position=plateau[l].index(numdisque)
            return l
        except ValueError:
            continue   

def verifier_deplacement(plateau,nt1,nt2):
    #on veut verifier que le dique deplacé soit plus petit que celui sur lequel on veut le placer
    d1=disque_superieur(plateau,nt1)
    d2=disque_superieur(plateau,nt2)
    if d1<0:
        return False
    if d2<0:
        return True
    return d1<d2


def verifier_victoire(plateau,n):
    jotaro=plateau[2]
    isDecroissant=jotaro==list(reversed(sorted(jotaro)))
    #sort() met dans l'ordre croissant reverse()les met dans l'ordre décroissant
    return n==len(jotaro)and isDecroissant


Tour0=[2,1]
Tour1=[]
Tour2=[3]
p=[Tour0,Tour1,Tour2]

setup(1500,600)
speed(0)
def dessine_plateau(n):
    up()
    goto(-600,0)
    down()
    n2=(n-1)*30+40
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
    t=position_disque(plateau,nd)
    if t==0:
        r=Tour0.index(nd)    
    elif t==1:
        r=Tour1.index(nd)
    elif t==2:
        r=Tour2.index(nd)
    print(t,r)
    goto((t+1)*20+(((n-1)*30+40)/2)*(t*2+1)-600-((nd-1)*30+40)/2,r*20+20)
    down()
    for i in range(0,4,1):
            if i%2==0:
                forward((nd-1)*30+40)
            else:
                forward(20)
            left(90)
    forward((nd-1)*15+17)
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

def efface_disque(nd,plateau,n):
    l20=[0,2,4,6]
    lef=[0,1,4,5]
    t=position_disque(plateau,nd)
    if t==0:
        r=Tour0.index(nd)    
    elif t==1:
        r=Tour1.index(nd)
    elif t==2:
        r=Tour2.index(nd)
    print(t,r)
    goto((t+1)*20+(((n-1)*30+40)/2)*(t*2+1)-600-((nd-1)*30+40)/2,r*20+20)
    left(90)
    for i in range(0,6,1):
        color("white")
        if i==2 or i==4:
            color("black")
        if i in l20:
            forward(20)
        if i==1 or i==5:
            forward((nd-1)*15+17)
        if i==3:
            forward(6)
        if i in lef:
            right(90)
        if i==2 or i==3:
            right(90)       
        
def dessine_config(plateau,n):
    dessine_plateau(n)
    for i in range(n,0,-1):
        dessine_disque(i)

def efface_tout(plateau,n):
    for i in range(n,0,-1):
        efface_disque(i,plateau,n)
    color("white")
    dessine_plateau(n)
    
    
    

dessine_plateau(3)

dessine_disque(2,p,3)
dessine_disque(1,p,3)
dessine_disque(3,p,3)

efface_disque(2,p,3)

exitonclick()
