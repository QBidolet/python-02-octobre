# Fonction print de base
print("Hello World!")

# Séparateur
print("Hello", "World!", sep="$")

# End
print("Hello", "World!", sep="+", end="**\n")
print("Hello", "World!")

# Notons qu'on peut utiliser les guillemets doubles
# ou simples.
# Arguments
nom = "BIDOLET"
prenom = "Quentin"
print('Je suis {0} {1}.'.format(nom, prenom))

print("J'ai 20 ans.")
print('"Quentin"')
print('Il s\'appelle "Quentin".')

# Ecrire deux lignes avec un retour chariot.
print("Première ligne.\nDeuxième Ligne.")

# Multilignes
print("""Une ligne.
Une autre.
etc.""")