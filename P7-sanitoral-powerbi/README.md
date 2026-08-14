# P7 — Sanitoral : pilotage de portefeuille projets
 
## Contexte
Sanitoral, PMO (Project Management Office) fictif suivant des projets
IT et Marketing.
 
## Problème métier
Donner à 3 profils utilisateurs (Directeur Général, Directeur Régional,
Directeur de Pays) une vue de pilotage des projets en alerte (dépassement
de coût, délai ou livrable de plus de 15%), chacun avec un accès aux
données limité à son périmètre.
 
## Démarche
- Modélisation en étoile via une clé concaténée Clé_Projet_Phase reliant
  4 tables de faits
- 6 mesures DAX : écarts de coût/durée/livrable en %, statut d'alerte,
  nombre de projets en alerte, taux de complétion
- Sécurité au niveau ligne (Row-Level Security) avec 3 rôles distincts,
  basée sur USERPRINCIPALNAME() et LOOKUPVALUE()
 
## Résultat
Dashboard 8 pages conforme au Product Strategy Canvas défini en amont
(3 profils utilisateurs, 9 user stories), avec Q&R visuel et tooltips
personnalisés.
 
## Compétences démontrées
Modélisation en étoile, DAX, sécurité des données (RLS), conception de
Product Strategy Canvas, définition de user stories.
 
## Outils
Power BI
 
## Livrables suggérés dans ce dossier
- Fichier .pbix (ou captures d'écran)
- Product Strategy Canvas
- Guide de construction pas-à-pas
