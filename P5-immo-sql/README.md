# P5 — DATAImmo : base de données de valeurs foncières (Laplace Immo)
 
## Contexte
Projet pour l'agence immobilière fictive Laplace Immo : construire une
base de données à partir des données publiques de valeurs foncières
(DVF) du premier semestre 2020.
 
## Problème métier
Construire une base conforme au RGPD, exploitable pour des analyses de
marché immobilier (prix au m², dynamique des ventes par région/commune).
 
## Démarche
- Modélisation d'un schéma relationnel normalisé à 6 tables (Ventes,
  Biens, Commune, Departement, Region, table temporaire Nombre de pièces
  réintégrée dans Biens)
- Suppression systématique des données non conformes au RGPD (adresses
  exactes, identités des acheteurs)
- Création de clés dédiées (Id_bien après dédoublonnage par
  adresse/commune, Id_vente, Id_codedep_codecommu)
- 12 requêtes SQL de complexité croissante : jointures à 4 tables, CTE
  pour les proportions et taux d'évolution trimestriels, CASE WHEN pour
  la répartition par trimestre, HAVING pour filtrer les communes actives,
  pivot manuel via MAX(CASE WHEN...) pour comparer deux catégories
 
## Résultat
31 229 appartements vendus au premier semestre 2020 sur les 19 régions
couvertes. Départements au prix au m² le plus élevé identifiés, communes
les plus actives repérées (300+ ventes au premier trimestre pour
certaines communes d'Île-de-France). Différentiel de prix au m² calculé
entre appartements de 2 et 3 pièces, taux d'évolution des ventes entre
le 1er et le 2e trimestre 2020.
 
## Compétences démontrées
Modélisation de base de données relationnelle sous contrainte
réglementaire (RGPD), gestion de clés et dédoublonnage, requêtes SQL
avancées (CTE, pivot, fenêtrage temporel), restitution en comité de
projet.
 
## Outils
SQL, SQLite, DB Browser for SQLite
 
## Livrables dans ce dossier
- Compte-rendu de réunion avec les 12 requêtes SQL et captures de
  résultats (Annexe 3)
- Présentation (PPTX)
