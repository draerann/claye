from B import *
from A import *
def lire_coords(plateau):
    t=False
    while (t==False):
        ntourd=int(input("numéro de la tour de départ ")) 
        if ntourd>2 or ntourd<0:
            t=False
            print("valeur interdite")
        ntoura=int(input("numéro de la tour de d'arrivée")) 
        if ntoura>2 or ntoura<0:
            t=False
            print("valeur interdite")
        else:
            for i in range (0,3):
                if (verifier_deplacement(plateau,ntourd,i)):
                    t=True
                    break 
        
    t=False 
    while (t==False):
        ntoura=int(input("numéro de la tour de d'arrivée ")) 
        if ntoura>2 or ntoura<0:
            t=False
            print("valeur interdite")
        elif (verifier_deplacement(plateau,ntourd,ntoura)):
            t=True
            break

    l1=(ntourd,ntoura)
    return l1


def jouer_un_coup(plateau,n):
    (ntourd,ntoura) = lire_coords(plateau)
    nd=disque_superieur(plateau,ntourd)
    efface_disque(nd,plateau,n)
    plateau[ntourd].remove(nd)
    nd=disque_superieur (plateau,ntoura)
    dessine_disque(nd,plateau,n)
    plateau[ntourd].remove(nd)
    plateau[ntoura].append(nd)

def boucle_jeu(plateau,n):
    p=0
    nmax=50
    while (not verifier_victoire(plateau,n)):
        jouer_un_coup(plateau,n)
        if p>nmax:
            print("perdu trop de coups")
        jouer_un_coup(plateau,n)
        p+=1
    
    return p

    