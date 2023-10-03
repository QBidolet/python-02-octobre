une_liste = ["pomme", "banane", "kiwi"]
print(une_liste)

une_liste = ["pomme", 1.0, True, ["kiwi"], []]
print(une_liste)

# sélectionner sur un indice
print(une_liste[0], une_liste[3][0])

# ajouter
une_liste.append("Hello")
print(une_liste)
une_liste.insert(0, "Hello")
print(une_liste)
print(une_liste.count("kiwi"))

# supprimer un élément
del une_liste[0]
print(une_liste)
une_liste.remove("Hello")
print(une_liste)

# gestion mémoire
a = [1, 2, 3, 4, 5]
b = a
a[0] = 0
print(id(a), id(b))

# test d'apartenance
if 0 in a:
    print("0 est dans a.")

# parcours
for element in a:
    print(element)

# trie
a = [5, 2, 9, 4, 0]
a.sort(reverse=True)
print(a)
