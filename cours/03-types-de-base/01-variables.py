# Noms de variable utilise le snake_case
# TOUT l'alphabet SAUF - , @ / \ #
# Un nom de variable ne doit pas commencer
# par un chiffre ou un underscore.

ma_boite = 42
ma_boite_2 = ma_boite
print(id(ma_boite))
print(id(ma_boite_2))
print(id(42))

# noms de variables valides
# a
# a_1
# a1
# _abc

# noms de variables invalides
# 1a
# 1_
# a@
# for etc. tous les noms réservés