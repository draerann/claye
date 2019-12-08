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
        return -1
    else:
        return plateau[numtour][c-1]
    #l=plateau[0]
    #n-l[C]
    #return c


    
def position_disque(plateau, numdisque):
    for l in range (0,3):
        if numdisque in plateau[l]:
            return l
    raise ValueError

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
    isDecroissant=plateau[2]==list(sorted(plateau[2]))
    #sort() met dans l'ordre croissant reverse()les met dans l'ordre décroissant
    return n==len(plateau[2]) and isDecroissant