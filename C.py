def lire_coords(plateau):
    t=False
    while (t==False):
        ntourd=int(input("numéro de la tour de départ ")) 
        if ntourd>2:
            t=False
            print("valeur interdite")
        elif ntourd<0:
            t=False
            print("valeur interdite")
        else:
            t=True  
    t=False 
     while (t==False):
        ntoura=int(input("numéro de la tour de d'arrivée ")) 
        if ntoura>2:
            t=False
            print("valeur interdite")
        elif ntoura<0:
            t=False
            print("valeur interdite")
        else:
            t=True  
    l1=[ntourd,ntoura]
return l1


def jouer_un_coup(plateau,n):
    print(lire_coords(plateau))











def boucle_jeu(plateau,n):
    