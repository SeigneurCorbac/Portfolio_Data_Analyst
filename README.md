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
| P3 | Requêtez une base de données avec SQL | Assureur habitation (fictif) | Modélisation et interrogation d'une base de contrats d'assurance habitation | Modélisation relationnelle, jointures, sous-requêtes, agrégations SQL | SQL (SQLite) |
| P4 | Étude de santé publique avec Python | ONG internationale (fictive) | Sous-nutrition mondiale : la faim est-elle un problème de production ou de répartition ? | Nettoyage multi-sources FAO, jointures, calculs d'indicateurs mondiaux | Python, pandas, matplotlib/seaborn |
| P5 | DATAImmo — Base de données foncières (Laplace Immo) | Laplace Immo (agence immobilière) | Modélisation RGPD-conforme et exploitation des données de valeurs foncières S1 2020 | Modélisation relationnelle multi-tables, conformité RGPD, requêtes SQL avancées (CTE, fenêtrage) | SQL (SQLite) |
| P6 | BottleNeck — Optimiser la gestion des données d'une boutique | BottleNeck (caviste en ligne) | Fusion multi-sources (ERP/Web/liaison), nettoyage, analyse univariée | Nettoyage de données, détection d'anomalies, statistiques descriptives | Python, pandas, matplotlib/plotly |
| P7 | Sanitoral — Suivi de portefeuille projets (PBI Sanitorial) | Sanitoral (PMO IT/Marketing) | Dashboard de pilotage : alertes coûts/délais/livrables, sécurité des données par rôle | Modélisation en étoile, DAX, sécurité au niveau ligne (RLS) | Power BI |
| P8 | Profil sociodémographique étudiants (Analyse Socio/Demo DBT Cloud) | OpenClassrooms | Pipeline analytique bout-en-bout jusqu'à un mart de données testé | Modélisation dbt, tests de données, ELT cloud | dbt Cloud, Snowflake |
| P9 | Ventes Librairie Python | Librairie en ligne (fictive) | Analyse des ventes, du profil client et des habitudes d'achat | Nettoyage multi-sources, tests statistiques (Khi², Spearman, Kruskal-Wallis), indice de Gini | Python, pandas, scipy |
| P10 | DWFA — Accès à l'eau potable (Eau Potable PBIX) | Drinking Water For All | Dashboard de priorisation de l'intervention par pays | Modélisation de données, storytelling géographique, accessibilité | Power BI |
| P11 | La Poule Qui Chante — Marchés export (Étude de Marché Python) | La Poule Qui Chante (volaille bio) | Segmentation de 137 pays pour cibler les marchés d'export prioritaires | ACP, CAH, K-Means, feature engineering | Python, scikit-learn |
| P12 | ONCFM — Détection de faux billets | ONCFM | Classification automatique de billets contrefaits + app de démo | ML supervisé/non supervisé, déploiement, packaging | Python, scikit-learn, Streamlit |
| P13 | BottleNeck — Segmentation augmentée par l'IA | BottleNeck | Amélioration critique du P6 : audit de données, clustering, veille, pilotage | Clustering non supervisé, audit critique, veille technologique, gestion de projet, usage encadré de l'IA | Python, scikit-learn, pandas |

*(P1 et P2 volontairement exclus du portfolio — non pertinents au regard du parcours présenté.)*

---

## Projets détaillés

### P13 — BottleNeck : segmentation augmentée par l'IA *(projet phare)*

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

**Problème** : comprendre le profil client et les habitudes d'achat d'une librairie en ligne à partir de 3 sources (clients, produits, transactions), pour identifier des leviers business exploitables.

**Démarche** : fusion des 3 fichiers avec jointure externe, isolement de 21 clients sans achat et 21 produits jamais vendus (exclus des statistiques pour ne pas fausser les résultats). Analyse du chiffre d'affaires (courbe mensuelle lissée par moyenne mobile 3 mois, répartition par catégorie), courbe de Lorenz et indice de Gini pour mesurer la concentration du CA. Série de tests statistiques avec justification systématique du choix de méthode : test du Khi² pour l'indépendance genre/catégorie, corrélations de Spearman (plutôt que Pearson, les distributions n'étant pas gaussiennes) entre âge et montant/fréquence/panier moyen, et test de Kruskal-Wallis — alternative non paramétrique à l'ANOVA — après qu'un test de Shapiro-Wilk a confirmé la non-normalité des distributions d'âge par catégorie.

**Résultat** : indice de Gini de 0,44 (4 clients BtoB représentant à eux seuls ~7,3% du CA total) ; association significative entre genre et catégorie de livres achetés (χ²=22,67, p=0,000012) ; l'âge s'est révélé un prédicteur faible des habitudes d'achat (corrélations de Spearman toutes sous 0,33 en valeur absolue), amenant à privilégier le genre comme critère de segmentation pour les recommandations produit plutôt que l'âge.

**Compétences démontrées** : nettoyage multi-sources, choix et justification de tests statistiques (paramétriques vs non paramétriques), mesure de concentration économique (Gini/Lorenz), traduction de résultats statistiques en implications business.

**Outils** : Python, pandas, matplotlib, scipy (tests statistiques)

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

### P3 — Requêtez une base de données avec SQL

**Problème** : modéliser et interroger une base de contrats d'assurance habitation pour répondre à des questions métier variées (répartition géographique, tarification, profils de biens assurés).

**Démarche** : conception d'un schéma relationnel à 2 tables (`Contrat` : 14 colonnes — type de local, occupation, formule, valeur déclarée, cotisation… ; `Region` : 8 colonnes — hiérarchie académie/région/département/commune), reliées par une clé étrangère sur le code commune. Base construite et interrogée sous SQLite (DB Browser). 12 requêtes progressives, des filtres simples aux agrégations avec jointure : filtrage par commune et département, sous-requête `IN` pour retrouver un code commune par son nom, `COUNT`/`AVG`/`GROUP BY` avec jointure, catégorisation par tranches via `CASE WHEN`, classement `ORDER BY ... LIMIT`, filtrage de groupes via `HAVING`.

**Résultat** : base de 69 251 lignes chargées avec succès ; réparation de la distribution des contrats par tranche de valeur déclarée (22 720 contrats entre 0 et 25 000€, seulement 104 au-dessus de 100 000€) ; Île-de-France identifiée comme région la plus représentée (14 177 contrats) ; Paris se distingue avec la cotisation mensuelle moyenne la plus élevée de France (36,40€, contre une moyenne nationale de 19,33€) ; 20 communes dépassant les 150 contrats identifiées, avec plusieurs arrondissements parisiens en tête.

**Compétences démontrées** : modélisation de base de données relationnelle, écriture de requêtes SQL (jointures, sous-requêtes, agrégations, `HAVING`, `CASE WHEN`), formulation de questions métier en requêtes exploitables.

**Outils** : SQL, SQLite, DB Browser for SQLite

---

### P4 — Étude de santé publique avec Python

**Problème** : la production alimentaire mondiale suffit-elle à nourrir la planète, ou la sous-nutrition est-elle avant tout un problème de répartition ? Où concentrer les efforts (pays, produits, types de perte) pour un impact maximal ?

**Démarche** : fusion et nettoyage de 4 sources FAO (population, disponibilité alimentaire, aide alimentaire, sous-nutrition), harmonisation des unités (milliers de tonnes → kg, conversion des plages d'années en année médiane pour la jointure), calcul de la capacité de nourrissage théorique mondiale à partir des calories disponibles, décomposition de la disponibilité intérieure par usage (nourriture, alimentation animale, pertes, traitement, semences), identification des pays les plus touchés par la sous-nutrition et des principaux bénéficiaires de l'aide alimentaire, étude de cas sur le manioc thaïlandais (production vs exportation).

**Résultat** : la production mondiale de calories permettrait théoriquement de nourrir 126% de la population réelle (et encore 104% en ne comptant que les végétaux) — la sous-nutrition (535,7 millions de personnes, 7,1% de la population mondiale en 2017) est donc structurellement un problème de répartition et d'accès, pas de volume produit. Seulement 49,5% de la disponibilité intérieure mondiale est utilisée comme nourriture humaine directe (13,2% part à l'alimentation animale). Cas du manioc thaïlandais : 83,4% de la production est exportée contre seulement 2,9% consommée localement comme nourriture, illustrant une logique d'exportation déconnectée des besoins nutritionnels locaux.

**Compétences démontrées** : nettoyage et harmonisation de données multi-sources (unités, granularité temporelle), calcul d'indicateurs à l'échelle mondiale, restitution de résultats contre-intuitifs de façon claire (excédent de production mais persistance de la faim).

**Outils** : Python, pandas, matplotlib, seaborn

---

### P5 — DATAImmo : base de données de valeurs foncières (Laplace Immo)

**Problème** : construire, pour l'agence Laplace Immo, une base de données conforme au RGPD à partir des données publiques de valeurs foncières (DVF) du premier semestre 2020, exploitable pour des analyses de marché immobilier.

**Démarche** : modélisation d'un schéma relationnel normalisé à 6 tables (Ventes, Biens, Commune, Departement, Region, table temporaire Nombre de pièces réintégrée dans Biens), avec suppression systématique des données non conformes au RGPD (adresses exactes, identités des acheteurs). Création de clés dédiées (`Id_bien` après dédoublonnage par adresse/commune, `Id_vente`, `Id_codedep_codecommu`). Rédaction de 12 requêtes SQL de complexité croissante : jointures à 4 tables, CTE (Common Table Expressions) pour les proportions et taux d'évolution trimestriels, `CASE WHEN` pour la répartition par trimestre, `HAVING` pour filtrer les communes actives, pivot manuel via `MAX(CASE WHEN...)` pour comparer deux catégories côte à côte.

**Résultat** : 31 229 appartements vendus au premier semestre 2020 sur l'ensemble des 19 régions couvertes. Identification des départements au prix au m² le plus élevé et des communes les plus actives (jusqu'à plus de 300 ventes sur le seul premier trimestre pour certaines communes d'Île-de-France). Calcul du différentiel de prix au m² entre appartements de 2 et 3 pièces, et du taux d'évolution des ventes entre le premier et le second trimestre 2020.

**Compétences démontrées** : modélisation de base de données relationnelle sous contrainte réglementaire (RGPD), gestion de clés et dédoublonnage, requêtes SQL avancées (CTE, pivot, fenêtrage temporel), restitution en comité de projet (compte-rendu de réunion, présentation).

**Outils** : SQL, SQLite, DB Browser for SQLite

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
