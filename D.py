def dernier_coups(coups,num_der_coups):
    pre_plateau=coups[num_der_coups]
    return pre_plateau

def annuler_dernier_coup(coups,num_der_coups):
    cp=dernier_coups(coups,num_der_coups)
    
    del coups[num_der_coups]
    d=cp[1]
    a=cp[0]
    nd=disque_superieur(plateau,d)
    efface_disque(nd,plateau,n)
    
    plateau[d].remove(nd)
    plateau[a].append(nd)
    
    dessine_disque(nd,plateau,n)
    return cp

