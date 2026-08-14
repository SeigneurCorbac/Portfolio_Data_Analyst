# P11 — La Poule Qui Chante : ciblage de marchés export
 
## Contexte
Entreprise fictive de volaille bio cherchant à identifier des marchés
d'export prioritaires.
 
## Problème métier
Parmi 137 pays, quels sont les marchés les plus prometteurs pour exporter
du poulet biologique ?
 
## Démarche
- ACP (analyse en composantes principales) sur 11 variables
  socio-économiques et agricoles
- Double clustering comparé : CAH (classification ascendante hiérarchique)
  et K-Means
- Identification automatisée du segment cible via un score de priorité
  normalisé
- Exclusion argumentée des micro-marchés (Samoa, Dominique) malgré un
  taux d'import élevé — volume absolu jugé insuffisant pour un export
  rentable
 
## Résultat
Ciblage des pays du Golfe (Émirats arabes unis, Koweït, Arabie Saoudite,
Oman) comme marché prioritaire structurel, avec silhouette de clustering
validée (~0,32) sur un panel hétérogène de 137 pays.
 
## Compétences démontrées
ACP, clustering (CAH, K-Means), feature engineering, argumentation
d'exclusion de données sur critère métier.
 
## Outils
Python, scikit-learn, pandas
 
## Livrables suggérés dans ce dossier
- Notebook 1 — préparation des données
- Notebook 2 — ACP et clustering
- Présentation (PPTX, 20 slides)
- Document de préparation à la soutenance
