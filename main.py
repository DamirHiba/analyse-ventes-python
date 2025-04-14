import pandas as pd

# Charger les données depuis le fichier CSV
df = pd.read_csv("data/sales.csv")

# Afficher un aperçu des données
print("Aperçu des données :")
print(df.head())  # Affiche les 5 premières lignes du DataFrame

# Ajouter une colonne "Total" qui est la quantité * prix unitaire
df["Total"] = df["Quantité"] * df["Prix_unitaire"]

# Afficher les données avec la colonne "Total"
print("\nDonnées avec la colonne Total :")
print(df.head())
# Calculer le chiffre d'affaires total
chiffre_affaires_total = df["Total"].sum()

# Afficher le chiffre d'affaires total
print(f"Chiffre d'affaires total : {chiffre_affaires_total}")
# Analyser les ventes par produit
ventes_par_produit = df.groupby("Produit")["Total"].sum().reset_index()

# Afficher les résultats
print("\nVentes par produit :")
print(ventes_par_produit)
import matplotlib.pyplot as plt

# Créer un graphique en barres pour les ventes par produit
plt.bar(ventes_par_produit["Produit"], ventes_par_produit["Total"])

# Ajouter des labels
plt.title("Ventes par produit")
plt.xlabel("Produit")
plt.ylabel("Total des ventes")

# Afficher le graphique
plt.show()
# Convertir la colonne "Date" en format datetime
df["Date"] = pd.to_datetime(df["Date"])

# Analyser les ventes par date
ventes_par_date = df.groupby(df["Date"].dt.date)["Total"].sum().reset_index()

# Afficher les résultats
print("\nVentes par date :")
print(ventes_par_date)
# Analyser la vente moyenne par produit
moyenne_par_produit = df.groupby("Produit")["Total"].mean().reset_index()

# Afficher les résultats
print("\nVente moyenne par produit :")
print(moyenne_par_produit)
