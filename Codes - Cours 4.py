import math

#%%

if condition:
    bla
    blabla
    blablabla

#%% if

nombre = 5

if nombre > 10:
    print("Ce nombre est plus grand que 10")

print("Terminé!")

#%% if et elif

nombre = 5

if nombre > 10:
    print("Ce nombre est plus grand que 10")
else:
    print("Ce nombre n'est pas plus grand que 10")
    
print("Terminé!")

#%% if, elif et else

nombre = 10

if nombre > 10:
    print("Ce nombre est plus grand que 10")
elif nombre < 10:
    print("Ce nombre est plus petit que 10")
else:
    print("Ce nombre est égal à 10")

print("Terminé!")
    
#%% Plusieurs elif

nombre = 123

if nombre > 1000:
    print("Ce nombre est plus grand que 1000")
elif nombre > 100:
    print("Ce nombre est plus grand que 100")
elif nombre > 10: 
    print("Ce nombre est plus grand que 10")
elif nombre == 10:
    print("Ce nombre est égal à 10")
else:
    print("Ce nombre est plus petit que 10")

print("Terminé!")

#%% Plusieurs if

nombre = 123

if nombre > 1000:
    print("Ce nombre est plus grand que 1000")
if nombre > 100:
    print("Ce nombre est plus grand que 100")
if nombre > 10: 
    print("Ce nombre est plus grand que 10")
if nombre == 10:
    print("Ce nombre est égal à 10")

print("Terminé!")

#%% Erreur possible

nombre = 1200

if nombre > 100:
    print("Ce nombre est plus grand que 100")
elif nombre > 1000:
    print("Ce nombre est plus grand que 1000") # Cette condition ne sera jamais VRAIE 
elif nombre > 10: 
    print("Ce nombre est plus grand que 10")
elif nombre == 10:
    print("Ce nombre est égal à 10")
else:
    print("Ce nombre est plus petit que 10")

print("Terminé!")

#%% Conditions et comparaisons

test_nombre = 19

if test_nombre == 0:
    print('Le nombre est 0')
elif test_nombre > 0:
    print('Le nombre est positif')
elif test_nombre < 0:
    print('Le nombre est négatif')

#%% Exercice 3.1: Identification

prénom = 'David'
age = 28

if age > 123:
    print('Cet âge est impossible!')
elif age >=18:
    print('Vous avez le droit de voter!')
else:
    print('Désolé, vous n\'avez pas le droit de voter.')

if prénom == 'David':
    print('Bonjour David!')
else:
    print('Vous n\'êtes pas David!')

print('Bonne journée!')

#%% Mot clé and

prénom = 'David'
age = 28

if prénom == 'David' and age == 28:
    print('Identification réussie!')
else:
    print('Identification échouée!')

#%% Plusieurs mot clé and

prénom = 'David'
nom = 'St-Amant'
age = 28

if prénom == 'David' and nom == 'St-Amant' and age == 28:
    print('Identification réussie!')
else:
    print('Identification échouée!')

#%% Mot clé or

age = 28

if age <= 10 or age >= 65:
    print('Vous avez droit à un rabais!')
else:
    print('Désolé, aucun rabais disponible.')

#%% Combiner and et or

age = 28
jour = 'Samedi'

if (age <= 10 or age >= 65) and (jour == 'Samedi' or jour == 'Dimanche'):
    print('Vous avez droit à un rabais!')
else:
    print('Désolé, aucun rabais disponible.')

#%% Mot clé not

age = 28

if not age < 18:
    print('Vous êtes majeur.')
else:
    print('Vous êtes mineur.')
    
#%% 

for i in range(5):
    print(i)

#%%

for i in range(0, 10, 2):
    print(i)

#%%

for i in range(1, 10, 2):
    print(i)

#%%

for i in range(10, 26, 5):
    print(i)

#%%

for i in range(5):
    print(i, end=' ')

#%%

for i in range(5):
    print(i, end=', ')

#%%

for i in range(5):
    print(i, end='$ ')

#%%

# Faire la somme des nombres entre 0 et n
n = 10
somme = 0
for i in range(1, n + 1, 1):
    somme += i
print(somme)

#%%

# Doubler n fois la valeur d'un nombre au choix
nombre = 2
n = 5
for i in range(5):
    nombre *= 2
print(nombre)

#%% Boucle avec somme des nombres entrés

somme = 0
nombre = ''
while nombre != '0':
    nombre = input('Entrez un nombre ou 0 pour quitter: ')
    somme += float(nombre)
    print(f'La somme est rendue à {somme}')

print('Merci, au revoir!')

#%% Fonction factorielle

n = 5
factorielle = 1
while n != 0:
    factorielle *= n
    n -= 1
print(f'La fonction factorielle est {factorielle}')

#%% Boucle infinie

a = 2
x = 0
while a < 10:
    x += a
    print(x)

#%% Exemple de break avec boucle for

for i in range(10):
    if i == 8:
        print('Arrivé à break')
        break
    else:
        print('La valeur de i est', i)

#%% Exemple de break avec boucle while

while True:
    nombre = float(input('Entrez un nombre positif pour trouver sa racine : '))
    if nombre < 0:
        print('Ce n\'est pas un nombre positif.')
    else:
        print(f'La racine de {nombre} est {math.sqrt(nombre)}')
        break

print('Boucle terminée, bonne journée!')

#%% Exemple de continue avec boucle for

for i in range(10):
    if i == 5:
        print('Arrivé à continue')
        continue
    print('La valeur de i est', i)

#%% Exemple de continue avec boucle while

compteur = 0

while True:
    nombre = float(input('Entrez un nombre positif ou 0 pour quitter: '))
    if nombre == 0:
        break
    elif nombre < 0:
        print(f'Vous avez entré {compteur} nombres positifs jusqu\'à présent.')
        continue
    else:
        compteur += 1
        print(f'Vous avez entré {compteur} nombres positifs jusqu\'à présent.')

print('Boucle terminée, bonne journée!')

#%%

for i in range(1, 11, 1):
    for j in range(1, 11, 1):
        print(f'{i * j:3d}', end = ' ')
    print()

#%% Exercice 3.2: Nombres premiers - Avec boucle for

nombre_choisi = int(input("Entrer un nombre entier : "))

# Déterminer si le nombre choisi est premier ou pas
for n in range(2, nombre_choisi):
    if nombre_choisi % n == 0: # Vérifie si le nombre choisi est divisible par n
        print(f"Le nombre {nombre_choisi} n'est pas premier.")
        break
    elif n == nombre_choisi - 1: # Si aucun n divise le nombre choisi, il est premier
        print(f"Le nombre {nombre_choisi} est premier.")
    else:
        continue

#%% Exercice 3.2: Nombres premiers - Avec boucle while

nombre_choisi = int(input("Entrer un nombre entier : "))

# Déterminer si le nombre choisi est premier ou pas
n = 2
while True:
    if nombre_choisi % n == 0: # Vérifie si le nombre choisi est divisible par n
        print(f"Le nombre {nombre_choisi} n'est pas premier.")
        break
    elif n == nombre_choisi - 1: # Si aucun n divise le nombre choisi, il est premier
        print(f"Le nombre {nombre_choisi} est premier.")
        break
    else:
        n += 1

#%%