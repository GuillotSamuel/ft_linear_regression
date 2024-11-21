# Régression linéaire

## Notion mathématiques

### Variance

Mesure de la dispersion des valeur : moyenne des carrés des écarts à cette moyenne.

Etapes de calcul :
1. Moyenne des valeurs
2. Somme des écarts à la moyenne au carré (valeur - moyenne) ^ 2 (suppression des valeurs négatives)
3. Division de la somme des écarts au carré par le nombre de valeurs (moins degré de liberté)

Exemple avec l'échantillon suivant :  [3, 7, 5, 10, 8]
1.  (3 + 7 + 5 + 10 + 8) / 5 = 33 / 5 = 6.6
2.  (3 - 6.6) ^ 2 = 13.96
    (7 - 6.6) ^ 2 = 0.16
    (5 - 6.6) ^ 2 = 2.56
    (10 - 6.6) ^ 2 = 11.56
    (8 - 6.6) ^ 2 = 1.96
    (13.6 + 0.16 + 2.56 + 11.56 + 1.96) = 30.2
3.  variance = 30.2 / 5 = 6.04

## Covariance
