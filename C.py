from B.py import *

def lire_coords(plateau):
    t=False
    while (t==False):
        ntourd=int(input("numéro de la tour de départ ")) 
        if ntourd>2 or ntourd<0:
            t=False
            print("valeur interdite")
        elif:
            for i in range (0,3):
                if (verifier_deplacement(plateau,ntourd,i):
                    t=True
                    break 
        
    t=False 
     while (t==False):
        ntoura=int(input("numéro de la tour de d'arrivée ")) 
        if ntoura>2 or ntoura<0:
            t=False
            print("valeur interdite")
        elif (verifier_deplacement(plateau,ntourd,ntoura):
            t=True
            break

    l1=(ntourd,ntoura)
return l1


def jouer_un_coup(plateau,n):
    (ntourd,ntoura) = lire_coords(plateau)
    nd=disque_supérieur (plateau,ntourd)
    efface_disque(nd,plateau,n)
    plateau[ntourd].remove(ndisque)
    nd=disque_supérieur (plateau,ntoura)
    dessine_disque(nd,plateau,n)
    plateau[ntourd].remove(ndisque)
    liste.append(nd)

def boucle_jeu(plateau,n):
    
    