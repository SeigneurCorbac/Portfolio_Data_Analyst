# P8 — Profil sociodémographique des étudiants OpenClassrooms
 
## Contexte
Construire un pipeline analytique fiable pour produire un profil
sociodémographique des étudiants du parcours.
 
## Problème métier
Fournir un mart de données testé et documenté, exploitable pour analyser
la démographie des étudiants (âge, région, genre).
 
## Démarche
- Pipeline dbt Cloud + Snowflake, de deux tables brutes jusqu'à un mart
  final (mart_profil_socio_demo.sql)
- 13 tests de données passants
- Harmonisation manuelle des noms de région INSEE
- Décisions documentées : COALESCE pour les valeurs de genre manquantes,
  conservation des USER_ID dupliqués comme inscriptions multi-années
  légitimes, jointure INNER pour l'indice de représentation
- Gestion d'un imprévu en cours de projet : migration complète de compte
  suite à l'expiration du trial dbt Cloud
 
## Résultat
Mart de données en production sur Snowflake, entièrement testé,
exportable en CSV pour analyse.
 
## Compétences démontrées
Modélisation dbt (staging → mart), tests de données, ELT cloud,
résolution d'incident (migration de compte), documentation de pipeline.
 
## Outils
dbt Cloud, Snowflake, SQL
 
## Livrables suggérés dans ce dossier
- Exports CSV du mart de données
- Documentation du workflow (Word ou Markdown)
- Présentation (PPTX, 15 slides)
