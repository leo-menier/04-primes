"""
 Permet d'obtenir une liste de nombres premiers.
"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Détermine si un nombre est premier.

    Paramètre:
    p (int): Le nombre à tester.

    Retourne:
    bool: True si le nombre est premier, False sinon.
    """
    # On commence par vérifier si p est strictement inférieur à 2, auquel cas il n'est pas premier
    if p < 2:
        return False
    # On vérifie les diviseurs potentiels de 2 jusqu'à la racine carrée de p
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:  # Si p est divisible par i, ce n'est pas un nombre premier
            return False
    # Si aucun diviseur n'est trouvé, p est premier
    return True


#### Fonction principale

def main():
    """
    Print tous les nombres premiers de 0 à 99.
    """
    # Vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
