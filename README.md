# Portfolio — Vincent Boutillier
### Data Analyst · Master 

> Ce repository rassemble les preuves de compétences acquises au fil des projets P3 à P13 du parcours Data Analyst : préparation et fiabilisation de données, analyse statistique, machine learning supervisé et non supervisé, data visualisation (Power BI), pipelines analytiques (dbt/Snowflake), et pilotage de projet augmenté par l'IA.

---

## Sommaire

1. [Comment lire ce portfolio](#comment-lire-ce-portfolio)
2. [Vue d'ensemble des projets](#vue-densemble-des-projets)
3. [Projets détaillés](#projets-détaillés)
4. [Compétences transverses démontrées](#compétences-transverses-démontrées)
5. [Stack technique](#stack-technique)

---

## Comment lire ce portfolio

Chaque projet répond à un besoin métier explicite formulé pour un client fictif (ONCFM, DWFA, La Poule Qui Chante, BottleNeck…). Pour chacun, ce portfolio indique : le problème posé, la méthode retenue et pourquoi, le résultat obtenu, et où trouver la preuve technique complète (notebook, dashboard, documentation).

Le projet **P13** occupe une place particulière : il ne s'agit pas d'un nouveau sujet, mais d'une **démarche critique et documentée d'amélioration** du P6, menée avec un usage encadré de l'IA (veille comparative, cahier des charges, POC, pilotage). C'est la preuve la plus complète de ma capacité à auditer, remettre en question et améliorer un livrable existant — voir [`P13-bottleneck-clustering/`](./P13-bottleneck-clustering/).

---

## Vue d'ensemble des projets

| # | Projet | Client fictif | Sujet | Compétences clés | Outils |
|---|---|---|---|---|---|
| P3 | Requêtez une base de données avec SQL | — | Interrogation d'une base de données relationnelle | Requêtes SQL | SQL |
| P4 | Étude de santé publique avec Python | — | Analyse de données de santé publique | Analyse statistique, nettoyage de données | Python |
| P5 | Base de données Immo avec SQL | — | Conception/exploitation d'une base de données immobilières | Modélisation de base de données, SQL | SQL |
| P6 | BottleNeck — Optimiser la gestion des données d'une boutique | BottleNeck (caviste en ligne) | Fusion multi-sources (ERP/Web/liaison), nettoyage, analyse univariée | Nettoyage de données, détection d'anomalies, statistiques descriptives | Python, pandas, matplotlib/plotly |
| P7 | Sanitoral — Suivi de portefeuille projets (PBI Sanitorial) | Sanitoral (PMO IT/Marketing) | Dashboard de pilotage : alertes coûts/délais/livrables, sécurité des données par rôle | Modélisation en étoile, DAX, sécurité au niveau ligne (RLS) | Power BI |
| P8 | Profil sociodémographique étudiants (Analyse Socio/Demo DBT Cloud) | OpenClassrooms | Pipeline analytique bout-en-bout jusqu'à un mart de données testé | Modélisation dbt, tests de données, ELT cloud | dbt Cloud, Snowflake |
| P9 | Ventes Librairie Python | — | Analyse des ventes d'une librairie | Analyse statistique, indicateurs de vente | Python |
| P10 | DWFA — Accès à l'eau potable (Eau Potable PBIX) | Drinking Water For All | Dashboard de priorisation de l'intervention par pays | Modélisation de données, storytelling géographique, accessibilité | Power BI |
| P11 | La Poule Qui Chante — Marchés export (Étude de Marché Python) | La Poule Qui Chante (volaille bio) | Segmentation de 137 pays pour cibler les marchés d'export prioritaires | ACP, CAH, K-Means, feature engineering | Python, scikit-learn |
| P12 | ONCFM — Détection de faux billets | ONCFM | Classification automatique de billets contrefaits + app de démo | ML supervisé/non supervisé, déploiement, packaging | Python, scikit-learn, Streamlit |
| P13 | BottleNeck — Segmentation augmentée par l'IA | BottleNeck | Amélioration critique du P6 : audit de données, clustering, veille, pilotage | Clustering non supervisé, audit critique, veille technologique, gestion de projet, usage encadré de l'IA | Python, scikit-learn, pandas |

*(P1 et P2 volontairement exclus du portfolio — non pertinents au regard du parcours présenté.)*

---

## Projets détaillés

### P13 — BottleNeck : segmentation augmentée par l'IA 

**Problème** : le P6 analysait le catalogue produit par produit et variable par variable — un constat, pas une décision. Comment regrouper automatiquement les produits en familles actionnables (assortiment, pricing, stock) ?

**Démarche** : audit critique de l'export du P6 → détection et correction à la source d'un bug de fusion pandas non identifié initialement (182 lignes corrompues sur 916) → comparaison de 2 jeux de variables et 2 algorithmes de clustering → arbitrage documenté entre performance statistique et valeur métier → 4 segments nommés et actionnables, dont un segment "stock dormant" invisible dans une analyse plus simple.

**Résultat** : segmentation de 689 produits en 4 familles, avec un segment de 32 produits à rotation de stock 6× supérieure à la moyenne, directement actionnable pour le déstockage.

**Preuves** :
- [`p6_extended.ipynb`](./P13-bottleneck-clustering/p6_extended.ipynb) — notebook POC exécuté de bout en bout
- [`documentation.md`](./P13-bottleneck-clustering/documentation.md) — cahier des charges, veille technologique sourcée et datée, traçabilité des essais IA, pilotage de projet (lots, backlog, planning, registre des risques)

---

### P12 — ONCFM : détection de faux billets

**Problème** : automatiser la détection de billets contrefaits à partir de 6 mesures géométriques.

**Démarche** : imputation des valeurs manquantes par régression linéaire (R²=0,546), comparaison de 4 modèles (régression logistique, K-Means, KNN, Random Forest) ; la régression logistique a été retenue en modèle final malgré une exactitude légèrement inférieure au KNN, pour sa stabilité, son interprétabilité et l'absence de dérive liée aux hyperparamètres — un choix documenté qui illustre qu'un score brut n'est pas le seul critère de décision en contexte métier.

**Résultat** : modèle déployé sous 3 formes (script Python, application Streamlit, app HTML client-side), validé sur le jeu de production officiel (5/5 prédictions correctes).

**Preuves** : notebook complet, script `predict_billets.py`, application Streamlit déployée, présentation 15 slides.

---

### P11 — La Poule Qui Chante : ciblage de marchés export

**Problème** : identifier les pays prioritaires pour l'export de volaille bio parmi 137 pays.

**Démarche** : ACP puis double clustering (CAH et K-Means comparés) sur 11 variables socio-économiques et agricoles ; identification automatisée du segment cible via un score de priorité normalisé, avec exclusion argumentée des micro-marchés (Samoa, Dominique) sur un critère de volume absolu malgré un taux d'import élevé.

**Résultat** : ciblage des pays du Golfe (Émirats, Koweït, Arabie Saoudite, Oman) comme marché prioritaire structurel.

**Preuves** : 2 notebooks (préparation + clustering), 20 slides de présentation, document de préparation à la soutenance.

---

### P10 — DWFA : priorisation de l'accès à l'eau potable

**Problème** : construire un dashboard identifiant les pays où l'accès à l'eau potable est le plus difficile, pour prioriser 3 axes d'intervention (création de service, modernisation, conseil).

**Démarche** : modélisation en étoile, résolution de plusieurs blocages réels de construction (paramètres régionaux/décimales, doublons de la Chine faussant la population mondiale de +1,5 milliard, synchronisation de filtres entre pages).

**Preuves** : dashboard Power BI, guide de construction pas-à-pas, thème de couleurs dédié, support de soutenance.

---

### P9 — Ventes Librairie Python

**Sujet** : analyse des ventes d'une librairie.

*Détails à compléter — ajouter ici : problème métier, démarche, résultat chiffré, lien vers le livrable.*

---

### P7 — Sanitoral : pilotage de portefeuille projets

**Problème** : donner à 3 profils utilisateurs (Directeur Général, Régional, Pays) une vue de pilotage des projets IT/Marketing en alerte (dépassement de coût, délai ou livrable de +15%).

**Démarche** : modélisation en étoile via une clé concaténée `Clé_Projet_Phase`, 6 mesures DAX, sécurité au niveau ligne (RLS) avec 3 rôles distincts basés sur `USERPRINCIPALNAME()`.

**Preuves** : dashboard 8 pages, Product Strategy Canvas, guide de construction.

---

### P8 — Profil sociodémographique des étudiants OpenClassrooms

**Problème** : construire un pipeline analytique fiable et testé pour produire un profil sociodémographique des étudiants.

**Démarche** : pipeline dbt Cloud + Snowflake, staging puis mart de données, 13 tests de données passants, harmonisation manuelle des régions INSEE, gestion d'une migration de compte en cours de projet (expiration du trial dbt Cloud).

**Preuves** : projet dbt complet, exports CSV, documentation du workflow.

---

### P6 — BottleNeck : analyse stock & ventes *(base du P13)*

**Problème** : fusionner 3 sources de données (ERP, site web, table de liaison) et produire une première analyse du catalogue.

**Démarche** : nettoyage, détection d'anomalies (stocks négatifs, doublons), analyse univariée du prix, du CA, des stocks et de la marge.

**Preuves** : voir le P13, qui reprend, audite et étend ce livrable.

---

### P3, P4, P5 — *à détailler*


---

## Compétences transverses démontrées

Ces indicateurs sont documentés en détail dans le [P13](./P13-bottleneck-clustering/documentation.md), qui sert de démonstration de référence pour la méthode ; les autres projets les illustrent aussi ponctuellement (colonne "Autres preuves").

| Compétence | Preuve principale (P13) | Autres preuves |
|---|---|---|
| Veille sélective, évaluée et justifiée (≥2 options comparées, critères explicites) | `documentation.md` §2.2 — KMeans vs Agglomératif, Pandera vs Great Expectations | P12 : régression logistique vs KNN vs Random Forest |
| Sources fiables, datées | `documentation.md` §2.5 | — |
| Critère de sobriété / impact dans la comparaison | `documentation.md` §2.2, colonne dédiée | — |
| Élément d'automatisation de la veille | `documentation.md` §2.4 — alertes GitHub Releases | — |
| Besoins de formation identifiés, y compris accessibilité | `documentation.md` §1.11 | P10 : dashboard conforme aux critères d'accessibilité de la grille d'évaluation |
| Cahier des charges structuré (état actuel, ressources, budget, périmètre, jalons) | `documentation.md` §1 | — |
| Gestion de projet (lots, backlog, planning, registre des risques) | `documentation.md` §4 | P7 (Sanitoral) : Product Strategy Canvas et user stories |
| POC documenté (hypothèses, tests, résultats, décisions) | `p6_extended.ipynb` + `documentation.md` §3 | P11 : arbitrage CAH vs K-Means documenté |
| Traçabilité de l'usage de l'IA (prompts, variantes, décisions gardées/écartées) | `documentation.md` §2.6 | — |

---

## Stack technique

**Langages & librairies** : Python (pandas, numpy, scikit-learn, matplotlib, seaborn, plotly), SQL

**Data engineering** : dbt Cloud, Snowflake

**Visualisation** : Power BI (DAX, RLS, modélisation en étoile), Streamlit

**Outils transverses** : Jupyter, Git/GitHub, assistance IA encadrée (Claude) pour la relecture critique et l'accélération du code — usage systématiquement documenté et validé, jamais appliqué sans vérification (voir méthode détaillée dans le P13)
