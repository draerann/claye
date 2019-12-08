from pickle import *

def enregistre(n,nc,time="10000"):
    nom=str(input("Entrez votre nom:"))
    while len(nom)>10:
        nom=int(input("10 caractère maximum:"))
    while len(nom)<=10:
        nom+=" "

    S={"nom":nom,"disque":n,"coup":nc,"time":time}

    print(S)
    dump(S,open('score.txt','ab'))

def tableau():
    l=[]
    lfin=[]
    score=open('score.txt','rb')
    tab=load(score)
    l.insert(0,tab)
    while len(l)<10:
        try:
            tab=load(score)
        except:
            break
        print(tab)            
        l.append(tab)    
    #Tri de la liste
    i=0
    while i<len(l):
        tab=l(i)
        l.pop(i)
        c=i+1
        tab2=l(c)
        while tab["coup"]<tab2["coup"]:
            c+1
        l.insert(c,tab)
        i+=1
    print(lfin)












tableau()

def temps():
    t=0
    for i in range(0,100):
        try:
            tab=load(open('score.txt','rb'))
        except:
            break
        S+=tab["time"]
        t+=1
    moy=S/t
    return moy
