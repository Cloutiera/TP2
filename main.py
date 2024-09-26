"""
Programme fait par Albert Cloutier
groupe 406
jeu de devinette
"""

from random import randint

continuer = 1
maximum = 100
minimum = 0


def bornes():
    global minimum, maximum
    minimum = int(input("Entrez la borne minimale\n"))
    maximum = int(input("Entrez la borne maximale\n"))


while continuer == 1:

    bornes()
    print(minimum, maximum)

    nombre = randint(minimum, maximum)
    nbr_essais = 0
    reponse = 0
    print("J'ai choisi un nombre entre %d et %d. À toi de le deviner" % (minimum, maximum))

    while reponse != nombre:
        nbr_essais += 1
        reponse = int(input("Entrez votre réponse\n"))
        # print(nombre)
        if reponse > nombre:
            print("Mauvaise réponse, le nombre est plus petit que", reponse)
        elif nombre > reponse:
            print("Mauvaise réponse, le nombre est plus grand que", reponse)
        elif nombre == reponse:
            print("Bravo %d était la bonne réponse. Vous avez réussi en %d essais" % (reponse, nbr_essais))
        else:
            print("nombre invalide")
    continuer = int(input("voulez-vous continuer\n1. oui\n2. non\n"))
    if continuer == 2:
        print("Au revoir.")
