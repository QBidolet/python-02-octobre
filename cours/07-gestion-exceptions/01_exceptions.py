try:
    nombre = int(input("Veuillez entrer un entier."))
    resultat = 7 / nombre
except ValueError as error:
    # print("Veuillez entrer un nombre valide.")
    print(error)
except ZeroDivisionError:
    # print("Veuillez entrer un nombre différent de 0.")
    # Actions etc.
    raise ZeroDivisionError("Veuillez rentrer une valeur de différente de 0.")
# except: # Fortement Déconseillé
#     print("Erreur")
else:
    print(resultat)
finally:
    print("finally")

