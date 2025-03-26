import requests
import pandas as pd
import time

"""
Ce script permet d'ajouter une colonne "commune" à un fichier CSV contenant des coordonnées GPS.
Pour cela, il interroge l'API OpenCageData pour obtenir la commune correspondant à chaque coordonnée.
"""

# Charge ton fichier CSV avec les colonnes latitude et longitude
df = pd.read_csv("C:/Users/Louati/Downloads/mygeodata/etape1/track_points.csv")

# Clé API OpenCage
API_KEY = "ENTER YOUR API KEY HERE"

# Fonction qui interroge l'API
def get_commune(lat, lon):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    try:
        return data["results"][0]["components"].get("city", "")
    except:
        return "Inconnu"

# Initialisation
commune_actuelle = ""

# Parcours des lignes
for i in range(len(df)):
    if i % 10 == 0:  # Une ligne sur 10
        lat = df.at[i, "Y"]
        lon = df.at[i, "X"]
        commune_actuelle = get_commune(lat, lon)
        time.sleep(1)  # Petite pause pour éviter un trop grand nombre de requêtes trop vite
        print(str(i/len(df)*100) + "%")
    df.at[i, "commune"] = commune_actuelle  # Remplit toutes les lignes avec la dernière valeur connue

# Sauvegarde
df.to_csv("fichier_avec_communes.csv", index=False)
print("Fichier sauvegardé avec les communes")