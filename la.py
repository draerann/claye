def init(n):
    Tour0=[]
    Tour1=[]
    Tour2=[]
    
    while n>0:
        Tour1.append(n)
        n-=1
    Plateau=[Tour0,Tour1,Tour2]
    return Plateau

print(init(5))

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
    
print(disque_superieur(init(5),0))
print(disque_superieur(init(5),1))
print(disque_superieur(init(5),2))


def position_disque(plateau, numdisque):
    for l in range (0,2):
        plateau[l]
        try:
            position=plateau[l].index(numdisque)
            return l
        except ValueError:
            continue
n=int(input("nombre de disque: "))
for i in range (0,n):
    print (position_disque(init(5),i))

def verifier_deplacement(plateau,nt1,nt2):
    #on veut verifier que le dique deplacé soit plus petit que celui sur lequel on veut le placer
    d1=disque_supérieur(plateau,nt1)
    d2=disque_supérieur(plateau,nt2)
    return d1<d2

def verifier_victoire(plateau,n):
    jotaro=plateau[2]
    isDecroissant=jotaro==list(reversed(sorted(jotaro)))
    #sort() met dans l'ordre croissant reverse()les met dans l'ordre décroissant
    return n==len(jotaro)and isDecroissant
    
