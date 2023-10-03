"""
Ecrire un programme qui recherche
le plus élément dans une liste.
Par exemple, [32, 5, 12, 8, 3, 75]
ce programme doit afficher : 75.
Contrainte :
le faire "à la main"
pas de fonction max, sort, etc.
"""
ma_liste = [32, 5, 12, 8, 3, 75]

if ma_liste:
    max = ma_liste[0]
    for nombre in ma_liste:
        if nombre > max:
            max = nombre
    else:
        print(f"Le maximum est {max}.")
else:
    print("La liste doit être valide.")