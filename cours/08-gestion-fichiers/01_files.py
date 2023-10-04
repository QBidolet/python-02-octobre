# 4 modes d'ouvertures
# r : pour lire
# w : pour écrire et écraser le contenu.
# x : pour écrire seulement si le fichier est inexistant.
# a : ajouter à la suite. (append)

# Méthode classique
fichier = open("mon_fichier.txt", "rt")
print(fichier.read())
fichier.close()

# Méthode pythonic avec with.
with open("mon_fichier.txt", "rt") as fichier:
    contenu = fichier.read()
    print(contenu)

# Ecriture dans le fichier avec a ou w
with open("mon_fichier.txt", "w") as fichier:
    fichier.write("Un mot.")


# Lire ligne par ligne
with open("mon_fichier.txt", "r") as fichier:
    for ligne in fichier.readlines():
        print(ligne)

# seek
print("#"*25)
fichier = open("mon_fichier.txt", "r")
print(fichier.read())
fichier.seek(1)
print(fichier.tell())
print(fichier.read())
fichier.close()

fruits = ["banane", "kiwi"]
with open("mon_fichier.txt", "w") as fichier:
    fichier.writelines(fruits)