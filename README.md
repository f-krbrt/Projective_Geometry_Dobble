# Générateur de jeu Dobble avec la Géométrie Projective

Ce projet implémente un générateur de cartes pour le jeu **Dobble** (aussi connu sous le nom de **Spot It**) en utilisant les principes de la géométrie projective sur le corps fini **ℤ/3ℤ**.

## 📋 Description

Le jeu Dobble est un jeu de cartes où chaque paire de cartes partage exactement un symbole en commun. Ce programme utilise la géométrie projective pour générer mathématiquement un jeu de cartes respectant cette propriété fondamentale.

### Principe mathématique

Le programme s'appuie sur la géométrie projective dans l'espace projectif **ℙ³(ℤ/3ℤ)** :
- Les **points** représentent les cartes du jeu
- Les **plans** (ou hyperplans) représentent les symboles
- Un point appartient à un plan si et seulement si le symbole correspondant apparaît sur la carte

La propriété clé : deux plans distincts se coupent toujours en exactement un point, garantissant qu'une paire de cartes partage exactement un symbole.

## 🎯 Caractéristiques

- **40 cartes** générées automatiquement
- **40 symboles** différents
- Chaque carte contient **4 symboles**
- Deux cartes quelconques partagent **exactement 1 symbole**

## 🔧 Prérequis

- Python 3.x
- Aucune bibliothèque externe requise

## 🚀 Installation

```bash
git clone https://github.com/votre-nom/projective-geometry-dobble.git
cd projective-geometry-dobble
```

## 💻 Utilisation

```bash
python Projective_Geometry_Dobble.py
```

Le programme génère automatiquement les cartes et affiche :
- La liste complète des points (cartes)
- Les plans associés à chaque point
- Un dictionnaire final associant chaque carte à ses symboles

## 📊 Structure du code

### Classe principale

**`Z3Z`** : Représente un vecteur dans (ℤ/3ℤ)⁴
- `__init__(a,b,c,d)` : Constructeur avec 4 coordonnées modulo 3
- `__add__(other)` : Addition de vecteurs
- `solution(self, other)` : Teste si deux vecteurs sont orthogonaux (produit scalaire ≡ 0 mod 3)
- `show()` : Affiche les coordonnées sous forme de tuple

### Fonctions principales

#### Génération de points
- `liste_points(p)` : Génère tous les points de l'espace projectif
- `tri_pointaffine_pointsinfini(l)` : Trie les points affines et les points à l'infini
- `affiche_liste_points(p)` : Affiche tous les points générés

#### Calcul des plans
- `plans_sol(p, lplan)` : Retourne les plans auxquels appartient un point
- `affiche_plan_sol(p, lplan)` : Affiche les plans contenant un point donné

#### Génération du jeu
- `attribut(symboles, lplan_uplet)` : Associe un symbole unique à chaque plan
- `cartes(lu)` : Numérote les cartes
- `dico_final_image(symbole, l1, l2)` : Génère le dictionnaire final carte → symboles

#### Utilitaires
- `convert(l)` : Convertit une liste de Z3Z en tuples d'entiers
- `meme(l1, l2)` : Trouve les éléments communs à deux listes
- `meme3(l1, l2, l3)` : Trouve les éléments communs à trois listes
- `alignes(a, b, c)` : Vérifie si trois points sont alignés

## 🎨 Liste des symboles

Le jeu utilise 40 symboles différents :
```
livre, barrière, épingle, lettre, lait, ballon, maison, piscine, chaise, horloge, 
église, nouille, oeuf, sac, vache, chaussettes, baleine, oignon, échelle, lunettes, 
tableau, appareil photo, chat, dragon, tomates, ninja, avion, soleil, telephone, 
écharpe, glace, lampadaire, fromage, fusil, poisson, arbre, fleurs, tobogan, fusée, bateau
```

## 📐 Exemple de sortie

```python
# Carte 31
['livre', 'ballon', 'église', 'vache']

# Carte 29
['barriÃ¨re', 'ballon', 'oeuf', 'lunettes']

# Symbole commun entre les cartes 31 et 29
['ballon']
```

## 🧮 Détails mathématiques

### Espace projectif

L'espace projectif ℙ³(ℤ/3ℤ) contient exactement :
```
(3⁴ - 1) / (3 - 1) = 80 / 2 = 40 points
```

### Condition d'incidence

Un point **p = (x, y, z, t)** appartient à un plan **π = (a, b, c, d)** si et seulement si :
```
ax + by + cz + dt ≡ 0 (mod 3)
```

### Propriété de Dobble

Pour deux plans π₁ et π₂ distincts dans ℙ³(ℤ/3ℤ), leur intersection contient exactement un point, garantissant qu'exactement un symbole est partagé entre deux cartes.

## 🔍 Extensions possibles

- Généralisation à d'autres corps finis (ℤ/pℤ avec p premier)
- Interface graphique pour visualiser les cartes
- Export au format PDF imprimable
- Optimisation des symboles pour éviter les confusions visuelles

## 📝 Licence

Ce projet est libre d'utilisation à des fins éducatives et personnelles.



---

**Note** : Pour modifier le nombre de symboles par carte, il faut changer la valeur de `p` (actuellement p=3). Avec p=2, on obtient 5 points (5 cartes) avec 3 symboles par carte. Avec p=5, on obtient 156 cartes avec 6 symboles par carte.
