"""
Application de detection de faux billets - ONCFM
==================================================

Ce script permet de predire si un ou plusieurs billets sont vrais ou faux,
a partir de leurs six caracteristiques geometriques :
    - diagonal
    - height_left
    - height_right
    - margin_low
    - margin_up
    - length

Le modele utilise est une regression logistique, entrainee sur 1500 billets
deja verifies (voir le notebook P12_detection_faux_billets.ipynb pour le
detail de l'analyse et du choix du modele).

Deux modes d'utilisation :

1) Fichier CSV contenant plusieurs billets :
    python predict_billets.py --csv billets_production.csv

2) Un seul billet, en donnant directement les six valeurs :
    python predict_billets.py --valeurs 171.81 104.86 104.95 4.52 2.89 112.83

Le fichier CSV doit contenir les six colonnes ci-dessus, separees par un
point-virgule (";"), avec une colonne "id" optionnelle. La colonne
"margin_low" peut contenir des valeurs manquantes : elles seront estimees
automatiquement.

Le script affiche pour chaque billet la prediction ("Vrai billet" ou
"Faux billet") ainsi que la probabilite associee, et enregistre un fichier
resultats_predictions.csv dans le meme dossier.
"""

import argparse
import os
import sys
import pickle

import pandas as pd


COLONNES_FEATURES = ["diagonal", "height_left", "height_right",
                      "margin_low", "margin_up", "length"]

DOSSIER_SCRIPT = os.path.dirname(os.path.abspath(__file__))

CHEMIN_MODELE_IMPUTATION = os.path.join(DOSSIER_SCRIPT, "modele_imputation_margin_low.pkl")
CHEMIN_SCALER = os.path.join(DOSSIER_SCRIPT, "scaler_billets.pkl")
CHEMIN_MODELE_FINAL = os.path.join(DOSSIER_SCRIPT, "modele_final_billets.pkl")


def charger_modeles():
    """Charge le modele d'imputation, le scaler et le modele final depuis le disque."""

    with open(CHEMIN_MODELE_IMPUTATION, "rb") as fichier:
        modele_imputation = pickle.load(fichier)

    with open(CHEMIN_SCALER, "rb") as fichier:
        scaler = pickle.load(fichier)

    with open(CHEMIN_MODELE_FINAL, "rb") as fichier:
        modele_final = pickle.load(fichier)

    return modele_imputation, scaler, modele_final


def imputer_margin_low(donnees, modele_imputation):
    """Remplace les valeurs manquantes de margin_low par une estimation.

    L'estimation est realisee par regression lineaire a partir des cinq
    autres caracteristiques geometriques du billet.
    """

    variables_explicatives = ["diagonal", "height_left", "height_right", "margin_up", "length"]
    masque_manquant = donnees["margin_low"].isna()

    if masque_manquant.sum() > 0:
        valeurs_estimees = modele_imputation.predict(donnees.loc[masque_manquant, variables_explicatives])
        donnees.loc[masque_manquant, "margin_low"] = valeurs_estimees
        print("Valeurs manquantes de margin_low estimees pour", masque_manquant.sum(), "billet(s).")

    return donnees


def predire(donnees, modele_imputation, scaler, modele_final):
    """Applique le pipeline complet (imputation, standardisation, prediction)."""

    donnees = donnees.copy()

    colonnes_manquantes = [colonne for colonne in COLONNES_FEATURES if colonne not in donnees.columns]
    if len(colonnes_manquantes) > 0:
        print("Erreur : colonnes manquantes dans les donnees fournies :", colonnes_manquantes)
        sys.exit(1)

    donnees = imputer_margin_low(donnees, modele_imputation)

    donnees_scaled = scaler.transform(donnees[COLONNES_FEATURES])

    predictions = modele_final.predict(donnees_scaled)
    probabilites = modele_final.predict_proba(donnees_scaled)

    resultats = donnees.copy()
    resultats["prediction"] = ["Vrai billet" if prediction else "Faux billet" for prediction in predictions]
    resultats["probabilite_vrai_billet"] = probabilites[:, 1].round(4)

    return resultats


def lire_csv_billets(chemin_csv):
    """Lit un fichier CSV de billets en detectant automatiquement le separateur.

    Le fichier peut etre separe par des virgules (format du fichier
    billets_production.csv fourni par l'ONCFM) ou par des points-virgules
    (format du fichier d'exemple billets.csv). Les deux sont acceptes.
    """

    with open(chemin_csv, "r", encoding="utf-8") as fichier:
        premiere_ligne = fichier.readline()

    if premiere_ligne.count(";") > premiere_ligne.count(","):
        separateur = ";"
    else:
        separateur = ","

    donnees = pd.read_csv(chemin_csv, sep=separateur)
    return donnees


def traiter_fichier_csv(chemin_csv, modele_imputation, scaler, modele_final):
    """Lit un fichier CSV de billets et affiche/enregistre les predictions."""

    if not os.path.exists(chemin_csv):
        print("Erreur : le fichier", chemin_csv, "n'existe pas.")
        sys.exit(1)

    donnees = lire_csv_billets(chemin_csv)

    colonne_id = None
    for nom_colonne_possible in ["id", "Id", "ID"]:
        if nom_colonne_possible in donnees.columns:
            colonne_id = nom_colonne_possible
            break

    resultats = predire(donnees, modele_imputation, scaler, modele_final)

    if colonne_id is not None:
        autres_colonnes = [colonne for colonne in resultats.columns if colonne != colonne_id]
        resultats = resultats[[colonne_id] + autres_colonnes]

    print()
    print("Resultats des predictions :")
    print(resultats.to_string(index=False))

    chemin_sortie = os.path.join(os.path.dirname(os.path.abspath(chemin_csv)), "resultats_predictions.csv")
    resultats.to_csv(chemin_sortie, sep=";", index=False)
    print()
    print("Resultats enregistres dans :", chemin_sortie)

    nombre_faux = (resultats["prediction"] == "Faux billet").sum()
    nombre_vrais = (resultats["prediction"] == "Vrai billet").sum()
    print()
    print("Recapitulatif :", nombre_vrais, "vrai(s) billet(s),", nombre_faux, "faux billet(s) detecte(s).")


def traiter_valeurs_manuelles(valeurs, modele_imputation, scaler, modele_final):
    """Traite un seul billet fourni via ses six valeurs en ligne de commande."""

    if len(valeurs) != 6:
        print("Erreur : il faut fournir exactement 6 valeurs, dans l'ordre :")
        print("diagonal height_left height_right margin_low margin_up length")
        sys.exit(1)

    donnees = pd.DataFrame([valeurs], columns=COLONNES_FEATURES)

    resultats = predire(donnees, modele_imputation, scaler, modele_final)

    print()
    print("Resultat de la prediction :")
    print("Prediction :", resultats.loc[0, "prediction"])
    print("Probabilite que le billet soit vrai :", resultats.loc[0, "probabilite_vrai_billet"])


def main():
    parser = argparse.ArgumentParser(
        description="Detection de faux billets a partir de leurs caracteristiques geometriques (ONCFM)."
    )
    groupe = parser.add_mutually_exclusive_group(required=True)
    groupe.add_argument(
        "--csv",
        type=str,
        help="Chemin vers un fichier CSV contenant les billets a analyser (colonnes : "
             "diagonal;height_left;height_right;margin_low;margin_up;length)."
    )
    groupe.add_argument(
        "--valeurs",
        type=float,
        nargs=6,
        metavar=("diagonal", "height_left", "height_right", "margin_low", "margin_up", "length"),
        help="Les six valeurs geometriques d'un seul billet, dans cet ordre precis."
    )

    arguments = parser.parse_args()

    modele_imputation, scaler, modele_final = charger_modeles()

    if arguments.csv is not None:
        traiter_fichier_csv(arguments.csv, modele_imputation, scaler, modele_final)
    else:
        traiter_valeurs_manuelles(arguments.valeurs, modele_imputation, scaler, modele_final)


if __name__ == "__main__":
    main()
