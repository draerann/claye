from cmath import *
from A import *
from B import *
from C import *

def hanoiint(n,a=0,b=1,c=2,l=[]):
    if (n > 0):
        r,v,l=hanoiint(n-1,a,c,b,l)  
        l.append(r)
        l.append(v)
        l.append(a)
        l.append(c)
        u,n,l=hanoiint(n-1,b,a,c,l)
        l.append(u)
        l.append(n)
    return a,c,l

def hanoi(n,a=0,b=1,c=2,l=[]):
    a,b,l=hanoiint(n,a=0,b=1,c=2,l=[])
    l.insert(0,a)
    l.insert(1,b)
    return l,n

def resolution(l,n):
    print("Tour de Hanoï: résolution automatique")    
    plateau=init(n)
    dessine_config(plateau,n)
    victoire=False    
    while not(victoire):
        nd=disque_superieur(plateau,l[0])
        efface_disque(nd,plateau,n)
        plateau[l[0]].remove(nd)
        plateau[l[1]].append(nd)
        dessine_disque(nd,plateau,n)
        l.pop(0)
        l.pop(1)
        victoire=verifier_victoire(plateau,n)
    
n=8
l=[0,2,0,1,2,1,0,2,1,0,1,2,0,2]
resolution(l,n)