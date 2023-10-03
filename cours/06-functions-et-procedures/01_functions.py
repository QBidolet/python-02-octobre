# Définition d'une fonction
def do_nothing():
    pass


def somme(a, b):
    return a + b


resultat = somme(1, 2)


# *args
def print_2(*args):
    print(type(args))
    for arg in args:
        print(arg)


print_2("Test", "Deux", "Trois")


# **kwargs
def menu(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


menu(entree="entrée", vin="vin", plat="Oeuf au plat")


# paramètres positionnel et nommés
def menu(entree, plat, dessert="glace"):
    print("Entrée : " + entree)
    print("Plat : " + plat)
    print("Dessert : " + dessert)


menu("entrée", plat="plat")

# fonction anonyme
print("#" * 25)
liste = [1, 2, 3, 4]


def double(nombre):
    return nombre * 2


# for nombre in liste:
#     print(double(nombre))

# mon_map = map(double, liste)
# print(list(mon_map))
mon_map = map(lambda x: x * 2, liste)
print(list(mon_map))

# filter
ma_liste = [6, 7, 8, 9]
nombre_pairs_object = filter(lambda x: x % 2 == 0, ma_liste)
nombre_pairs = list(nombre_pairs_object)
print(nombre_pairs)


# closure
def fonction_externe():
    compteur = 10
    def fonction_interne():
        return 5 + compteur
    return fonction_interne

resultat = fonction_externe()
print(resultat())

# fonction génératrice
def range_2(n):
    compteur = 0
    while compteur < n:
        yield compteur
        compteur += 1

for i in range_2(6):
    print(i)