# P13 — BottleNeck : segmentation augmentée par l'IA
 
## Contexte
Amélioration critique du livrable P6, menée avec un usage encadré de l'IA :
veille technologique comparative, cahier des charges fonctionnel, POC
documenté (hypothèses, tests, résultats, décisions), pilotage de projet.
 
## Problème métier
Le P6 analysait le catalogue produit par produit, variable par variable —
un constat, pas une décision. Comment regrouper automatiquement les
produits en familles actionnables pour l'assortiment, le pricing et la
gestion de stock ?
 
## Démarche
- Audit critique de l'export du P6 : détection ET correction à la source
  d'un bug de fusion pandas (jointure sur NaN==NaN, 182 lignes corrompues
  sur 916), avec reproduction du bug et validation croisée de la correction
- Isolement des invendus par règle métier avant clustering
- Comparaison de 2 jeux de variables (3 axes vs 4 axes) et 2 algorithmes
  (KMeans vs Clustering Agglomératif)
- Arbitrage documenté entre performance statistique (silhouette) et valeur
  métier (k=3 optimal statistiquement, k=4 retenu pour révéler un segment
  actionnable)
 
## Résultat
689 produits segmentés en 4 familles nommées et actionnables : Moteur de
CA (327), Premium à faible rotation (189), Nouveautés performantes (141),
Stock dormant (32 — rotation de stock 6x supérieure à la moyenne,
recommandation de déstockage prioritaire).
 
## Compétences démontrées
Clustering non supervisé (KMeans, CAH), audit critique de données, veille
technologique sourcée, cahier des charges fonctionnel, gestion de projet
(lots/backlog/planning/registre des risques), traçabilité de l'usage de
l'IA.
 
## Outils
Python, pandas, scikit-learn, matplotlib/seaborn, Jupyter
 
## Livrables dans ce dossier
- p6_extended.ipynb — notebook POC exécuté de bout en bout
- documentation.md — cahier des charges, veille, démarche complète,
  pilotage de projet
- erp.xlsx, web.xlsx, liaison.xlsx — fichiers sources
