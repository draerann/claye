from la import *

class TonProgrammePue(Exception):
    pass

def assertTrue(val1,val2,raison):
    if(val1 != val2):
        print(raison)
        raise TonProgrammePue(raison + str(val1) + str(val2))
    return True

def test_nombre_disques():
    plat = init(5)
    assertTrue(nombre_disques(plat,0),0,"tour vide")
    assertTrue(nombre_disques(plat,1),5, "tour remplie a 5")

def test_disque_supérieur():
    plat = init(5)
    assertTrue(disque_superieur(plat,0), -1, "tour vide")
    assertTrue(disque_superieur(plat,1), 5, "tour remplie")

def test_position_disque():
    plat = init(5)
    assertTrue(position_disque(plat,1),1,"position initiale")
    assertTrue(position_disque(plat,2),1, "pos initiale")

def test_verifier_deplacement():
    plat = init(5)
    assertTrue(verifier_deplacement(plat,0,1), False, "vide sur plein")
    assertTrue(verifier_deplacement(plat,0,2),False, "vide sur vide")
    assertTrue(verifier_deplacement(plat,1,2),True, "plein sur vide")
    assertTrue(verifier_deplacement(plat,1,1),True, "plein sur plein")

def test_verifier_victoire():
    plat = init(5)
    assertTrue(verifier_victoire(plat,5), False, "etat initial n'est pas victoire")
    plat = [[],[],[4,3,2,1]]
    assertTrue(verifier_victoire(plat,5), False, "pas assez de disques")
    assertTrue(verifier_victoire(plat,4), True, "etat initial n'est pas victoire")
    plat = [[],[],[4,2,3,1,5]]
    assertTrue(verifier_victoire(plat,5), False, "disques désordonnés")


def tests():
    test_disque_supérieur()
    test_nombre_disques()
    test_position_disque()  
    test_verifier_deplacement()  
    test_verifier_victoire()

tests()