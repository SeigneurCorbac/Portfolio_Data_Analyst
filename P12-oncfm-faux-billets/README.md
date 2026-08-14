# P12 — ONCFM : détection de faux billets
 
## Contexte
Projet pour l'Organisation nationale de lutte contre le faux-monnayage
(ONCFM) : détecter automatiquement les billets contrefaits à partir de
mesures géométriques.
 
## Problème métier
Automatiser la détection de faux billets en euros à partir de 6 mesures
géométriques (diagonale, hauteurs, marges, longueur), sur un jeu de 1500
billets pré-vérifiés (1000 vrais, 500 faux).
 
## Démarche
- Imputation des valeurs manquantes de margin_low par régression linéaire
  (R² = 0,546) plutôt que suppression des lignes, pour préserver la classe
  minoritaire (billets contrefaits)
- Comparaison de 4 modèles : régression logistique, K-Means, KNN, Random
  Forest
- Régression logistique retenue en modèle final malgré une exactitude
  légèrement inférieure au KNN (meilleur score brut), pour sa stabilité,
  son interprétabilité et l'absence de dérive liée aux hyperparamètres —
  décision documentée illustrant qu'un score n'est pas le seul critère
  de choix en contexte métier
 
## Résultat
Modèle déployé sous 3 formes : script Python autonome, application
Streamlit, application HTML côté client. Validé sur le jeu de production
officiel (5/5 prédictions correctes).
 
## Compétences démontrées
Machine learning supervisé et non supervisé, imputation de données,
comparaison et arbitrage de modèles, déploiement et packaging
d'application.
 
## Outils
Python, scikit-learn, Streamlit, pandas
 
## Livrables suggérés dans ce dossier
- Notebook d'analyse complet
- predict_billets.py (script de prédiction)
- Lien vers l'application Streamlit déployée
- Présentation (PPTX, 15 slides)
