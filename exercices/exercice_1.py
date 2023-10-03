# Demander à l'utilisateur de saisir
# une vitesse en miles/heure
# et vous la convertisser en km/h et m/s.
# Indication pour la conversion :
# pour passer des miles à heures
# au m/s il faut diviser par 2.237.
# pour passer miles/heure au km/h il faut multiplier par 1.609

continuer = "oui"
while continuer == "oui":
    vitesse_mh = float(input("Veuillez saisir une vitesse en miles/heure.\n"))
    vitesse_kmh = vitesse_mh * 1.609
    vitesse_ms = vitesse_mh / 2.237
    print(f"Vitesse en km/h: {vitesse_kmh}")
    print(f"Vitesse en ms: {vitesse_ms}")
    continuer = input("Voulez-vous continuer ? (oui/non)").lower()


