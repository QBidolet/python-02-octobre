# Ensemble désordonné sans doublon.

prenoms = {
    "Quentin",
    "Julien",
    "Pierre"
}

# Ajouter un élément
prenoms.add("Romain")
prenoms.add("Romain")
print(prenoms)

# Suppression d'un élément
prenoms.remove("Romain")

for prenom in prenoms:
    print(prenom)

# Cas d'utilisation
ma_liste = [1, 2, 2, 3, 4, 5, 5]
sans_doublon = set(ma_liste)
print(sans_doublon)