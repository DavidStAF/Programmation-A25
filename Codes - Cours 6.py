#%% Exercice de révision: Section 4.1

notes_math = {'Bob':[78, 95, 67], 'Mathis':[54, 91, 62],
              'Sarah':[94, 50, 74], 'Eve':[98, 83]}

print('Notes de Mathis:', notes_math['Mathis'])

notes_math['Sarah'][0] += 5
notes_math['Sarah'][1] += 5
notes_math['Sarah'][2] += 5
print('Notes modifiées de Sarah:', notes_math['Sarah'])
#%%
print('Moyenne de Bob:', sum(notes_math['Bob']) / len(notes_math['Bob']))

notes_math['Jimmy'] = [89, 97, 95]
print(notes_math)
#%%
notes_math['Eve'].append(91)

print(notes_math)

#%% Boucle for sur les indices
     
nombres = [4, 8, 9, 15, 20]

n = len(nombres)

for i in range(n):
    print(nombres[i])
    
#%% Boucle for sur les indices - Plus concis

nombres = [4, 8, 9, 15, 20]

for i in range(len(nombres)):
    print(nombres[i])

#%% Boucle for sur les éléments

nombres = [4, 8, 9, 15, 20]

for patate in nombres:
    print(patate)

#%% Boucle for sur les éléments - Plus explicite
 
nombres = [4, 8, 9, 15, 20]

for élément in nombres:
    print(élément)

#%% Boucle for sur les éléments avec un dictionnaire

age = {'David': 28, 'Steve': 25, 'Bob': 22, 'Charlie': 31}

for nom in age:
    print(nom)
    print(age[nom])

#%% Opération sur tous les éléments

notes = [88, 53, 62, 68, 69, 59, 94, 72, 75, 76]

for i in range(len(notes)):
    notes[i] += 2

print(notes)

#%% Opération avec condition

notes_examen = [34, 87, 67, 43, 50, 90, 54, 46, 14, 78]

for i in range(len(notes_examen)):
    if notes_examen[i] < 40:
        notes_examen[i] += 10
    elif notes_examen[i] < 50:
        notes_examen[i] += 5

print(notes_examen)

#%% Application: Trouver un élément

prénoms = ['Bob', 'David', 'Charlie', 'Alice', 'David', 'Robert', 'Samuel', 'David']

recherche = 'David'

for i in range(len(prénoms)):
    if prénoms[i] == recherche:
        print(i, end = ' ')

#%% Condition avec dictionnaire

biscuits_avoine = {'oeuf': 1, 'miel': '170 g', 'beurre': '112 g',
                   'farine': '145 g','avoine': '130 g', 
                   'cannelle': '1.5 tsp', 'poudre_pâte': '1.5 tsp'}

ingrédient = 'miel'

if ingrédient in biscuits_avoine:
    print(biscuits_avoine[ingrédient])
else:
    print('Pas de', ingrédient)
    
#%% Trouver valeur minimale avec boucle for

import math

minimum = math.inf

notes = [88, 53, 62, 68, 69, 59, 94, 72, 75, 76]

for i in range(len(notes)):
    if notes[i] < minimum:
        minimum = notes[i]

print('Valeur minimale:', minimum)

#%% Trouver valeur maximale avec boucle for

import math

maximum = -math.inf

notes = [88, 53, 62, 68, 69, 59, 94, 72, 75, 76]

for i in range(len(notes)):
    if notes[i] > maximum:
        maximum = notes[i]

print('Valeur maximale:', maximum)

#%% Trouver la somme et la moyenne avec boucle for

notes = [88, 53, 62, 68, 69, 59, 94, 72, 75, 76]



for élément in notes:
    somme += élément
    taille += 1

print('Somme:', somme)
print('Moyenne:', somme/taille)

#%% Trouver les indices d'un élément recherché

prénoms = ['Bob', 'David', 'Charlie', 'Alice', 'David', 'Robert', 'Samuel', 'David']

recherche = 'David'
indices_recherche = []

for i in range(len(prénoms)):
    if prénoms[i] == recherche:
        indices_recherche.append(i)

print(indices_recherche)

#%% Calculer le déplacement à partir de la position

position = [0, 2, 5, 9, 9,  12, 17, 25]
déplacement = []

for i in range(len(position) - 1):
    valeur_déplacement = position[i+1] - position[i] 
    déplacement.append(valeur_déplacement)

print(déplacement)

#%% Exercice: Séquence d'ADN

ADN = '''ttgaatctggctaaccccttgacttgctctggcatggcaggc
agctcaatgtcactcgatgtcaattttccccctctgtcgaaggagctagcggactacgaa
tcctatacgatacactgcctctgtgacctcaatgaatatamtgacggtgctcgaccgcgt
ggacgtccggtatcgtcctgtgccagaggaggcttttctgcctgcggccacgtttagggg
aatcgacgagtttctacttgcagagtctgacattggaacggcctctattaattttacagg
actctgaccgmgtcgtggccctgccatagcccgagctcaattagtgccaaccactaacag
aacgaagaaaaacaccgatgctgcgtgactagtccgmttttatatagaatcggggtacct
accagtgatcgggggtccgggactcacctaaagtaatacccgatagtctacattggggaa
ctaatcataatgtaactgcaccaggcctacacagggctcctacgttttgggagttatatg
gacatatgccctttaacggctgtgggtgtggccatagtgtgcagccacttctactc'''    

nombre_a = 0
nombre_t = 0
nombre_c = 0
nombre_g = 0

position_m = []

ARN = ''

for i in range(len(ADN)):
    
    if ADN[i] == 'a':
        nombre_a += 1
        ARN += 'a'
        
    elif ADN[i] == 't':
        nombre_t += 1
        ARN += 'u'
        
    elif ADN[i] == 'c':
        nombre_c += 1
        ARN += 'c'
        
    elif ADN[i] == 'g':
        nombre_g += 1
        ARN += 'g'
    
    if ADN[i] == 'm':
        position_m.append(i)
    

print('Nombres de bases:')
print('a:', nombre_a)
print('t:', nombre_t)
print('c:', nombre_c)
print('g:', nombre_g)
print('Position des bases mutantes:', position_m,'et nombre de m:', len(position_m))
print('Séquence d\'ARN:', ARN)

#%% Exercice: Séquence d'ADN - Version utilisant un dictionnaire

ADN = '''ttgaatctggctaaccccttgacttgctctggcatggcaggc
agctcaatgtcactcgatgtcaattttccccctctgtcgaaggagctagcggactacgaa
tcctatacgatacactgcctctgtgacctcaatgaatatamtgacggtgctcgaccgcgt
ggacgtccggtatcgtcctgtgccagaggaggcttttctgcctgcggccacgtttagggg
aatcgacgagtttctacttgcagagtctgacattggaacggcctctattaattttacagg
actctgaccgmgtcgtggccctgccatagcccgagctcaattagtgccaaccactaacag
aacgaagaaaaacaccgatgctgcgtgactagtccgmttttatatagaatcggggtacct
accagtgatcgggggtccgggactcacctaaagtaatacccgatagtctacattggggaa
ctaatcataatgtaactgcaccaggcctacacagggctcctacgttttgggagttatatg
gacatatgccctttaacggctgtgggtgtggccatagtgtgcagccacttctactc'''    

nombre_bases = {'a': 0, 't': 0, 'c': 0, 'g': 0}

position_m = []

ARN = ''

for i in range(len(ADN)):
    if ADN[i] in nombre_bases:
        nombre_bases[ADN[i]] += 1
        if ADN[i] == 't':
            ARN += 'u'
        else:
            ARN += ADN[i]
        
    if ADN[i] == 'm':
        position_m.append(i)
    

print('Nombres de bases:', nombre_bases)
print('Position des bases mutantes:', position_m,'et nombre de m:', len(position_m))
print('Séquence d\'ARN:', ARN)

#%% Mouvement vertical 1D sans air

import scipy.constants as cst

t = 0 
y = 2
v = 10
a = -cst.g

temps = [t]
position = [y]
vitesse = [v]
accélération = [a]

delta_t = 0.001

while y > 0:
    t += delta_t
    y += v*delta_t + 1/2*a*delta_t**2
    v += a*delta_t
    a = -cst.g
    
    temps.append(t)
    position.append(y)
    vitesse.append(v)
    accélération.append(a)

hauteur_max = max(position)
temps_hauteur_max = temps[position.index(hauteur_max)]
temps_sol = temps[-1]
vitesse_sol = vitesse[-1]

print(f'Hauteur maximale de {hauteur_max:.3f} m après {temps_hauteur_max:.3f} s.')
print(f'Touche le sol après {temps_sol:.3f} s à {vitesse_sol:.3f} m/s.')

#%%  Mouvement vertical 1D avec frottement de l'air

masse = 80
aire = 0.8
CD = 1
rho = 1.225

t = 0
y = 2
v = 10
a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

temps = [t]
position = [y]
vitesse = [v]
accélération = [a]

delta_t = 0.001

while y > 0:
    t += delta_t
    y += v*delta_t + 1/2*a*delta_t**2
    v += a*delta_t
    a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

    temps.append(t)
    position.append(y)
    vitesse.append(v)
    accélération.append(a)

hauteur_max = max(position)
temps_hauteur_max = temps[position.index(hauteur_max)]
temps_sol = temps[-1]
vitesse_sol = vitesse[-1]

print(f'Hauteur maximale de {hauteur_max:.3f} m après {temps_hauteur_max:.3f} s.')
print(f'Touche le sol après {temps_sol:.3f} s à {vitesse_sol:.3f} m/s.')

#%%  Exercice: Saut en altitude - 1)

masse = 90
aire = 1.2
CD = 0
rho = 1.225

t = 0
y = 100
v = 0
a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

temps = [t]
position = [y]
vitesse = [v]
accélération = [a]

delta_t = 0.001

while y > 0:
    t += delta_t
    y += v*delta_t + 1/2*a*delta_t**2
    v += a*delta_t
    a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

    temps.append(t)
    position.append(y)
    vitesse.append(v)
    accélération.append(a)

temps_sol = temps[-1]
vitesse_sol = vitesse[-1]

print('Réponse 1):')
print(f'Touche le sol après {temps_sol:.3f} s à {vitesse_sol:.5f} m/s.')

#%%  Exercice: Saut en altitude - 2)

masse = 90
aire = 1.2
CD = 0.9
rho = 1.225

t = 0
y = 100
v = 0
a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

temps = [t]
position = [y]
vitesse = [v]
accélération = [a]

delta_t = 0.001

while y > 0:
    t += delta_t
    y += v*delta_t + 1/2*a*delta_t**2
    v += a*delta_t
    a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

    temps.append(t)
    position.append(y)
    vitesse.append(v)
    accélération.append(a)

temps_sol = temps[-1]
vitesse_sol = vitesse[-1]

print('Réponse 2):')
print(f'Touche le sol après {temps_sol:.3f} s à {vitesse_sol:.5f} m/s.')

#%%  Exercice: Saut en altitude - 3)

# La vitesse tend vers une valeur de -36.53 m/s
# lorsque la hauteur est augmentée, car il s'agit
# de la vitesse terminale de l'objet. C'est à cette vitesse que 
# la force gravitationnelle et la force de frottement de l'air
# deviennent égales, et l'accélération devient nulle.
# Donc, la vitesse reste constante.

#%%  Exercice: Saut en altitude - 4)

masse = 90
aire = 1.2
CD = 0.9
rho = 1.225

t = 0
y = 1000
v = 0
a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

temps = [t]
position = [y]
vitesse = [v]
accélération = [a]

delta_t = 0.001

while y > 0:
    
    if y < 250:
        aire = 20
        CD = 3
    
    t += delta_t
    y += v*delta_t + 1/2*a*delta_t**2
    v += a*delta_t
    a = -cst.g - 1/2*aire*CD*rho*v*abs(v)/masse

    temps.append(t)
    position.append(y)
    vitesse.append(v)
    accélération.append(a)

temps_sol = temps[-1]
vitesse_sol = vitesse[-1]

print('Réponse 4)')
print(f'Touche le sol après {temps_sol:.3f} s à {vitesse_sol:.3f} m/s.')

#%%