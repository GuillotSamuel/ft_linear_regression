# Régression linéaire

## Calcul direct basé sur la covariance et la variance

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

### Covariance

Mesure de la relation entre deux variables :
- Covariance positive = les deux variables augmentent ou diminuent ensemble
- Covariance négative = une variable augmente pendant que l'autre diminuent
- Covariance nulle (ou proche de 0) = pas de relation significative entre les deux variables

Etapes de calcul :
1. Moyennes des valeurs des deux variables
2. Calcul des écarts à la moyenne pour chaque valeur
3. Multiplication des écarts à la moyenne pour chaque valeur
4. Somme des produits des écarts
5. Division par n - degré de liberté de la somme des écarts

Exemple avec les échantillons suivants :  x[3, 7, 5, 10, 8] y[1, 4, 3, 8, 6]
1.  (3 + 7 + 5 + 10 + 8) / 5 = 33 / 5 = 6.6
    (1 + 4 + 3 + 8 + 6) / 5 = 4.4
2.  x   (3 - 6.6) = -3.6
        (7 - 6.6) = 0.4
        (5 - 6.6) = -1.6
        (10 - 6.6) = 3.4
        (8 - 6.6) = 1.4
    y   (1 - 4.4) = -3.4
        (4 - 4.4) = -0.4
        (3 - 4.4) = -1.4
        (8 - 4.4) = 3.6
        (6 - 4.4) = 1.6
3.  -3.6 * -3.4 = 12.24
    0.4 * -0.4 = -0.16
    -1.6 * -1.4 = 2.24
    3.4 * 3.6 = 12.24
    1.4 * 1.6 = 2.24
4.  12.24 + -0.16 + 2.24 + 12.24 + 2.24 = 28.8
5.  28.8 / 5 = 5.76

### Régression linéaire

Régression linéaire consiste à déterminer l'équation suivante :
    y = ax + b
        a est le coefficient directeur de la pente
        b est l'ordonnée à l'origine lorsque x = 0

Calcul de la pente: a = Cov(x,y) / Var(x)

Calcul de l'origine: b = y.moyenne - a * x.moyenne

Exemple avec les échantillons suivants :  x[3, 7, 5, 10, 8] y[1, 4, 3, 8, 6]
1. Moyennes :
    x.moyenne = 6.6
    y.moyenne = 4.4
2. Covariance :
    Cov(x,y) = 5.76
3. Variance :
    Var(x) = 6.04
4.  Pente a:
    a = 5.76 / 6.04 = 0.95364
5.  Ordonnée à l'origine b :
    b = 4.4 - (0.95364 * 6.6) = -1.89
6.  Équation de la droite :
    y = 0.953 * x - 1.89

## Calcul descente de gradient

### Objectif

Minimiser l'erreur entre prédiction et valeurs réelles (cost function)

### Implémentation

# Lecture des données
mileage = [m1, m2, ..., mn]
price = [p1, p2, ..., pn]

# Initialisation des paramètres
theta0 = 0
theta1 = 0
learning_rate = 0.01
max_iterations = 1000

# Entraînement
for iteration in range(max_iterations):
    # Calcul des gradients
    sum_errors = 0
    sum_errors_mileage = 0
    for i in range(len(mileage)):
        error = (theta0 + theta1 * mileage[i]) - price[i]
        sum_errors += error
        sum_errors_mileage += error * mileage[i]
    
    # Mise à jour des paramètres
    tmp_theta0 = theta0 - learning_rate * (1 / len(mileage)) * sum_errors
    tmp_theta1 = theta1 - learning_rate * (1 / len(mileage)) * sum_errors_mileage
    
    # Mise à jour simultanée
    theta0 = tmp_theta0
    theta1 = tmp_theta1

# Sauvegarder les paramètres
save_to_file(theta0, theta1)


