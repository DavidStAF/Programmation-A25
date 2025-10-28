#%% Question 1 - Roche-papier-ciseaux

import random

rpc = ['roche', 'papier', 'ciseaux']
points = [0,0] # [joueur, ordinateur]

while True:
    
    if max(points) == 3:
        if points[0] == 3:
            print('Bravo vous avez gagné!')
        else:
            print('Désolé vous avez perdu!')
        break
    
    choix = input('Choisir roche, papier ou ciseaux: ')
    ordi = random.choice(rpc)
    print(f'Ordinateur choisi {ordi}.')
    
    if choix == ordi:
        print('Match nul.')
    
    elif choix == 'roche':
        if ordi == 'papier':
            points[1] += 1
        else:
            points[0] += 1
            
    elif choix == 'papier':
        if ordi == 'ciseaux':
            points[1] += 1
        else:
            points[0] += 1
            
    elif choix == 'ciseaux':
        if ordi == 'roche':
            points[1] += 1
        else:
            points[0] += 1
    
    else:
        print('Choix invalide.')
     
    print(f'Vous: {points[0]} VS Ordinateur: {points[1]}')
             
#%% Question 2 - Approximer une intégrale
    
import random

dessous = 0

for i in range(1000000):
    randx = random.uniform(0, 3)
    randy = random.uniform(0, 9)
    
    if randy < randx**2:
        dessous += 1

print(f'Aire = {(dessous/1000000) * 27}') # Aire de x**2 entre 0 et 3

#%%
import math

dessous = 0

for i in range(1000000):
    randx = random.uniform(0, 1.5)
    randy = random.uniform(0, 1)
    
    if randy < math.sin(randx**2):
        dessous += 1

print(f'Aire = {dessous/1000000*1.5}') # Aire de sin(x**2) entre 0 et 1.5

#%% Question 3 - Encryptage et décryptage

lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encryption = {}

for i in range(len(lettres)):
        encryption[lettres[i]] = lettres[(i + 5)%26]

mot_secret = 'Ce message secret ne doit pas être intercepté!'
mot_crypté = ''

for élément in mot_secret:
    if élément in encryption:
        mot_crypté += encryption[élément]
    else:
        mot_crypté += élément      
print(mot_crypté)

#%%

decryption = {}

for i in range(len(lettres)):
        decryption[lettres[i]] = lettres[(i - 5)%26]
 
mot_inconnu_crypté = 'Bwfat, yz fx wézxxn à iéhwnuyjw hj rjxxflj!'
mot_inconnu_décrypté = ''        

for élément in mot_inconnu_crypté:
    if élément in decryption: 
        mot_inconnu_décrypté += decryption[élément]
    else:
        mot_inconnu_décrypté += élément
print(mot_inconnu_décrypté)

#%% Question 4 - Tableau de notes 

import numpy as np

note = np.array([[68,83,57],
                 [96,67,86],
                 [59,74,70],
                 [77,89,41],
                 [81,91,74]])

note_max = note.max()
note_min = note.min()
print('Note la plus élevée:', note_max)
print('Note la plus basse:', note_min)

note[:,0] += 2
note[note > 90] -= 5 
print(note)

moyenne_groupes = note.mean(axis=0)
std_groupes = note.std(axis=0)
print('Moyenne des groupes:',moyenne_groupes)
print('Écart-type des groupes:',std_groupes)

def cote_z(note, moyenne, std):
    return (note - moyenne) / std

cote_z = cote_z(note, note.mean(), note.std())
print('Cote Z des personnes:')
print(cote_z)

#%% Question 5 - Cinématique en 2D

# Code de base en 1D

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

#%% 

# Code modifié pour analyser le mouvement en 2D

import scipy.constants as cst

t = 0
x = 0
y = 5
vx = 20*math.cos(math.radians(35))
vy = 20*math.sin(math.radians(35))
ax = 0
ay = -cst.g

temps = [t]
position_x = [x]
position_y = [y]
vitesse_x = [vx]
vitesse_y = [vy]
accélération_x = [ax]
accélération_y = [ay]

delta_t = 0.001

while y > 0:
    t += delta_t
    x += vx*delta_t
    y += vy*delta_t + 1/2*ay*delta_t**2
    vx += ax*delta_t
    vy += ay*delta_t
    ax = 0
    ay = -cst.g

    temps.append(t)
    position_x.append(x)
    position_y.append(y)
    vitesse_x.append(vx)
    vitesse_y.append(vy)
    accélération_x.append(ax)
    accélération_x.append(ay)

hauteur_max = max(position_y)
temps_hauteur_max = temps[position_y.index(hauteur_max)]

distance_horizontale = position_x[-1]
temps_sol = temps[-1]

module_vit_sol = (vitesse_x[-1]**2 + vitesse_y[-1]**2)**(1/2)

print(f'Hauteur maximale: {hauteur_max:.3f} m à {temps_hauteur_max:.3f} s')
print(f'Distance horizontale: {distance_horizontale:.3f} m à {temps_sol:.3f} s')
print(f'Module de la vitesse au sol: {module_vit_sol:.3f} m/s')

#%%