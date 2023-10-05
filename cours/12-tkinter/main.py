import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar


def main():
    # Création de la fenêtre
    fenetre = Tk()
    fenetre.geometry("410x450")
    fenetre.title("Annuaire")
    fenetre.configure(background="powder blue")

    # Créer les widgets
    nom_label = Label(fenetre, text="Nom :")
    nom_label.place(x=0, y=0)

    telephone_label = Label(fenetre, text="Téléphone :")
    telephone_label.place(x=0, y=30)

    # Création de champs de saisie
    # Sur Tkinter Entry ce sont les inputs.
    global nom_var
    global telephone_var
    nom_var = StringVar()
    telephone_var = StringVar()

    nom_entry = Entry(fenetre, width=20, textvar=nom_var)
    nom_entry.place(x=80, y=0)

    telephone_entry = Entry(fenetre, width=20, textvar=telephone_var)
    telephone_entry.place(x=80, y=30)

    # Création des boutons
    bouton_insertion = Button(fenetre, text="Insérer",
                              command=insert)
    bouton_insertion.place(x=80, y=100)

    bouton_afficher = Button(fenetre, text="Afficher",
                             command=afficher)
    bouton_afficher.place(x=130, y=100)

    fenetre.mainloop()

def afficher():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contacts;")
    for element in cursor.fetchall():
        nom, telephone = element
        print(nom, telephone)

    cursor.close()
    connection.close()

def create_database():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "
                   "contacts(nom TEXT, telephone TEXT);")
    connection.commit()
    # ORM SqlAlchemy
    cursor.close()
    connection.close()

def insert():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO contacts VALUES "
                   "(?,?);", (nom_var.get(),
                             telephone_var.get()))
    connection.commit()

    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_database()
    main()
