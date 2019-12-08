from B import *
from A import *
def lire_coords(plateau):
    t=False
    while (t==False):
        ntourd=int(input("numéro de la tour de départ ")) 
        if ntourd>2 or ntourd<0:
            t=False
            print("valeur interdite")
        ntoura=int(input("numéro de la tour de d'arrivée ")) 
        if ntoura>2 or ntoura<0:
            t=False
            print("valeur interdite")
        else:
            for i in range (0,3):
                if (verifier_deplacement(plateau,ntourd,i)):
                    t=True
                    break 
        
    l1=(ntourd,ntoura)
    return l1


def jouer_un_coup(plateau,n):
    ntourd,ntoura=lire_coords(plateau)
    while not(verifier_deplacement(plateau,ntourd,ntoura)):
        print("Invalide")
        ntourd,ntoura=lire_coords(plateau)        
    r=plateau[ntourd][0]
    efface_disque(r,plateau,n)
    plateau[ntoura].insert(0,r)
    plateau[ntourd].pop(0)
    dessine_disque(r,plateau,n)


def boucle_jeu(plateau,n):
    p=0
    nmax=50
    verifier=verifier_victoire(plateau,n)
    while not(verifier):
        jouer_un_coup(plateau,n)
        if p>nmax:
            print("perdu trop de coups") 
        p+=1
        print(p)
        verifier=verifier_victoire(plateau,n)
    print("victoire")
    return p

    