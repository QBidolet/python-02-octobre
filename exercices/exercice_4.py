"""
Créer un programme qui demande à l'utilisateur
de saisir des noms chats.
Le programme s'arrête quand l'utilisateur décide
d'arrêter la saisie, sinon il continue.
Une fois que l'utilisateur arrête la saisie,
le programme doit afficher la liste des chats saisies
dans l'ordre saisie.

BONUS :
Ne pas pouvoir saisir deux fois le même nom.
Afficher l'indice des noms.

1er étape:
Demander à l'utilisateur de saisir

2eme étape:
Stockage : dans quelle structure ?

3ème étape:
Afficher le résultat (dans le terminal)

4ème :
Gérer plusieurs saisies
"""
chats = []

# Gérer la saisie utilisateur
saisie = ""
mots_stop = ["exit", "stop", "quit", "quitter"]

while saisie.lower() not in mots_stop:
    saisie = input("Entrez un nom de chat.\n")
    saisie = saisie.strip().lower().capitalize()
    if saisie in chats:
        print(f"Vous avez déjà saisie le nom {saisie}.")
    elif saisie != "":
        print("Veuillez saisir un nom de chat valide.")
        break
    elif saisie.lower() not in mots_stop:
        chats.append(saisie)

# Gérer l'affichage à l'utilisateur
print("La liste des chats :")
for indice, chat in enumerate(chats):
    print(f"Chat n°{indice+1}: {chat}.")