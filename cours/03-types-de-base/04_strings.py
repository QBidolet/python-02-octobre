# Escape avec \
print('J\'ai 29 ans.')

# Combiner avec le +
prenom = "Quentin"
nom = "BIDOLET"
print(prenom + " " + nom)

# Je veux écrire la phrase :
# Je m'appelle Quentin BIDOLET.

# version simple
phrase = "Je m'appelle " + prenom + " " + nom + "."
print(phrase)

# version python 2
phrase = "Je m'appelle %25s %s." % (prenom, nom)
print(phrase)

# Version pythonic
phrase = f"Je m'appelle {prenom} {nom}."
print(phrase)

# Dupliquer
print("#"*25)

# Extraction de chaine de caractère [ ]
alphabet = "abcdefg"

# [start:end:step]
print(alphabet[0])

# end non inclus
print(alphabet[2:4])

# tout sélection
print(alphabet[::])

# sélectionner à partir de l'indice 2
print(alphabet[2:])

# sélection par pas de 2
print(alphabet[1::2])

# parcours à l'envers
print(alphabet[::-1])

# indice négatif
print(alphabet[:-2])