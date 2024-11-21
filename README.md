# Variance - Formule et Définition

## Qu'est-ce que la variance ?

La variance est une mesure de la dispersion des valeurs dans un ensemble de données. Elle indique dans quelle mesure les valeurs s'écartent de la moyenne. Une faible variance signifie que les valeurs sont proches de la moyenne, tandis qu'une variance élevée signifie que les valeurs sont plus dispersées.

### Définition :
La variance d'un ensemble de données est la moyenne des carrés des écarts entre chaque valeur et la moyenne de l'ensemble de données.

## Formule de la Variance

La formule pour calculer la variance (\(\sigma^2\)) d'un ensemble de données est :

### Pour un échantillon :

\[
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
\]

### Pour une population :

\[
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
\]

### Où :
- \(s^2\) est la variance de l'échantillon,
- \(\sigma^2\) est la variance de la population,
- \(x_i\) est la \(i\)-ème valeur dans l'ensemble de données,
- \(\bar{x}\) est la moyenne de l'échantillon,
- \(\mu\) est la moyenne de la population,
- \(n\) est le nombre d'observations dans l'échantillon,
- \(N\) est le nombre d'observations dans la population.

## Exemple de calcul

Supposons que nous ayons les valeurs suivantes dans un échantillon : [3, 7, 5, 10, 8].

1. **Calcul de la moyenne** (\(\bar{x}\)) :
   \[
   \bar{x} = \frac{3 + 7 + 5 + 10 + 8}{5} = 6.6
   \]

2. **Calcul des écarts à la moyenne** et de leur carré :
   - \((3 - 6.6)^2 = 13.96\)
   - \((7 - 6.6)^2 = 0.16\)
   - \((5 - 6.6)^2 = 2.56\)
   - \((10 - 6.6)^2 = 11.56\)
   - \((8 - 6.6)^2 = 1.96\)

3. **Somme des carrés des écarts** :
   \[
   13.96 + 0.16 + 2.56 + 11.56 + 1.96 = 30.2
   \]

4. **Calcul de la variance** :
   \[
   s^2 = \frac{30.2}{5 - 1} = \frac{30.2}{4} = 7.55
   \]

Ainsi, la variance de cet échantillon est \(7.55\).

## Conclusion

La variance est une mesure clé en statistique, utilisée pour quantifier l'étendue de la dispersion des données. Une variance élevée indique une grande dispersion des valeurs, tandis qu'une variance faible indique que les valeurs sont plus concentrées autour de la moyenne.
