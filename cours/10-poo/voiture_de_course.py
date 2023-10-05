from voiture import Voiture

# Héritage multiple en séparant par des virgules
# Exemple
# class Enfant(Parent1, Parent2, Parent3) etc.
class VoitureDeCourse(Voiture):
    def __init__(self, couleur, marque, vitesse):
        Voiture.__init__(self, couleur, marque)
        self.vitesse = vitesse

    def set_vitesse(self, vitesse):
        self.vitesse = vitesse

    def __str__(self):
        return f"Je suis une voiture de course" \
               f"de vitesse {self.vitesse}" \
               f", de couleur {self.couleur}" \
               f" et de marque {self.marque}."
