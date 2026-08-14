# Portfolio — Vincent Boutillier
### Data Analyst · Master OpenClassrooms

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

Chaque projet est raconté selon la même trame : **contexte** (qui, pourquoi) → **besoin métier** (la question à résoudre) → **démarche** (méthode et choix) → **résultats** (ce qui a été obtenu) → **impact** (ce que ça change pour le métier). Les preuves techniques complètes (notebook, dashboard, documentation) sont liées à la fin de chaque fiche.

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

**Contexte** : le P6 avait produit une analyse du catalogue BottleNeck variable par variable (prix, ventes, stock, marge pris isolément) — un constat, jamais une vue croisée.

**Besoin métier** : les équipes assortiment, pricing et gestion de stock ont besoin de familles de produits actionnables, pas de statistiques séparées. Comment regrouper automatiquement les produits en segments cohérents pour orienter ces décisions ?

**Démarche** : audit critique de l'export du P6 → détection et correction à la source d'un bug de fusion pandas non identifié initialement (182 lignes corrompues sur 916) → veille comparative sur les méthodes de clustering et les outils de qualité de données (voir intégration ci-dessous) → comparaison de 2 jeux de variables et 2 algorithmes → arbitrage documenté entre performance statistique et valeur métier.

**Intégration des résultats de veille** : le choix de KMeans plutôt que le clustering agglomératif, et de Pandera plutôt que Great Expectations pour une future industrialisation, découle directement du tableau de veille sourcé et daté (`documentation.md` §2) — chaque option a été évaluée sur la qualité du résultat, la sobriété/impact calcul, et la reproductibilité avant décision.

**Résultats** : segmentation de 689 produits en 4 familles nommées, dont un segment de 32 produits à rotation de stock 6× supérieure à la moyenne, invisible dans une analyse plus simple.

**Impact** : le segment "stock dormant" rend visible un capital immobilisé jusque-là invisible en lecture univariée — recommandation directe de déstockage prioritaire, plus un mini-plan de formation pour que les équipes métier exploitent le résultat sans compétence data science.

**Preuves** :
- [`p6_extended.ipynb`](./P13-bottleneck-clustering/p6_extended.ipynb) — notebook POC exécuté de bout en bout
- [`documentation.md`](./P13-bottleneck-clustering/documentation.md) — cahier des charges, veille technologique sourcée et datée, traçabilité des essais IA, pilotage de projet (lots, backlog, planning, registre des risques)

---

### P12 — ONCFM : détection de faux billets

**Contexte** : l'Organisation nationale de lutte contre le faux-monnayage (ONCFM) doit fiabiliser sa détection de billets contrefaits.

**Besoin métier** : automatiser la détection à partir de 6 mesures géométriques, sur un jeu de 1500 billets pré-vérifiés.

**Démarche** : imputation des valeurs manquantes par régression linéaire (R²=0,546), comparaison de 4 modèles (régression logistique, K-Means, KNN, Random Forest) ; la régression logistique a été retenue en modèle final malgré une exactitude légèrement inférieure au KNN, pour sa stabilité, son interprétabilité et l'absence de dérive liée aux hyperparamètres — un choix documenté qui illustre qu'un score brut n'est pas le seul critère de décision en contexte métier.

**Résultats** : modèle déployé sous 3 formes (script Python, application Streamlit, app HTML client-side), validé sur le jeu de production officiel (5/5 prédictions correctes).

**Impact** : un outil de détection utilisable en routine, dont le choix de modèle est défendable devant un non-spécialiste (interprétabilité) plutôt qu'un modèle boîte noire plus précis de quelques dixièmes de point.

**Preuves** : notebook complet, script `predict_billets.py`, application Streamlit déployée, présentation 15 slides.

---

### P11 — La Poule Qui Chante : ciblage de marchés export

**Contexte** : entreprise de volaille bio cherchant à orienter sa stratégie d'export.

**Besoin métier** : parmi 137 pays, lesquels prioriser pour l'export de poulet biologique ?

**Démarche** : ACP puis double clustering (CAH et K-Means comparés) sur 11 variables socio-économiques et agricoles ; identification automatisée du segment cible via un score de priorité normalisé, avec exclusion argumentée des micro-marchés (Samoa, Dominique) sur un critère de volume absolu malgré un taux d'import élevé.

**Résultats** : ciblage des pays du Golfe (Émirats, Koweït, Arabie Saoudite, Oman) comme marché prioritaire structurel.

**Impact** : une liste de marchés priorisée et défendable (pas une intuition), avec les cas limites explicitement tranchés plutôt que laissés à l'appréciation du lecteur.

**Preuves** : 2 notebooks (préparation + clustering), 20 slides de présentation, document de préparation à la soutenance.

---

### P10 — DWFA : priorisation de l'accès à l'eau potable

**Contexte** : Drinking Water For All (DWFA), organisation intervenant sur l'accès à l'eau potable dans le monde.

**Besoin métier** : identifier les pays où l'accès à l'eau potable est le plus difficile, pour prioriser 3 axes d'intervention (création de service, modernisation, conseil).

**Démarche** : modélisation en étoile, résolution de plusieurs blocages réels de construction (paramètres régionaux/décimales, doublons de la Chine faussant la population mondiale de +1,5 milliard, synchronisation de filtres entre pages).

**Résultats** : dashboard Power BI multi-pages conforme à la grille d'évaluation, avec vues temporelles et géographiques.

**Impact** : un outil de priorisation directement utilisable pour l'allocation des interventions terrain, accessible (contraste, alternatives textuelles) pour tous les utilisateurs de l'ONG.

**Preuves** : dashboard Power BI, guide de construction pas-à-pas, thème de couleurs dédié, support de soutenance.

---

### P9 — Ventes Librairie Python

**Contexte** : librairie en ligne cherchant à mieux comprendre sa clientèle.

**Besoin métier** : comprendre le profil client et les habitudes d'achat à partir de 3 sources (clients, produits, transactions), pour identifier des leviers business exploitables.

**Démarche** : fusion des 3 fichiers avec jointure externe, isolement de 21 clients sans achat et 21 produits jamais vendus (exclus des statistiques pour ne pas fausser les résultats). Analyse du chiffre d'affaires (courbe mensuelle lissée par moyenne mobile 3 mois, répartition par catégorie), courbe de Lorenz et indice de Gini pour mesurer la concentration du CA. Série de tests statistiques avec justification systématique du choix de méthode : test du Khi² pour l'indépendance genre/catégorie, corrélations de Spearman (plutôt que Pearson, les distributions n'étant pas gaussiennes) entre âge et montant/fréquence/panier moyen, et test de Kruskal-Wallis — alternative non paramétrique à l'ANOVA — après qu'un test de Shapiro-Wilk a confirmé la non-normalité des distributions d'âge par catégorie.

**Résultats** : indice de Gini de 0,44 (4 clients BtoB représentant à eux seuls ~7,3% du CA total) ; association significative entre genre et catégorie de livres achetés (χ²=22,67, p=0,000012) ; l'âge s'est révélé un prédicteur faible des habitudes d'achat (corrélations de Spearman toutes sous 0,33 en valeur absolue), amenant à privilégier le genre comme critère de segmentation pour les recommandations produit plutôt que l'âge.

**Impact** : un critère de segmentation (genre) validé statistiquement plutôt que choisi par défaut (âge), évitant d'investir dans des recommandations basées sur un critère faiblement prédictif.

**Compétences démontrées** : nettoyage multi-sources, choix et justification de tests statistiques (paramétriques vs non paramétriques), mesure de concentration économique (Gini/Lorenz), traduction de résultats statistiques en implications business.

**Outils** : Python, pandas, matplotlib, scipy (tests statistiques)

---

### P8 — Profil sociodémographique des étudiants OpenClassrooms

**Contexte** : OpenClassrooms souhaite mieux connaître le profil de ses étudiants Data Analyst.

**Besoin métier** : construire un pipeline analytique fiable et testé pour produire ce profil sociodémographique (âge, région, genre).

**Démarche** : pipeline dbt Cloud + Snowflake, staging puis mart de données, 13 tests de données passants, harmonisation manuelle des régions INSEE, gestion d'une migration de compte en cours de projet (expiration du trial dbt Cloud).

**Résultats** : mart de données en production sur Snowflake, entièrement testé, exportable en CSV pour analyse.

**Impact** : une base fiable et reproductible pour toute analyse future du profil étudiant, plutôt qu'un export ponctuel à refaire à chaque besoin.

**Preuves** : projet dbt complet, exports CSV, documentation du workflow.

---

### P7 — Sanitoral : pilotage de portefeuille projets

**Contexte** : Sanitoral, PMO (Project Management Office) suivant des projets IT et Marketing.

**Besoin métier** : donner à 3 profils utilisateurs (Directeur Général, Régional, Pays) une vue de pilotage des projets en alerte (dépassement de coût, délai ou livrable de +15%), chacun limité à son périmètre de données.

**Démarche** : modélisation en étoile via une clé concaténée `Clé_Projet_Phase`, 6 mesures DAX, sécurité au niveau ligne (RLS) avec 3 rôles distincts basés sur `USERPRINCIPALNAME()`.

**Résultats** : dashboard 8 pages conforme au Product Strategy Canvas défini en amont.

**Impact** : chaque profil voit uniquement ce qui le concerne (sécurité des données), sans dashboard séparé à maintenir par rôle.

**Preuves** : dashboard 8 pages, Product Strategy Canvas, guide de construction.

---

### P6 — BottleNeck : analyse stock & ventes *(base du P13)*

**Contexte** : BottleNeck, caviste en ligne fictif — premier contact avec ce jeu de données.

**Besoin métier** : fusionner 3 sources de données (ERP, site web, table de liaison) et produire une première analyse du catalogue.

**Démarche** : nettoyage, détection d'anomalies (stocks négatifs, doublons), analyse univariée du prix, du CA, des stocks et de la marge.

**Résultats** : table consolidée exploitable, base de travail pour le P13.

**Impact** : voir le P13 — c'est justement l'absence de vue croisée de ce livrable qui motive toute la démarche du P13.

**Preuves** : voir le P13, qui reprend, audite et étend ce livrable.

---

### P3 — Requêtez une base de données avec SQL

**Contexte** : assureur habitation (fictif) souhaitant exploiter sa base de contrats.

**Besoin métier** : répondre à des questions métier variées à partir de la base (répartition géographique, tarification, profils de biens assurés).

**Démarche** : conception d'un schéma relationnel à 2 tables (`Contrat` : 14 colonnes — type de local, occupation, formule, valeur déclarée, cotisation… ; `Region` : 8 colonnes — hiérarchie académie/région/département/commune), reliées par une clé étrangère sur le code commune. Base construite et interrogée sous SQLite (DB Browser). 12 requêtes progressives, des filtres simples aux agrégations avec jointure : filtrage par commune et département, sous-requête `IN` pour retrouver un code commune par son nom, `COUNT`/`AVG`/`GROUP BY` avec jointure, catégorisation par tranches via `CASE WHEN`, classement `ORDER BY ... LIMIT`, filtrage de groupes via `HAVING`.

**Résultats** : base de 69 251 lignes chargées avec succès ; répartition des contrats par tranche de valeur déclarée (22 720 contrats entre 0 et 25 000€, seulement 104 au-dessus de 100 000€) ; Île-de-France identifiée comme région la plus représentée (14 177 contrats) ; Paris se distingue avec la cotisation mensuelle moyenne la plus élevée de France (36,40€, contre une moyenne nationale de 19,33€) ; 20 communes dépassant les 150 contrats identifiées.

**Impact** : une base interrogeable directement par l'équipe tarification, sans dépendre d'exports manuels répétés.

**Compétences démontrées** : modélisation de base de données relationnelle, écriture de requêtes SQL (jointures, sous-requêtes, agrégations, `HAVING`, `CASE WHEN`), formulation de questions métier en requêtes exploitables.

**Outils** : SQL, SQLite, DB Browser for SQLite

---

### P4 — Étude de santé publique avec Python

**Contexte** : organisation internationale s'intéressant à la sous-nutrition mondiale.

**Besoin métier** : la production alimentaire mondiale suffit-elle à nourrir la planète, ou la sous-nutrition est-elle avant tout un problème de répartition ? Où concentrer les efforts pour un impact maximal ?

**Démarche** : fusion et nettoyage de 4 sources FAO (population, disponibilité alimentaire, aide alimentaire, sous-nutrition), harmonisation des unités (milliers de tonnes → kg, conversion des plages d'années en année médiane pour la jointure), calcul de la capacité de nourrissage théorique mondiale à partir des calories disponibles, décomposition de la disponibilité intérieure par usage, identification des pays les plus touchés et des principaux bénéficiaires de l'aide alimentaire, étude de cas sur le manioc thaïlandais (production vs exportation).

**Résultats** : la production mondiale de calories permettrait théoriquement de nourrir 126% de la population réelle (104% en ne comptant que les végétaux) — la sous-nutrition (535,7 millions de personnes, 7,1% de la population mondiale en 2017) est donc structurellement un problème de répartition, pas de volume produit. Cas du manioc thaïlandais : 83,4% de la production est exportée contre 2,9% seulement consommée localement comme nourriture.

**Impact** : un résultat contre-intuitif qui réoriente la question posée — pas "produire plus" mais "mieux répartir et rendre accessible" — directement utile pour cibler une politique d'aide alimentaire.

**Compétences démontrées** : nettoyage et harmonisation de données multi-sources (unités, granularité temporelle), calcul d'indicateurs à l'échelle mondiale, restitution de résultats contre-intuitifs de façon claire.

**Outils** : Python, pandas, matplotlib, seaborn

---

### P5 — DATAImmo : base de données de valeurs foncières (Laplace Immo)

**Contexte** : Laplace Immo, agence immobilière, souhaite exploiter les données publiques de valeurs foncières.

**Besoin métier** : construire une base conforme au RGPD à partir des données DVF du premier semestre 2020, exploitable pour des analyses de marché immobilier.

**Démarche** : modélisation d'un schéma relationnel normalisé à 6 tables (Ventes, Biens, Commune, Departement, Region, table temporaire Nombre de pièces réintégrée dans Biens), avec suppression systématique des données non conformes au RGPD (adresses exactes, identités des acheteurs). Création de clés dédiées (`Id_bien` après dédoublonnage par adresse/commune, `Id_vente`, `Id_codedep_codecommu`). 12 requêtes SQL de complexité croissante : jointures à 4 tables, CTE pour les proportions et taux d'évolution trimestriels, `CASE WHEN`, `HAVING`, pivot manuel via `MAX(CASE WHEN...)`.

**Résultats** : 31 229 appartements vendus au premier semestre 2020 sur les 19 régions couvertes. Départements au prix au m² le plus élevé identifiés, communes les plus actives repérées (300+ ventes au premier trimestre pour certaines communes d'Île-de-France).

**Impact** : une base RGPD-conforme réutilisable pour toute étude de marché future de l'agence, sans risque de conservation de données personnelles non nécessaires.

**Compétences démontrées** : modélisation de base de données relationnelle sous contrainte réglementaire (RGPD), gestion de clés et dédoublonnage, requêtes SQL avancées (CTE, pivot, fenêtrage temporel), restitution en comité de projet.

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
