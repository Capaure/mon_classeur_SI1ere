from datetime import datetime

# Obtenir l'heure actuelle
current_time = datetime.now()

# Formater l'heure (exemple : HH:MM:SS)
formatted_time = current_time.strftime("%H:%M:%S")

# Afficher l'heure
print("L'heure actuelle est :", formatted_time)
