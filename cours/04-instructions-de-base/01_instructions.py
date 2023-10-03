nom = "BIDOLET"
prenom = "Quentin"

# condition
if nom == "Julien":
    print("Bonjour Julien.")
elif prenom == "Michel":
    print("Bonjour Michel")
else:
    print("Aucune des conditions n'a été rempli.")

# boucle for
for caractere in nom:
    print(caractere, end="")

print('\n#'*25)

# enumerate
for indice, caractere in enumerate(nom):
    print(indice, caractere, sep="-")

# range
for i in range(6):
    print(i)

# while
i = 0
while i < 6:
    print(i)
    i += 1