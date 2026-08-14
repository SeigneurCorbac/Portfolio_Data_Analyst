# P9 — Ventes Librairie Python
 
## Contexte
Analyse du profil client et des habitudes d'achat d'une librairie en ligne
fictive, à partir de 3 sources : clients, produits, transactions.
 
## Problème métier
Comprendre qui achète, quoi, et identifier des leviers business
exploitables (segmentation, dépendance à certains clients).
 
## Démarche
- Fusion des 3 fichiers (jointure externe), isolement de 21 clients sans
  achat et 21 produits jamais vendus, exclus des statistiques
- Analyse du CA : courbe mensuelle lissée par moyenne mobile 3 mois,
  répartition par catégorie de produit
- Courbe de Lorenz et indice de Gini pour mesurer la concentration du CA
- Tests statistiques avec justification systématique du choix de méthode :
  Khi² (indépendance genre/catégorie), Spearman plutôt que Pearson (les
  distributions ne sont pas gaussiennes), Kruskal-Wallis plutôt qu'ANOVA
  après confirmation de la non-normalité par un test de Shapiro-Wilk
 
## Résultat
Indice de Gini de 0,44 (4 clients BtoB représentant ~7,3% du CA total) ;
association significative entre genre et catégorie de livres achetés
(χ²=22,67, p=0,000012) ; l'âge s'est révélé un prédicteur faible des
habitudes d'achat, orientant la segmentation vers le genre plutôt que
l'âge pour les recommandations produit.
 
## Compétences démontrées
Nettoyage multi-sources, choix et justification de tests statistiques
paramétriques vs non paramétriques, mesure de concentration économique
(Gini/Lorenz), traduction de résultats statistiques en implications
business.
 
## Outils
Python, pandas, matplotlib, scipy
 
## Livrables dans ce dossier
- Notebook d'analyse complet
- Résumé statistique (synthèse des tests et résultats)
