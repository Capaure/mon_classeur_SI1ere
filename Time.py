from datetime import datetime, timedelta

# Définir les horaires des cours
cours_horaires = {
    "lundi": (11, 5, 12, 5),    # Début : 11h05, Fin : 12h05
    "mardi": (7, 55, 9, 55),   # Début : 7h55, Fin : 9h55
    "vendredi": (16, 20, 17, 20),  # Début : 16h20, Fin : 17h20
}

# Fonction pour obtenir le temps avant le prochain cours
def temps_avant_cours():
    maintenant = datetime.now()
    jour_semaine = maintenant.strftime("%A").lower()  # Obtenir le jour en minuscule (e.g., "lundi")
    heure_actuelle = maintenant.time()
    
    # Liste ordonnée des jours de la semaine pour calculer les décalages
    jours_ordre = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

    prochain_cours = None
    temps_restant_minimum = timedelta(days=7)  # Valeur maximale initiale

    # Vérifier chaque jour où il y a un cours
    for jour, horaires in cours_horaires.items():
        debut_heure, debut_minute, _, _ = horaires
        
        # Calculer la date et l'heure du cours
        cours_datetime = datetime(
            maintenant.year, maintenant.month, maintenant.day,
            debut_heure, debut_minute
        )
        
        # Décalage en jours pour les cours après aujourd'hui
        decalage_jour = (jours_ordre.index(jour) - jours_ordre.index(jour_semaine)) % 7
        if decalage_jour < 0 or (decalage_jour == 0 and heure_actuelle >= cours_datetime.time()):
            decalage_jour += 7  # Passer au jour suivant si nécessaire

        # Ajouter le décalage
        cours_datetime += timedelta(days=decalage_jour)
        
        # Calculer le temps restant
        temps_restant = cours_datetime - maintenant
        if 0 < temps_restant < temps_restant_minimum:
            temps_restant_minimum = temps_restant
            prochain_cours = cours_datetime

    # Afficher le temps avant le prochain cours
    if prochain_cours:
        heures, reste_secondes = divmod(temps_restant_minimum.total_seconds(), 3600)
        minutes, _ = divmod(reste_secondes, 60)
        return f"Prochain cours dans {int(heures)} heures et {int(minutes)} minutes."
    else:
        return "Pas de cours prévu."

# Appeler la fonction pour afficher le temps avant le prochain cours
print(temps_avant_cours())
