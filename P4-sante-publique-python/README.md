# P4 — Étude de santé publique avec Python
 
## Contexte
Étude de la sous-nutrition mondiale à partir de données FAO (population,
disponibilité alimentaire, aide alimentaire, sous-nutrition).
 
## Problème métier
La production alimentaire mondiale suffit-elle à nourrir la planète, ou
la sous-nutrition est-elle avant tout un problème de répartition ? Où
concentrer les efforts pour un impact maximal ?
 
## Démarche
- Fusion et nettoyage de 4 sources FAO, harmonisation des unités
  (milliers de tonnes → kg), conversion des plages d'années en année
  médiane pour permettre la jointure
- Calcul de la capacité de nourrissage théorique mondiale à partir des
  calories disponibles
- Décomposition de la disponibilité intérieure par usage (nourriture,
  alimentation animale, pertes, traitement, semences)
- Identification des pays les plus touchés par la sous-nutrition et des
  principaux bénéficiaires de l'aide alimentaire
- Étude de cas sur le manioc thaïlandais (production vs exportation)
 
## Résultat
La production mondiale de calories permettrait théoriquement de nourrir
126% de la population réelle (104% en ne comptant que les végétaux) —
la sous-nutrition (535,7 millions de personnes, 7,1% de la population
mondiale en 2017) est donc structurellement un problème de répartition,
pas de volume produit. Seulement 49,5% de la disponibilité intérieure
mondiale sert de nourriture humaine directe (13,2% part à l'alimentation
animale). Cas du manioc thaïlandais : 83,4% de la production est
exportée contre 2,9% seulement consommée localement comme nourriture.
 
## Compétences démontrées
Nettoyage et harmonisation de données multi-sources (unités, granularité
temporelle), calcul d'indicateurs à l'échelle mondiale, restitution de
résultats contre-intuitifs.
 
## Outils
Python, pandas, matplotlib, seaborn
 
## Livrables dans ce dossier
- Notebook d'analyse complet
