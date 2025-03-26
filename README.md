# 📍 Profil d'altitude : Montpellier → Ales (Bonus : Aubenas)

Ce projet vise à visualiser le profil d'altitude d'un itinéraire à vélo entre Montpellier (34) et Ales (30) à partir d'un fichier GPX.\
Il a été réalisé à l'aide de **Python** pour le traitement des données et **Tableau** pour la visualisation.

------------------------------------------------------------------------

## 🗺️ Données utilisées

-   Fichier GPX de l’étape i, exporté depuis [OpenRunner](https://www.openrunner.com/)
-   Conversion en fichier CSV via le site [GPX to CSV (MyGeodata)](https://mygeodata.cloud/converter/gpx-to-csv)
-   Enrichissement par géocodage inverse via [OpenCage API](https://opencagedata.com/)

------------------------------------------------------------------------

## ⚙️ Étapes de traitement

### 1. Exportation data brut

-   Création de l'itinéraire sur **OpenRunner**
-   Exportation en gpx

### 2. Conversion du GPX en CSV

-   Utilisation du site **mygeodata.cloud** pour convertir en CSV

### 3. Enrichissement en Python

-   Script Python pour :
    -   Lire le fichier CSV
    -   Ajouter une colonne `commune`
    -   Appeler l’API **OpenCage** toutes les 10 lignes pour economiser le nombre de requete (limit = 2500)
    -   Remplir les 9 lignes suivantes avec la **dernière commune trouvée**
    -   Exporter le tout dans `fichier_avec_communes.csv`

------------------------------------------------------------------------

## 📊 Visualisation avec Tableau

### Création d’un graphique d’altitude :

-   Columns : `track_seg_point_id`
-   Rows : `ele`
-   Remplissage (`area chart`) coloré par `commune`
-   Étiquettes dynamiques : nom des communes

------------------------------------------------------------------------

## 📝 Fichiers du projet

| Nom du fichier | Description |
|------------------------------------|------------------------------------|
| `data/etape1.gpx` | Fichier GPS exporté depuis OpenRunner |
| `data/fichier_avec_communes.csv` | Fichier CSV enrichi avec élévation et commune |
| `etape1.twb` | Fichier Tableau profil altitude |
| `add_city.py` | Script Python utilisé pour ajouter les communes |
| `README.md` | Ce fichier |

------------------------------------------------------------------------

## 🚀 Pour aller plus loin

-   Ajouter la **distance cumulée** en km à chaque point
-   Ajouter l'altitude sur les endroit clé
-   Créer une figure pour le dénivelé en pourcentage
-   Créer les **profils pour les étapes suivents** (Quissac→Ales→...→Aubenas)

------------------------------------------------------------------------

## 👤 Auteur

Chamss-Eddine LOUATI\
Mars 2025
