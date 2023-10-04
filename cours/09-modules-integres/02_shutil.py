import os
import shutil

# copier des fichiers et des dossiers.
# on peut aussi renommer le nom de destination.
# attention : si le fichier est existant il sera écrasé.

src = os.path.join(os.getcwd(), "test.txt")
os.makedirs(os.path.join(os.getcwd(), "mon_dossier"), exist_ok=True)
dst = os.path.join(os.getcwd(), "mon_dossier", "test_2.txt")
shutil.copy(src, dst)

# Copie récursive
src = os.path.join(os.getcwd(), "data")
dst = os.path.join(os.getcwd(), "data_backup")
# Si le dossier existe, une exception est levée.
# shutil.copytree(src, dst)

# suppression récursive
shutil.rmtree(dst)

# déplacement
src = os.path.join(os.getcwd(), "test.txt")
dst = os.path.join(os.getcwd(), "mon_dossier")
shutil.move(src, dst)