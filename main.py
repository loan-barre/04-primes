"""
Programme permettant de savoir si un nombre entier est premier
"""
from math import sqrt


#### Fonction secondaire

def isprime(p):
    """
    Determine si le nombre est premier

    Arg:
    p: valeur entière
    
    Returns: True/False
    """
    index = int(sqrt(p))
    if p==1:
        return False
    if p==2:
        return True
    for d in range(2, index+1):
        if p%d == 0:
            return False
    return True



#### Fonction principale

def main():
    """
    Permet l'appel des fonctions du programme
    """
    # vos appels à la fonction secondaire ici
    isprime(3)
    isprime(37)
    isprime(1000345)
    isprime(19)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
