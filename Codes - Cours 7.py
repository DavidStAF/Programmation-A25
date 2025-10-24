#%% Exercice de révision - Section 4.2

age = [23, 15, 11, 68, 35, 8, 71, 46, 31, 5]
prix = []

for i in range(len(age)):
    if age[i] <= 12:
        prix.append(9)
    elif age[i] >= 65:
        prix.append(10)
    else:
        prix.append(12)

print(prix)
print(f'Montant total à payer: {sum(prix)} $')

#%% Définir un array

import numpy as np


#%%
test_array = np.array([1, 2, 3, 4, 5])

liste = [11, 12, 13, 14, 15]
liste_array = np.array(liste)

print(test_array)
print(liste_array)

#%% Accéder aux éléments d'un array

print(test_array)
print(test_array[0])
print(test_array[2])

print(test_array[0:2])
print(test_array[1:4])

print(test_array[0:4:2])
print(test_array[1:4:2])
print(test_array[0:5:3])

#%% Opérations sur un array

nombres = np.array([10, 20, 30, 40, 50])

ajouter5 = nombres + 5
soustraire15 = nombres - 15
multiplier2 = nombres*2
diviser10 = nombres/10

print(ajouter5)
print(soustraire15)
print(multiplier2)
print(diviser10)

#%% Attention: les opérations ne modifient pas l'array original

print(nombres)

nombres - 10

print(nombres)

#%% Opérations entre deux arrays

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)
print(x - y)
print(x * y)
print(x / y)

#%% Fonctions mathématiques

valeurs = np.array([1, 2, 3, 4, 5])

sinus = np.sin(valeurs)
cosinus = np.cos(valeurs)
exponentielle = np.exp(valeurs)
log_naturelle = np.log(valeurs)
log_base10 = np.log10(valeurs)

print(sinus)
print(cosinus)
print(exponentielle)
print(log_naturelle)
print(log_base10)

#%% Fonctions courantes

valeurs = np.array([1, 2, 3, 4, 5])

print(valeurs.size)
print(valeurs.sum())
print(valeurs.mean())
print(valeurs.std())
print(valeurs.min())
print(valeurs.max())

#%% Trier un array

test = np.array([5, 2, 1, 3, 4])
test.sort()
print(test)

test = np.array([5, 2, 1, 3, 4])
test_trié = np.sort(test)
test_trié_inverse = np.flip(test_trié)
print(test)
print(test_trié)
print(test_trié_inverse)

#%% Copier un array

original = np.array([0, 10, 20, 30, 40])
copie = np.copy(original)
mauvaise_copie = original

original[0] = 123

print(original)
print(copie)
print(mauvaise_copie)

#%% Ajouter des éléments

x = np.array([])
x = np.append(x, 10)
x = np.append(x, 25)
print(x)

x = np.insert(x, 0, 99)
x = np.insert(x, 2, 777)
print(x)

np.append(x, 12345) # Ne modifie pas l'array x
np.insert(x, 0, 12345)
print(x)

#%% Créer un array de 0

array_zéros = np.zeros(10)
print(array_zéros)

#%% Remplacer les valeurs dans un array de 0

for i in range(len(array_zéros)):
    array_zéros[i] = i**2

print(array_zéros)

#%% Conditions avec array et modifications

notes = np.array([74, 54, 89, 23, 34, 99])

sous50 = notes[notes < 50]
haut70 = notes[notes > 70]
print(sous50)
print(haut70)

notes[notes < 60] += 5  # Ajouter 5 aux notes en bas de 60
print(notes)

#%% Array 2D - 2 lignes et 2 colonnes

test2x2 = np.array([[1,2], [4, 5]])
print(test2x2)

#%% Array 2D - 4 lignes et 3 colonnes

test4x3 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(test4x3)

#%% Accéder aux éléments d'un array en 2D

matrice = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(matrice[2,1])
print()
print(matrice[3,:])
print()
print(matrice[:,0])
print()
print(matrice[0:3,1:3])
print()
print(matrice[2:4,0:2])

#%% Fonctions sur array 2D 0 - Exemple avec sum()

test = np.array([[1,2], [3,4]])

print(test)
print(test.sum())
print(test.sum(axis=0))
print(test.sum(axis=1))

#%% Importer le module random

import random

#%% Nombres aléatoires

aléatoire0_1 = random.random()
print(aléatoire0_1)

aléatoire50_100 = random.uniform(50,100)
print(aléatoire50_100)

entier_aléatoire0_10 = random.randint(0, 10)
print(entier_aléatoire0_10)

entier_aléatoire1_5 = random.randint(1, 5)
print(entier_aléatoire1_5)

#%% Choisir au hasard

fruits = ['pomme', 'banane', 'poire', 'raisin', 'fraise']

un_choix = random.choice(fruits)
print(un_choix)

trois_choix = random.choices(fruits, k=3)
print(trois_choix)

#%% Choisir au hasard sans multiple

deux_tirage = random.sample(fruits, k=2)
print(deux_tirage)

quatre_tirage = random.sample(fruits, k=4)
print(quatre_tirage)

#%% Brasser au hasard

nombres = [1, 2, 3, 4, 5]

random.shuffle(nombres)

print(nombres)

#%%