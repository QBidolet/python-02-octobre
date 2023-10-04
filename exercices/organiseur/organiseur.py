"""
Construire un organiseur de fichier
selon le dictionnaire donné.
Le programme doit scanner le dossier et devra
créer un dossier correspondant au type de fichier
et déplacer celui-ci à l'intérieur.
Exemple : Dans mon dossier A TRIER j'ai
une fichier PDF, je crée un répertoire PDF
et je déplace le fichier à l'intérieur.
"""
import os
import shutil

folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

chemin_a_trier = os.path.join(os.getcwd(), "A TRIER")

# for fichier in os.listdir(chemin_a_trier):
#     chemin_fichier = os.path.join(chemin_a_trier, fichier)
#     if os.path.isfile(chemin_fichier):
#         _, extension = os.path.splitext(fichier)
#         for key, values in folder_dict.items():
#             if extension.strip().lower() in values:
#                 chemin_dossier = os.path.join(os.getcwd(), key)
#                 os.makedirs(chemin_dossier, exist_ok=True)
#                 shutil.move(chemin_fichier, chemin_dossier)

# for element in os.scandir(chemin_a_trier):
#     if element.is_file():
#         _, extension = os.path.splitext(element.name)
#         for key, values in folder_dict.items():
#             if extension in values:
#                 chemin_dossier = os.path.join(os.getcwd(), key)
#                 os.makedirs(chemin_dossier, exist_ok=True)
#                 chemin_element = os.path.join(chemin_a_trier, element.name)
#                 print(chemin_element)
#                 shutil.move(chemin_element, chemin_dossier)

for folder, subfolders, files in os.walk(chemin_a_trier):
    for file in files:
        _, extension = os.path.splitext(file)
        for key, values in folder_dict.items():
            if extension in values:
                chemin_dossier = os.path.join(os.getcwd(), key)
                os.makedirs(chemin_dossier, exist_ok=True)
                chemin_element = os.path.join(folder, file)
                shutil.move(chemin_element, chemin_dossier)
