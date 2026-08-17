# P13 — Documentation de la démarche
### Amélioration du livrable P6 par une approche de Machine Learning non supervisé, avec usage encadré de l'IA

> **Projet** : Segmentation automatisée du catalogue BottleNeck par clustering
> **Livrable d'origine** : Notebook P6 — Analyse du stock et des ventes (nettoyage ERP/Web/liaison + analyse univariée)
> **Notebook POC associé** : `p6_extended.ipynb`

---

## Sommaire

1. Cahier des charges fonctionnel
   1.1 Contexte et état actuel · 1.2 Parties prenantes · 1.3 Objectifs & enjeux · 1.4 Problématique métier reformulée · 1.5 Éléments prioritaires · 1.6 Périmètre · 1.7 Contraintes · 1.8 Ressources et budget · 1.9 Livrables et jalons · 1.10 Critères de réussite · 1.11 Mini-plan de formation
2. Veille métier et technologique
3. Démarche : hypothèses, tests, résultats, décisions
4. Organisation et pilotage du projet
5. Synthèse recruteur / client

---

## 1. Cahier des charges fonctionnel

### 1.1 Contexte et état actuel

Le P6 fusionne trois sources (ERP, site web, table de liaison) puis passe en revue chaque variable séparément : prix, chiffre d'affaires, quantités vendues, stock, marge. Le notebook obtenu se lit bien mais reste une juxtaposition de constats indépendants : rien n'y indique explicitement que tel groupe de produits se comporte de la même façon sur l'ensemble de ces axes à la fois.

L'environnement est **complexe et évolutif** : le catalogue de BottleNeck change en continu (nouvelles références, arrêts de vente, variations de stock), les données proviennent de trois systèmes distincts (ERP, site web, table de liaison) dont la synchronisation n'est pas garantie — le bug de fusion détecté en §3.1 en est la preuve concrète — et les usages attendus (assortiment, pricing, stock) ont des horizons de décision différents. Le projet doit donc produire un résultat robuste à cette instabilité, pas une photographie figée à usage unique.

### 1.2 Parties prenantes et rôles

| Partie prenante | Rôle vis-à-vis du projet |
|---|---|
| Équipe assortiment | Consommatrice du résultat : utilise les segments pour décider quels produits maintenir, renforcer ou retirer du catalogue |
| Équipe pricing | Consommatrice du résultat : ajuste les stratégies tarifaires par segment (ex. Premium vs Moteur de CA) |
| Équipe gestion de stock | Consommatrice prioritaire : agit directement sur le segment "Stock dormant" (déstockage) |
| Auteur du projet (moi) | Responsable de la fiabilité de l'analyse : audit des données, choix méthodologiques, validation des décisions assistées par l'IA |
| Formateur/évaluateur P13 | Valide la démarche critique et documentée ; n'est pas un utilisateur final du résultat métier |

Le P6 répond à un besoin de **constat** (« quel est l'état du catalogue ? ») ; le P13 doit répondre à un besoin de **décision** (« comment regrouper les produits pour agir dessus ? »).

### 1.3 Objectifs & enjeux

**Objectif** : livrer une segmentation du catalogue directement exploitable par les équipes métier, sans expertise data science requise pour l'interpréter.

**Enjeux** :
- **Enjeu business** : les produits à rotation de stock anormale immobilisent du capital sans que cela soit visible dans une lecture univariée du P6 — un enjeu direct de trésorerie.
- **Enjeu de fiabilité** : la donnée source contient une anomalie non détectée en P6 (§3.1) ; le projet doit démontrer qu'une segmentation n'est fiable que si l'audit de données qui la précède l'est aussi.
- **Enjeu d'adoption** : un résultat que les équipes non techniques ne comprennent pas ou n'utilisent pas n'a pas de valeur — d'où le mini-plan de formation (§1.11).

### 1.4 Problématique métier reformulée

> *« Comment dépasser une lecture indicateur par indicateur du catalogue BottleNeck pour faire émerger, à partir des données déjà disponibles (prix, ventes, ancienneté, rotation de stock), des groupes de produits cohérents et exploitables pour les décisions d'assortiment, de pricing et de gestion de stock ? »*

L'approche passe d'une lecture variable par variable à une **segmentation multivariée et data-driven** : ce n'est plus l'analyste qui fixe des seuils a priori sur chaque variable, c'est l'algorithme qui révèle des groupes cohérents, l'analyste se chargeant de les interpréter, les nommer et en tirer des recommandations.

### 1.5 Éléments prioritaires

1. **Priorité 1 — Fiabiliser la donnée avant tout calcul** : sans audit, tout résultat de clustering serait construit sur des lignes corrompues (cf. §3.1). Non négociable, traité en premier.
2. **Priorité 2 — Isoler les invendus** : condition pour que le clustering ne mélange pas un état qualitatif (jamais vendu) avec un continuum de comportements de vente.
3. **Priorité 3 — Comparer au moins 2 approches de segmentation** (nombre d'axes, algorithmes) plutôt que de figer un seul choix a priori, pour pouvoir justifier la décision finale.
4. **Priorité 4 — Rendre le résultat actionnable** : nommer les segments et proposer une recommandation par segment, condition de valeur pour le métier.
5. *Priorité réalisée en cours d'itération* : la re-fusion des données à la source a finalement pu être menée (fichiers sources obtenus en cours de projet) — voir §3.1. Reste non traitée : l'industrialisation (Pandera).

### 1.6 Périmètre

| Traité | Non traité |
|---|---|
| Segmenter les produits actuellement commercialisés, c'est-à-dire ayant enregistré au moins une vente | Anticiper les ventes futures (les données disponibles sont une photo à un instant T, pas un historique daté exploitable pour une série temporelle) |
| Variables : prix, ventes cumulées, ancienneté de la fiche, rotation de stock | Recommandation produit / personnalisation client |
| Isolement des invendus par règle métier avant clustering | |
| Audit critique de l'export P6 (détection d'anomalies non vues en P6) | |
| **Correction du bug de fusion à la source** (refusion depuis `erp.xlsx`/`web.xlsx`/`liaison.xlsx`) | |
| Correction de l'anomalie `purchase_price` > `price` sur `product_id` 4355 | Signalée mais non corrigée (hors périmètre P13) |

### 1.7 Contraintes

- **Données** : export `df_final.xlsx` du P6, snapshot figé → forecasting exclu d'emblée.
- **Qualité** : héritage d'anomalies du P6, dont une non détectée à l'époque (voir §3.1) — audit obligatoire avant modélisation.
- **Volumétrie** : 689 produits en cœur de catalogue après nettoyage → faible volume, résultats à interpréter comme un **POC**, non déployable en l'état.
- **Reproductibilité** : résultats stables d'une exécution à l'autre (graine fixée, date d'ancrage figée sur la donnée et non sur la date d'exécution).
- **Outillage** : Python / pandas / scikit-learn, notebook Jupyter.
- **Contrainte externe** : les données sources (ERP, web) sont des exports figés d'un instant T, hors du contrôle direct de l'analyste — toute évolution du système d'information de BottleNeck (changement de structure ERP, migration de plateforme e-commerce) casserait le pipeline sans préavis. C'est un argument supplémentaire en faveur de l'industrialisation (validation Pandera, §2.2) pour détecter ce genre de rupture automatiquement plutôt que silencieusement.

### 1.8 Ressources et budget

Projet mené en solo (étudiant), sans budget financier dédié — le "coût" se lit en temps et en outillage.

| Ressource | Nature | Coût |
|---|---|---|
| Temps analyste | 1 personne, ~5 jours cumulés (cadrage → restitution, cf. planning §4.3) | Temps de formation, non facturé |
| Outillage logiciel | Python, pandas, scikit-learn, Jupyter — tous open source | 0€ |
| Assistance IA (Claude) | Relecture critique, aide au code, comparaison de méthodes — usage documenté en §2.6 | Inclus dans l'abonnement outil existant |
| Données | Export `df_final.xlsx` déjà produit par le P6 — pas de collecte supplémentaire | 0€ |
| Infrastructure de calcul | Notebook local, volumétrie faible (689 lignes) — aucun besoin de calcul distribué ou cloud | 0€ |

**Budget non extensible à ce stade** : toute extension (re-fusion à la source, industrialisation Pandera, recalcul périodique automatisé) nécessiterait un arbitrage de temps supplémentaire, non chiffré ici faute de contexte organisationnel réel (projet pédagogique).

### 1.9 Livrables et jalons

| Livrable | Jalon associé |
|---|---|
| Cahier des charges + veille (ce document, §1-2) | J1 — Cadrage validé |
| Données auditées et nettoyées (`coeur`, 689 produits) | J2 — Données auditées |
| Segmentation variante A (baseline) | J3 — Modèle v1 |
| Segmentation variante B (k=4) + arbitrage documenté | J4 — Modèle v2 |
| Notebook `p6_extended.ipynb` exécuté + documentation complète | J5 — Restitution |

*(Détail du planning et des dépendances entre tâches : §4.2 et §4.3.)*

### 1.10 Critères de réussite (critères d'acceptation)

| Niveau | Critère | Cible |
|---|---|---|
| **Data** | Aucune valeur manquante / dupliquée frauduleuse sur les variables de clustering | 0 NaN sur les features, anomalie de fusion isolée |
| **Data** | Anomalies métier isolées avant modélisation | Invendus sortis du scope de clustering |
| **Modèle** | Nombre de segments justifié par une métrique objective | Score de silhouette |
| **Modèle** | Robustesse testée par comparaison | ≥ 2 algorithmes (KMeans, Agglomératif) ET 2 jeux de variables (variante A, B) comparés |
| **Opérationnel** | Résultat reproductible | `random_state` fixé, date d'ancrage figée sur la donnée, notebook exécutable de bout en bout sans erreur |
| **Métier** | Segments interprétables et actionnables | Chaque segment nommé + 1 recommandation |

### 1.11 Mini-plan de formation pour les équipes métier

**Besoin** : les équipes assortiment/pricing/stock doivent pouvoir lire le résultat sans compétence data science.

| Format | Contenu | Durée |
|---|---|---|
| Fiche 1 page | Les 4 segments, un pictogramme par segment, une action par segment (cf. §4 du notebook) | Lecture 5 min |
| Session de restitution | Démonstration du graphique rotation × marge coloré par segment ; Q&R sur les cas limites (ex. pourquoi tel produit est dans tel segment) | 30 min |
| Point de vigilance à transmettre | La segmentation est un **instantané** : à recalculer périodiquement, pas figée définitivement | — |

**Arbitrage sur le format** : une fiche synthétique + démo commentée a été préférée à une formation technique complète (ex. apprendre à relire du code Python) — l'objectif est l'usage du résultat, pas la reproduction de la méthode par des non-data.

**Accessibilité (principe respecté pour tous les publics, y compris en situation de handicap)** :
- Fiche 1 page fournie en **texte structuré** (pas uniquement en image), compatible lecteur d'écran, avec un contraste de couleurs suffisant sur les 4 segments (pas de code couleur seul — chaque segment est aussi identifié par un nom et un libellé texte).
- Graphique de restitution accompagné d'une **description textuelle équivalente** (ce que montre le graphique, en une phrase, pour les personnes malvoyantes ou utilisant un lecteur d'écran).
- Session de restitution proposée en présentiel **et** en version enregistrée avec sous-titres, pour couvrir les contraintes d'agenda et les besoins d'accessibilité auditive.
- Vocabulaire technique (silhouette, KMeans, StandardScaler) volontairement absent de la fiche métier — reformulé en langage courant ("indice de fiabilité du regroupement", "algorithme de regroupement automatique").

---

## 2. Veille métier et technologique

### 2.1 Besoin de veille

Basculer d'une lecture univariée faite à la main (P6) vers une segmentation multivariée automatisée implique trois choix techniques distincts : quel algorithme de regroupement utiliser, comment déterminer le nombre de groupes pertinent, et comment traiter en amont les anomalies de données repérées lors de l'audit. La veille ci-dessous couvre ces trois choix.

### 2.2 Panel de solutions évaluées

| Axe | Option | Cas d'usage | Avantages | Limites | Sobriété / impact | Décision |
|---|---|---|---|---|---|---|
| **Clustering** | **KMeans** | Partitionnement de données numériques, géométrie « plate » | Rapide, simple, centroïdes interprétables | Suppose des clusters sphériques ; sensible à l'échelle et aux outliers | Très léger (complexité linéaire en nb de points) — coût de calcul négligeable sur 689 lignes, aucune ressource cloud nécessaire | **Retenu** — meilleure silhouette obtenue sur nos données à chaque comparaison (0,400 vs 0,367 en variante A ; 0,386 vs 0,287 en variante B, k=3) |
| | Clustering Agglomératif (Ward) | Structure hiérarchique, pas de k fixé a priori | Dendrogramme lisible, pas d'hypothèse de forme sphérique | Plus coûteux, moins performant ici | Complexité quadratique en nb de points — encore négligeable ici (689 lignes) mais ne passerait pas à l'échelle sur un catalogue de plusieurs dizaines de milliers de références sans un coût de calcul et énergétique bien supérieur | Comparé — témoin de robustesse, écarté sur ce jeu de données |
| **Choix du nombre de clusters** | Score de silhouette | Validation interne chiffrée et reproductible | Objectif, comparable entre variantes | Peut désigner un optimum statistique qui masque un segment métier utile (cf. §3.4) | Calcul déjà inclus dans l'exécution scikit-learn, pas de surcoût | **Retenu**, mais **pondéré par un critère métier explicite** quand l'écart est faible |
| **Fiabilisation de la donnée (amont)** | **Pandera** | Validation de schéma en notebook/pipeline | Léger (~12 dépendances), API proche de pandas, type-safe | Pas de reporting « métier » natif | Empreinte minimale : librairie légère, exécution locale, pas de service externe à faire tourner en continu | Piste retenue pour industrialiser la détection du bug de fusion identifié en §3.1 (ex. règle : `id_web` ne doit jamais être NaN des deux côtés d'un merge) |
| | Great Expectations | Qualité de données en pipeline de production | Multi-moteur, Data Docs lisibles par le métier | Lourd, surdimensionné pour un notebook ponctuel | 100+ dépendances, empreinte disque et temps d'installation nettement supérieurs pour un usage ponctuel — non sobre au regard du besoin réel | Écarté à ce stade (sur-ingénierie disproportionnée par rapport au volume traité) |

**Principe de sobriété appliqué à la décision finale** : sur un volume de 689 produits, l'écart de coût de calcul entre les options est négligeable en valeur absolue — mais le raisonnement de sobriété a été mené comme s'il devait passer à l'échelle (catalogue complet BottleNeck, plusieurs dizaines de milliers de références), ce qui a pesé en faveur de KMeans (linéaire) et de Pandera (léger) plutôt que de solutions plus lourdes mais non nécessaires au besoin actuel.

**Limite assumée sur Pandera** : contrairement à KMeans, testé et comparé chiffres à l'appui dans le notebook (§5-7), Pandera n'a été qu'**identifié** comme piste via la veille — il n'a pas été expérimenté (pas de schéma de validation implémenté dans ce POC). C'est une action volontairement reportée à une itération d'industrialisation future (cf. §4.1, lot L7), documentée comme telle plutôt que présentée à tort comme testée.

### 2.3 Critères de comparaison

On juge une option sur la qualité de la séparation obtenue entre groupes, sa sensibilité au bruit ou aux biais, le temps de calcul requis, une dimension **sobriété / impact** (empreinte calcul et outillage), la reproductibilité d'une exécution à l'autre, la facilité avec laquelle un non-spécialiste peut interpréter le résultat, et enfin la charge de maintenance de la solution dans la durée.

### 2.4 Système de veille : élément d'automatisation

Pour ne pas re-comparer manuellement les mêmes outils à chaque projet, un flux de veille minimal a été mis en place :

- **Abonnement au flux "Releases" du dépôt GitHub `scikit-learn/scikit-learn`** (notifications automatiques à chaque nouvelle version stable, ex. changements sur `KMeans`, nouveaux algorithmes de clustering) — permet de détecter une évolution qui remettrait en cause un choix documenté ici sans avoir à revérifier manuellement la documentation à chaque projet.
- **Alerte équivalente sur `unitaryai/pandera`** (piste retenue en §2.2), pour suivre sa maturité avant une éventuelle industrialisation.

Cet élément d'automatisation soutient directement la démarche d'amélioration continue : un changement notable dans un outil suivi déclenche une réévaluation ciblée plutôt qu'une revue complète de la veille.

### 2.5 Sources

- scikit-learn — *Clustering* (documentation officielle, comparatif des algorithmes et du score de silhouette), consultée le 06/08/2026 : https://scikit-learn.org/stable/modules/clustering.html
- Pandera — documentation officielle, consultée le 06/08/2026 : https://pandera.readthedocs.io/
- Great Expectations — documentation officielle, consultée le 06/08/2026 : https://docs.greatexpectations.io/
- pandas — documentation officielle sur le comportement de `merge()` avec valeurs manquantes (base de la détection du bug §3.1), consultée le 06/08/2026 : https://pandas.pydata.org/docs/reference/api/pandas.merge.html

### 2.6 Traçabilité de l'usage de l'IA

L'IA (Claude) a été mobilisée comme assistant critique sur ce projet, avec validation systématique avant intégration :

| Étape | Ce qui a été demandé | Ce qui a été retenu | Ce qui a été écarté / reformulé |
|---|---|---|---|
| Audit de l'export P6 | Repérer les anomalies dans `df_final.xlsx` au-delà de celles déjà identifiées en P6 | Détection du bug de fusion `id_web` NaN==NaN (182 lignes corrompues, non identifiées en P6) | — |
| Correction du bug | Deux options proposées et comparées : exclusion en aval (rapide, disponible immédiatement) vs refusion à la source (plus rigoureuse, mais nécessitait les fichiers sources) | Exclusion testée en premier faute d'accès aux sources ; **refusion à la source finalement menée** une fois les fichiers obtenus en cours de projet, retenue comme version définitive après validation croisée (mêmes résultats : 714/25/689) | Aucune option écartée définitivement — les deux ont été menées et comparées |
| Choix du k pour la variante B | Proposition automatique : k au silhouette maximal (k=3) | k=4 retenu malgré une silhouette légèrement inférieure, sur justification métier explicite (segment stock dormant révélé) — **décision humaine, pas suivie aveuglément de la sortie algorithmique** | k=3 (optimum statistique pur) écarté au profit du critère métier |
| Nommage des segments | Suggestions de noms de segments à partir des profils chiffrés | Noms adaptés aux profils réels observés (ex. "Premium à faible rotation d'entrée" plutôt qu'un simple "Premium" générique, pour refléter la spécificité du profil ventes/rotation) | — |

---

## 3. Démarche : hypothèses, tests, résultats, décisions

> Cette section trace les choix de modélisation menés dans `p6_extended.ipynb`, leurs justifications, et les pistes écartées.

### 3.1 Audit critique : un bug non détecté en P6, corrigé à la source

**Constat** : le P6 fusionne les tables via `pd.merge(df_final, df_web, on='id_web', how='outer')`. Pandas traite deux valeurs `NaN` comme égales lors d'un merge : tous les produits ERP sans correspondance web (`id_web` NaN, faute de ligne dans `liaison.xlsx`) ont été croisés en cartésien avec les lignes web elles-mêmes sans `id_web`.

**Preuve chiffrée (fusion naïve reproduite dans le notebook)** : cette fusion, refaite à l'identique du P6, donne 916 lignes dont 182 à `id_web` manquant mais colonnes web renseignées (`post_title`, `product_type`) — impossible si la jointure avait réellement échoué. Ces 182 lignes correspondent à seulement **91 `product_id` uniques**, chacun dupliqué, avec un `total_sales` constant et fabriqué (**-56 ou -17** selon le groupe) qui n'est pas une vraie mesure de ventes. Ce sont ces lignes qui expliquaient les `total_sales` négatifs de l'export original (`min = -56`) et les rotations de stock aberrantes (jusqu'à -3,65 mois) — un artefact de fusion, pas un phénomène métier réel.

**Deux corrections comparées, avec critères explicites** :

| Option | Principe | Rigueur | Faisabilité | Décision |
|---|---|---|---|---|
| **A — Exclusion en aval** | Filtrer les lignes `id_web` NaN sur l'export déjà fusionné | Corrige le symptôme, pas la cause ; fragile si la structure des NaN change dans un futur export | Faisable immédiatement (seul l'export `df_final.xlsx` requis) | Testée en premier (résultat : 714 produits fiables) |
| **B — Refusion à la source** | Séparer les lignes à `id_web` connu (merge normal) des lignes orphelines (aucune correspondance par construction, gardées sans jointure) avant de les recombiner | Corrige la cause ; robuste à toute évolution future de la donnée | Nécessite les 3 fichiers sources (obtenus en cours de projet) | **Retenue au final**, une fois les fichiers sources disponibles |

**Validation croisée** : les deux options produisent exactement le même résultat en aval — **714 produits fiables, 25 invendus, 689 en cœur de catalogue** — ce qui confirme que l'exclusion initiale était une décision correcte, tout en montrant que la refusion à la source est la version la plus rigoureuse à conserver pour la suite (825 lignes = 825 produits ERP, chacun une seule fois, zéro doublon).

### 3.2 Isolement des régimes particuliers avant le ML

**Hypothèse** : l'absence totale de vente (`total_sales == 0`) ne traduit pas un simple niveau bas dans un continuum de performance — c'est une situation à part, différente par nature d'un produit qui se vend peu mais se vend quand même. Demander au clustering de faire cette distinction reviendrait à lui faire deviner une frontière qu'une règle métier simple permet de fixer directement.

**Décision** : isolement par règle métier explicite, avant le clustering.

| Règle | Volume |
|---|---|
| Invendus (`total_sales == 0`) | 25 produits |
| → Cœur de catalogue (base du clustering) | 689 produits |

### 3.3 Choix des variables (anti-fuite de données)

Deux variables explicitement exclues des features :
- `ca_par_article` (= `price × total_sales`) : colinéaire aux entrées.
- `taux_marge` : quasi-plate sur le cœur de catalogue (75% des produits entre 87,9% et 99,6%) — non discriminante pour séparer des groupes, donc écartée des features, mais gardée à titre indicatif pour décrire les segments une fois formés.

**Anomalie signalée, non corrigée** : `product_id` 4355 a un `purchase_price` (77,48€) très supérieur au `price` de vente (12,65€), donnant une marge de -83,7% — vraisemblablement une erreur de saisie. Hors périmètre du P13 (correction à reporter au P6), mais documentée comme limite connue.

### 3.4 Pré-traitement et comparaison des variantes

**Transformation** : `log1p` appliqué à `price`, `total_sales`, `rotation_stock` (asymétrie à droite, skew jusqu'à 4,93) ; pas à `anciennete_jours` (asymétrie modérée à gauche). `StandardScaler` sur toutes les variables — KMeans raisonne en distances.

| | Variante A — 3 axes | Variante B — 4 axes |
|---|---|---|
| Variables | prix, ventes, ancienneté | prix, ventes, ancienneté, **rotation de stock** |
| Meilleur k statistique | k=3 (silhouette 0,400) | k=3 (silhouette 0,386) |
| k=4 testé ? | — | Oui : silhouette 0,375 (écart -0,011 vs k=3) |

![Comparaison des scores de silhouette entre la variante A (3 axes) et la variante B (4 axes), selon le nombre de clusters k](images/silhouette_comparaison.png)

*Lecture du graphique : la variante A domine systématiquement en netteté statistique, mais l'écart avec la variante B se resserre à k=4 (0,400 vs 0,375) — c'est cet écart marginal qui rend l'arbitrage métier possible sans sacrifier excessivement la qualité de séparation.*

**Arbitrage k=3 vs k=4 sur la variante B** : le k optimal au sens strict de la silhouette est 3. Mais à k=4, le plus petit cluster (32 produits) affiche une rotation de stock moyenne de **16,9 mois**, contre 3,0 mois pour l'ensemble du cœur de catalogue — un segment à rotation anormale, invisible à k=3 où il serait dilué dans un groupe plus large. Sa dispersion interne (`describe()` sur le sous-groupe) confirme qu'il ne s'agit pas d'un artefact (pas un point unique isolé).

**Décision** : k=4 retenu pour la variante B malgré la perte marginale de silhouette (-0,011) — l'actionnabilité prime sur la netteté statistique pure, dès lors que le segment supplémentaire est validé comme homogène.

**Arbitrage final entre variantes** : écart de silhouette entre variante A (k=3, 0,400) et variante B (k=4, 0,375) = +0,025 en faveur de A. Variante B retenue malgré cet écart : elle est la seule à révéler le segment "stock dormant", directement actionnable pour la gestion de stock — objectif même du cahier des charges (§1.10, critère métier).

### 3.5 Segments obtenus et recommandations

| Segment | Volume | Profil clé | Action métier |
|---|---|---|---|
| **Moteur de CA** | 327 | Prix 16,5€ · fort volume (10,6 ventes) · ancien (827j) · rotation saine (2,7 mois) | Sécuriser la disponibilité |
| **Premium à faible rotation d'entrée** | 189 | Prix 57,3€ · faibles ventes (4,7) · rotation rapide (1,6 mois, stock volontairement réduit) | Piloter le réassort au fil de l'eau |
| **Nouveautés performantes** | 141 | Prix 25,5€ · récent (374j) · bonnes ventes (8,8) | Accélérer la mise en avant |
| **Stock dormant** | 32 | Prix 75,7€ · rotation 16,9 mois (6× la moyenne) · marge plus faible (73%) | Déstocker en priorité |

Le segment *Stock dormant* était invisible dans une segmentation prix/ventes/ancienneté seule — c'est l'ajout de la rotation de stock qui le révèle, validant la démarche de comparaison A/B.

![Les 4 segments du catalogue BottleNeck, positionnés selon la rotation de stock et le taux de marge](images/segments_scatter.png)

*Lecture du graphique : le segment "Stock dormant" (en rouge) se détache nettement sur l'axe horizontal (rotation de stock), avec une dispersion propre — ce n'est pas un nuage de points épars, ce qui confirme visuellement qu'il ne s'agit pas d'un artefact isolé.*

### 3.6 Limites de l'analyse

- Données en instantané, pas de série temporelle → forecasting hors périmètre.
- Bug de fusion identifié **et corrigé à la source** (refusion depuis `erp.xlsx`/`web.xlsx`/`liaison.xlsx`, validée par comparaison avec l'approche par exclusion — résultats identiques).
- Volume modeste (689 produits) : POC indicatif, non déployable en l'état.
- Une anomalie de saisie probable (`product_id` 4355) signalée mais non corrigée.
- Silhouettes modestes (~0,38-0,40) : attendu sur des données produits en continuum, pas un échec du modèle.

---

## 4. Organisation et pilotage du projet

### 4.1 Découpage en lots

| Lot | Contenu | Livrable de sortie |
|---|---|---|
| **L1 — Cadrage** | Poser le problème métier et ses limites : à qui s'adresse le résultat, ce qui entre et sort du périmètre, ce qui contraint le projet, comment on saura que c'est réussi | Cahier des charges fonctionnel (§1) |
| **L2 — Veille** | Comparaison méthodes/outils, sources | Tableau de veille sourcé (§2) |
| **L3 — Audit & préparation** | Audit de l'export P6, détection du bug de fusion, isolement des invendus | `df_clean` / `coeur` propres |
| **L4 — Modélisation** | Pré-traitement, variantes A/B, comparaison KMeans vs Agglomératif, arbitrage k | Tables de silhouette + décision tracée |
| **L5 — Validation** | Vérification d'homogénéité du segment révélé, contrôle anti-fuite | Segment "Stock dormant" confirmé non-artefact |
| **L6 — Restitution** | Nommage métier, recommandations, mini-plan de formation | Notebook conclu + §1.11 |
| **L7 — Industrialisation légère** *(piste future)* | Validation Pandera du merge (règle anti-NaN==NaN), re-fusion depuis les sources | Non réalisé — backlog futur |

### 4.2 Backlog priorisé

Charge relative : **S** (≤ ½ j), **M** (½–1 j), **L** (> 1 j).

| # | Tâche | Lot | Charge | Dépend de | Date cible | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | Reformuler le besoin métier | L1 | S | — | 03/08/2026 | Problématique validée |
| T2 | Comparer méthodes de clustering + outils qualité, sourcer | L2 | M | — | 04/08/2026 | Tableau de veille avec ≥ 2 options/axe |
| T3 | Auditer `df_final.xlsx` (NaN, doublons, cohérence) | L3 | M | T1 | 05/08/2026 | Bug de fusion identifié et prouvé |
| T4 | Isoler les lignes corrompues et les invendus | L3 | S | T3 | 05/08/2026 | `coeur` = 689 produits, comptes vérifiés |
| T5 | Feature engineering + pré-traitement (log/scale justifiés) | L4 | M | T4 | 06/08/2026 | 0 NaN dans les features, transfos argumentées |
| T6 | Variante A : silhouette + comparaison KMeans/Agglomératif | L4 | M | T5 | 06/08/2026 | k justifié |
| T7 | Variante B : idem + arbitrage k=3 vs k=4 | L4 | M | T6 | 07/08/2026 | Décision tracée (statistique vs métier) |
| T8 | Arbitrer entre variantes A et B | L5 | S | T6, T7 | 07/08/2026 | Décision documentée |
| T9 | Valider l'homogénéité du segment "Stock dormant" | L5 | S | T8 | 07/08/2026 | Dispersion vérifiée, non-artefact |
| T10 | Nommer les segments + recommandations | L6 | M | T9 | 08/08/2026 | 4 segments nommés, 1 reco/segment |
| T11 | Documentation de la démarche (ce document) | L6 | L | tous | 08-14/08/2026 | Doc complète, reproductible |

### 4.3 Planning & jalons

| Jalon | Date cible | Contenu | Critère de passage |
|---|---|---|---|
| **J1 — Cadrage validé** | 04/08/2026 | L1 + L2 | Problématique + veille arrêtées |
| **J2 — Données auditées** | 05/08/2026 | L3 | Bug de fusion isolé, `coeur` propre |
| **J3 — Modèle v1 (baseline)** | 06/08/2026 | L4 variante A | Segmentation 3 axes obtenue |
| **J4 — Modèle v2 + arbitrage** | 07/08/2026 | L4 variante B + L5 | Décision k=4 tranchée et validée |
| **J5 — Restitution** | 14/08/2026 | L6 | Segments nommés, doc déposable |

**Marge de sécurité** : 6 jours entre J4 (arbitrage technique bouclé) et J5 (échéance finale) — volontairement large pour absorber un imprévu (c'est ce créneau qui a permis d'intégrer la refusion à la source une fois les fichiers obtenus, sans décaler l'échéance finale).

### 4.4 Points de contrôle

- **Reproductibilité** : `random_state=42` fixé, date d'ancrage figée sur `post_date_gmt.max()` (et non la date d'exécution).
- **Validation intermédiaire** : à chaque jalon, contrôle des comptes (714 → 689) et des garde-fous (0 NaN dans les features) avant de poursuivre.
- **Revue de décision** : chaque choix méthodologique (exclusion des lignes corrompues, choix de k, arbitrage variantes) documenté au moment où il est pris.

### 4.5 Registre des risques

| Risque | Prob. | Impact | Parade mise en œuvre | Statut |
|---|---|---|---|---|
| **Anomalie de fusion non détectée** (héritée du P6) | Élevée | Élevé | Audit systématique de l'export avant modélisation ; bug reproduit puis **corrigé à la source** (refusion depuis les 3 fichiers, validée par comparaison croisée) | ✅ Maîtrisé |
| **Risque de colinéarité dans les features** (une variable dérivée directement d'une autre) | Élevée | Élevé | `ca_par_article` et `taux_marge` volontairement écartées des variables de clustering | ✅ Maîtrisé |
| **Biais de méthode** (distance euclidienne sur données asymétriques) | Moyenne | Moyen | `log1p` justifié par la forme des distributions + `StandardScaler` | ✅ Maîtrisé |
| **Sur-interprétation du k statistique** | Moyenne | Moyen | Arbitrage explicite k=3 vs k=4, validation d'homogénéité du segment supplémentaire | ✅ Maîtrisé |
| **Correction incomplète** (fichiers sources indisponibles) | Moyenne | Moyen | Fichiers sources obtenus en cours de projet ; refusion propre menée et validée (§3.1) | ✅ Maîtrisé |
| **Volume insuffisant** (689 produits) | Moyenne | Moyen | POC explicite, non déployable en l'état | ⚠️ Accepté |
| **Métriques instables** (silhouette modeste ~0,38) | Élevée | Faible | Assumé et documenté : continuum de données produits | ⚠️ Accepté |
| **Non-reproductibilité** | Moyenne | Élevé | `random_state` fixé, ancienneté ancrée sur date figée | ✅ Maîtrisé |

---

## 5. Synthèse recruteur / client

Le P6 livrait un audit descriptif du catalogue, variable par variable. Le P13 transforme cet audit en **outil de décision** : une segmentation en 4 familles actionnables, obtenue par une démarche critique qui a elle-même révélé une anomalie de données non détectée en P6 (bug de fusion pandas) — anomalie reproduite, prouvée, puis **corrigée à la source**, avec une validation croisée entre deux méthodes de correction. La méthode de segmentation a été choisie et validée par comparaison systématique (2 algorithmes, 2 jeux de variables, 2 valeurs de k), avec un arbitrage assumé entre performance statistique et valeur métier — le résultat final priorise la valeur métier de façon documentée plutôt que l'optimum algorithmique brut.

**Prochaines étapes suggérées** : validation automatisée (Pandera) pour prévenir la réapparition du bug de fusion ; recalcul périodique de la segmentation à mesure que le catalogue évolue.
