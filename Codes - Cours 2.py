#%% Exercice de révision de 2.1

#Code pour calculer l'aire d'un triangle
base = 5
hauteur = 10

aire_triangle = base*hauteur/2

print(aire_triangle)
#%%
#Code pour calculer l'aire d'un carré
longueur_coté = 10

aire_carré = longueur_coté*longueur_coté

print(aire_carré)

#%%

1+5*(3+2)
     
#%%

4**(1/2)

#%%

2.5 + 3

#%%

2,5 + 3

#%% Exercice 2.2: Arithmétique

réponse_a = (2 - 5**2) / (1 + 3**3)
print(réponse_a)

#%%

réponse_b = (7 * (2**3 + 4))**(1/3) + 12
print(réponse_b)

#%%

réponse_c = (3.5E6 + 4.1E7)**2 / (1.9E-3)**(2/3)
print(réponse_c)

#%%

réponse_d = (-3 + (3**2 - 4*2*(-5))**(1/2)) / (2*2)
print(réponse_d)

#%%

a = 2
b = 3
c = -5

quadratique_plus = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
quadratique_moins = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print(quadratique_plus)
print(quadratique_moins)

#%%

base = 5
BASE = 10
Base = 15

print(base)
print(BASE)
print(Base)

#%%

a = 5
b = 2.3
c = 'canada'

print(type(a))
print(type(b))
print(type(c))

#%%

nom = 'David'
age = 28

print('Mon nom est ' + nom)

print('Mon âge est ' + str(age) + ' ans.')

#%% Exercice 2.3: Opération entre variables

a = 5
b = '40'
c = 2.0
d = 'salut'
e = 'bonjour'

#%%

réponse_1 = a + 3*c*a
print(réponse_1)

#%%

réponse_2 = a*b - 5*c
print(réponse_2)

#%% Correction des erreurs

réponse_2 = a*int(b) - 5*c
print(réponse_2)

#%%

réponse_3 = d*a + e
print(réponse_3)

#%%

réponse_4 = e + b*2 + d
print(réponse_4)

#%%

réponse_5 = (e + d)*c + a
print(réponse_5)

#%% Correction des erreurs

réponse_5 = (e + d)*int(c) + str(a)
print(réponse_5)

#%%

import math
import scipy.constants as cst

print(math.pi)
print(math.e)

print(cst.g)
print(cst.c)
print(cst.Avogadro)

#%%

x = 3
print(x)

#%%

x = 5
print(x)

#%%

x = 2*x
print(x)

#%%

del x
print(x)

#%%


