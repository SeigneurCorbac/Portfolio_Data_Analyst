# P6 — BottleNeck : analyse stock & ventes
 
## Contexte
BottleNeck, caviste en ligne fictif. Ce projet est la base sur laquelle
le P13 a été construit (voir dossier P13-bottleneck-clustering pour la
version améliorée et le détail de la démarche).
 
## Problème métier
Fusionner 3 sources de données (ERP, site web, table de liaison) et
produire une première analyse exploratoire du catalogue.
 
## Démarche
Nettoyage des 3 fichiers sources, détection d'anomalies (stocks négatifs,
codes articles incohérents, doublons), fusion en une table consolidée,
analyse univariée du prix, du chiffre d'affaires, des quantités vendues,
des stocks et de la marge.
 
## Résultat
Table consolidée exploitable, base de travail pour le P13.
 
## Compétences démontrées
Nettoyage de données multi-sources, détection d'anomalies, statistiques
descriptives.
 
## Outils
Python, pandas, matplotlib/plotly
 
## Livrables suggérés dans ce dossier
- Notebook d'analyse univariée
- Export de la table consolidée
 
## Voir aussi
Le dossier P13-bottleneck-clustering pour la suite : audit critique de
ce livrable (avec un bug de fusion non détecté ici, corrigé en P13) et
segmentation par clustering.
