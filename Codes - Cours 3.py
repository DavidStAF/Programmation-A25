#%% Exercice de révision de 2.2 et 2.3

import scipy.constants as cst
import math

masse_proton = cst.m_p
energie_proton = masse_proton*cst.c**2
print('L\'énergie relâchée par un proton est ' + str(energie_proton) + ' Joules')
#%%
aire_cercle = 100 
rayon = (aire_cercle/math.pi)**(1/2)
print('Le rayon d\'un cercle avec une aire de ' + str(aire_cercle) + ' est ' + str(rayon))

#%% 

prénom = input('Quel est ton prénom? ')

print('Bonjour ' + prénom + ', je suis Python !')

#%%

nombre = float(input('Entrez un nombre pour trouver sa racine: '))
racine = nombre**(1/2)

print('La racine de ' + str(nombre) + ' est ' + str(racine))

#%%

jour = 5
mois = 'Septembre'
année = 2025

print(f'Nous sommes le {jour} {mois} {année}')

#%%

x = 4.176**10

print(x)
print(f'{x:e}')
print(f'{x:.2e}')
print(f'{x:.2f}')
print(f'{x:.5}')

#%% Exercice 2.4: input et print
    
nombre = float(input('Entrez un nombre: '))

racine = nombre**(1/2)
carré = nombre**2
cube = nombre **3

print(f'La racine de {nombre} est {racine:.2f}')
print(f'Le carré de {nombre} est {carré:.3e}')
print(f'Le cube de {nombre} est {cube:.5}')

#%%

def fonction(argument_1, argument_2, argument_3):

    bla
    blabla

    return blablabla

#%%

def carré(x):
    return x**2

#%%

réponse = carré(2)
print(réponse)
print(carré(5))
#%%

def racine_carré(nombre):
    racine_nombre = nombre**(1/2)
    return racine_nombre

print(racine_nombre)
#%%

def racine_carré(nombre):
    return nombre**(1/2)
    
#%%

print(racine_carré(25))
print(racine_carré(81))
print(racine_carré(144))

#%%

test_5 = racine_carré(25)
test_9 = racine_carré(81)
test_12 = racine_carré(144)

print(test_5 + test_9)

#%%

def fonction(x, y):
    return x * y / 2

#%%

def aire_triangle(base, hauteur):
    return (base * hauteur) / 2

#%%

import math

def aire_cercle(rayon):
    
    pi = math.pi
    aire = pi*rayon**2
    
    return aire


print(aire_cercle(0))
print(aire_cercle(1))
print(aire_cercle(1/math.pi**(1/2)))

#%%

def somme_produit(nombre1, nombre2):
    
    somme_nombres = nombre1 + nombre2
    produit_nombres = nombre1*nombre2
    
    return somme_nombres, produit_nombres

#%%

somme, produit = somme_produit(5, 5)

print(f'La somme est {somme}')
print(f'Le produit est {produit}')

#%%

def saluer_utilisateur(nom):
    print('Bonjour', nom)
    print('Bienvenue!')


saluer_utilisateur('Bob')

#%%

def bienvenue():
    nom = input('Quel est votre nom? ')
    print('Bonjour', nom, '!')

bienvenue()

#%%

réponse = math.sin(math.radians(45))

print(réponse)

#%%

dir(math)

#%%

help(math.cbrt)

#%%

pi = math.pi

print(math.sin(pi/2))
print(math.cos(pi/2))

#%%

print(math.radians(45))
print(math.radians(90))

#%%

print(math.degrees(math.pi))
print(math.degrees(3/2*math.pi))

#%% Exercice 2.5: Création de fonctions

def distance_parcourue(pos_initial, pos_finale):
    return abs(pos_finale - pos_initial)

print(distance_parcourue(10, 10))
print(distance_parcourue(10, 20))
print(distance_parcourue(20, 10))

#%%

def logarithmes():
    import math
    nombre = float(input('Entrez un nombre: '))
    
    print(f'Logarithme en base e:   {math.log(nombre)}')
    print(f'Logarithme en base 10:  {math.log10(nombre)}')
    print(f'Logarithme en base 2:   {math.log(nombre, 2)}')

logarithmes()

#%%

def trigo(angle_degrés):
    angle_rads = math.radians(angle_degrés)
    
    sinus = math.sin(angle_rads)
    cosinus = math.cos(angle_rads)
    tangente = math.tan(angle_rads)
    
    return sinus, cosinus, tangente

sin, cos , tan = trigo(45) 

print(sin/cos)
print(tan)

#%%


