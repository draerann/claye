Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def init(n):
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
    if numtour==0:
        c=len(plateau[0])
    elif numtour==1:
        c=len(plateau[1])
    elif numtour==2:
        c=len(plateau[2])
    else:
        c=None
    
    if c==0:
        c=-1

    return c

def disque_superieur(plateau,numtour):
    
    if numtour==0:
        c=nombre_disques(plateau,0)
        l=plateau[0]
        n=l[c]
        
    elif numtour==1:
        c=nombre_disques(plateau,1)
        l=plateau[1]
        n=l[c]
        
    elif numtour==2:
        c=nombre_disques(plateau,2)
        l=plateau[2]
        n=l[c]
        
    return c
    
print(disque_superieur(init(5),0))
