"""
Créer une fonction qui affiche les
20 premiers termes de la table de multiplication
de 7.
BONUS :
Pouvoir rendre variable le nombre de termes et
la table choisie
"""

def generer_table_multiplication(table=7, nombre_terme=20):
    for nombre in range(1, nombre_terme+1):
        print(f"{table}X{nombre}={table*nombre}")

generer_table_multiplication(nombre_terme=15)

