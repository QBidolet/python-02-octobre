# Module intégré donc import os "tout court"
import os

# A ne pas faire : on évite les chemins absolus
chemin = "D:/users/quentin/python/projet/fichier.py"

# Chemin relatif
print(os.getcwd())
chemin = os.getcwd() + "\mon_fichier.txt"
chemin = os.path.join(os.getcwd(), "dossier", "mon_fichier.txt")
print(chemin)

# Vérifier l'existence d'un fichier
print(os.path.isfile(chemin))
print(os.path.isdir(chemin))

# Créer un répertoire
os.makedirs("data", exist_ok=True)

# Récupérer nom et extension d'un fichier
nom, extension = os.path.splitext("data/mon_fichier.txt")
print(nom, extension)

# lister les dossiers et les fichiers
print(os.listdir(os.getcwd()))
