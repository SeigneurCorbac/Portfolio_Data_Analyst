# P3 — Requêtez une base de données avec SQL
 
## Contexte
Base de données de contrats d'assurance habitation (assureur fictif),
modélisée et interrogée sous SQLite.
 
## Problème métier
Répondre à des questions métier variées à partir de la base : répartition
géographique des contrats, tarification moyenne, profils de biens
assurés.
 
## Démarche
- Conception d'un schéma relationnel à 2 tables : Contrat (14 colonnes :
  type de local, occupation, formule, valeur déclarée, cotisation...) et
  Region (8 colonnes : hiérarchie académie/région/département/commune),
  reliées par une clé étrangère sur le code commune
- Base construite et interrogée sous SQLite (DB Browser)
- 12 requêtes progressives : filtres simples, sous-requête IN, jointures
  avec agrégation (COUNT/AVG/GROUP BY), catégorisation par tranches via
  CASE WHEN, classement ORDER BY + LIMIT, filtrage de groupes via HAVING
 
## Résultat
Base de 69 251 lignes chargées avec succès. Répartition des contrats par
tranche de valeur déclarée (22 720 contrats entre 0 et 25 000€, 104
au-dessus de 100 000€). Île-de-France identifiée comme région la plus
représentée (14 177 contrats). Paris se distingue avec la cotisation
mensuelle moyenne la plus élevée de France (36,40€, contre une moyenne
nationale de 19,33€). 20 communes dépassant les 150 contrats identifiées.
 
## Compétences démontrées
Modélisation de base de données relationnelle, écriture de requêtes SQL
(jointures, sous-requêtes, agrégations, HAVING, CASE WHEN), traduction
de questions métier en requêtes exploitables.
 
## Outils
SQL, SQLite, DB Browser for SQLite
 
## Livrables dans ce dossier
- Script SQL de création des tables
- Captures d'écran de la structure de la base
- Requêtes et résultats (trame remplie + requêtes complémentaires)
