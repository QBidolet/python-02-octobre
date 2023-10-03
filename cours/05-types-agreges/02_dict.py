mon_dict = {
    "nom": "BIDOLET",
    "prenom": "Quentin"
}

print(mon_dict["nom"])

# parcours d'un dict sur les clés
for element in mon_dict.keys():
    print(element)

# parcours d'un dict sur les valeurs
for element in mon_dict.values():
    print(element)

for cle, valeur in mon_dict.items():
    print(cle, valeur)

# Exemple
users = {
    "125A": {
        "nom": "BIDOLET",
        "prenom": "Quentin",
        "competences": ["Python", "Javascript"]
    },
    "126B":{
        "nom": "DUPONT",
        "prenom": "Jean",
        "competences": ["HTML", "CSS"]
    },
}


