# Un tuple est une liste immuable.
mon_tuple = ()
print(type(mon_tuple))

mon_tuple = (99, 22)
print(mon_tuple)

mon_tuple = 99, 22
print(type(mon_tuple))

# unpacking
a, b = mon_tuple
a, b = 99, 22
print(a, b)

# syntaxe de retour d'une fonction
def ma_func():
    return 10, 99

resultat = ma_func()
print(type(resultat))

# parcours d'un tuple
for element in resultat:
    print(element)
print(resultat[0])
# Immuable, sans modification ni suppression.