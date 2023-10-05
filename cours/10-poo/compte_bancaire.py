"""
    Définir une classe CompteBancaire().
    Elle permettra d'instancier des objets tels que
    compte_1, compte_2 etc.
    Le constructeur de cette classe
    doit initialiser deux attributs :
    - nom
    - solde
    avec les valeurs par défaut "DUPONT" et 1000.
    Trois méthodes doivent être définies :
    - deposer(somme) : ajouter une certaine somme au solde.
    - retirer(somme) : retirer une certaine somme au solde.
    - une méthode pour afficher la représentation en string
    du compte avec le nom du titulaire et le solde.
"""


class CompteBancaire:
    def __init__(self, nom="DUPONT", solde=1000):
        self.nom = nom
        self.solde = solde

    def deposer(self, somme):
        if somme > 0:
            self.solde += somme
        else:
            print("Vous ne pouvez pas ajouter une somme"
                  " inférieur ou égal à 0.")

    def retirer(self, somme):
        if somme > 0:
            self.solde -= somme

    def __str__(self):
        return f"Compte bancaire de {self.nom}\n" \
               f"Solde : {self.solde}"
