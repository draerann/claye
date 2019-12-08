from turtle import *
from A import *

setup(1500,600)
speed(9)

def dessine_plateau(n):
    #On place le curseur et fixe les valeurs utiles
    up()
    goto(-600,0)
    down()
    n2=(n-1)*30+40
    #On trace le plateau
    for i in range(0,4,1):
        if i%2==0:
            forward(3*n2+4*20)          
        else:
            forward(20)            
        left(90)
    up()
    #Puis les 3 tours
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
    #On fixe les valeurs qui nous servirons à placer le disque
    color("black")
    t=position_disque(plateau,nd)
    if t==0:
        r=len(plateau[0])-plateau[0].index(nd)
    elif t==1:
        r=len(plateau[1])-plateau[1].index(nd)
    elif t==2:
        r=len(plateau[2])-plateau[2].index(nd)    
    #On se place en bas à gauche du disque     
    goto((t+1)*20+(((n-1)*30+40)/2)*(t*2+1)-600-((nd-1)*30+40)/2,r*20)
    down()
    #On trace le disque
    for i in range(0,4,1):
            if i%2==0:
                forward((nd-1)*30+40)
            else:
                forward(20)
            left(90)
    forward((nd-1)*15+17)
    #On efface la tour derrière
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
    #Parallèlement à dessine disque, on récupère là hauteur, le décalage à droite où a gauche
    seth(0)
    t=position_disque(plateau,nd)
    if t==0:
        r=len(plateau[0])-plateau[0].index(nd)
    elif t==1:
        r=len(plateau[1])-plateau[1].index(nd)
    elif t==2:
        r=len(plateau[2])-plateau[2].index(nd)
    #On efface les trois segements superieur du disque (le dernier étant confondu avec le disque inférieur)
    goto((t+1)*20+(((n-1)*30+40)/2)*(t*2+1)-600-((nd-1)*30+40)/2,r*20+1)
    left(90)
    pencolor("white")
    down()
    forward(19)
    right(90)
    forward((nd-1)*30+40)
    right(90)
    forward(20)
    up()
    #Puis on retrace les deux segements de la tour
    goto((t+1)*20+(((n-1)*30+40)/2)*(t*2+1)-600-((nd-1)*30+40)/2+((nd-1)*30+40)/2-3,r*20+1)
    right(180)
    color("black")
    down()
    forward(20)
    up()
    goto((t+1)*20+(((n-1)*30+40)/2)*(t*2+1)-600-((nd-1)*30+40)/2+((nd-1)*30+40)/2+3,r*20+1)
    down()
    forward(20)
    up()

def dessine_config(plateau,n):
    #On dessine tout les disques, du plus grand au plus petit
    dessine_plateau(n)
    for i in range(n,0,-1):
        dessine_disque(i,plateau,n)

def efface_tout(plateau,n):
    #Je trace un grand cadre blanc de 10 de coté de plus que le plateau, que je remplis de blanc
    pencolor("white")
    fillcolor("white")
    begin_fill()
    up()
    goto(-610,-10)
    down()
    seth(0)
    for i in range(0,5,1):
        if i%2==0:
            forward(3*((n-1)*30+40)+5*20)
            left(90)    
        if i%2!=0:
            forward(20*n+80)
            left(90)
    end_fill()
