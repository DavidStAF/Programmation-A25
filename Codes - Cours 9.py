#%%
import numpy as np
import matplotlib.pyplot as plt
#import scipy.constants as cst

#%% Exercice de révision - Chapitre 6

plt.subplot(2,2,1) # Sinus
t1 = np.linspace(-np.pi, np.pi, 1000)
y1 = np.sin(t1)
plt.plot(t1, y1, color = 'green')
plt.xlabel('t')
plt.ylabel('sin(t)')
plt.grid()

plt.subplot(2,2,2) # Cosinus
t2 = np.linspace(-2*np.pi, 2*np.pi, 1000)
for a in np.arange(1, 3.5, 0.5):
    plt.plot(t2, np.cos(a*t2), '--', label = f'a = {a}')
plt.xlabel('t')
plt.ylabel('cos(t)')
plt.legend()
plt.grid()

plt.subplot(2,2,3) # Ellipse
t3 = np.linspace(0, 2*np.pi, 1000)
x3 = 2*np.cos(t3)
y3 = 3*np.sin(t3)
plt.plot(x3, y3, ':', color = 'blue')
plt.xlabel('2cos(t)')
plt.ylabel('3sin(t)')
plt.grid()

plt.subplot(2,2,4) # Pétales
t4 = np.linspace(0, np.pi, 1000)
x4 = np.cos(3*t4)*np.cos(t4)
y4 = np.cos(3*t4)*np.sin(t4)
plt.plot(x4, y4, 'x', color = 'red', markevery = 10)
plt.xlabel('cos(3t)cos(t)')
plt.ylabel('cos(3t)sin(t)')
plt.grid()

plt.tight_layout()
plt.show()

#%% Exemple: Cinématique en 1D

cinematique1d = np.loadtxt("cinematique1d.csv", delimiter=";", skiprows=1, usecols=[0,1]) 
print(cinematique1d)

temps = cinematique1d[:,0]
position = cinematique1d[:,1]

plt.plot(temps, position)
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.show()

#%% Exercice: Notes en sciences de la nature

notes = np.loadtxt('notes_sciences.csv', delimiter=';', skiprows=1, usecols=[0,1,2,3])
print(notes)

#%% a) 

moyenne_cours = notes.mean(axis = 0)
print(moyenne_cours)

#%% b)

mediane_cours = np.median(notes, axis = 0)
print(mediane_cours)

#%% c)

ecart_type_cours = notes.std(axis = 0)

cote_z = (notes - moyenne_cours) / ecart_type_cours
print(cote_z)

#%%

print(cote_z[:,1]) #Toutes les lignes de la 2ième colonne (celle de math)

#%% d)

moyenne_etudiants = notes.mean(axis = 1)
print(moyenne_etudiants)

#%% e)

max_moyenne = max(moyenne_etudiants)
min_moyenne = min(moyenne_etudiants)

print(f'La plus haute moyenne générale est {max_moyenne:.0f}%.')
print(f'La plus basse moyenne générale est {min_moyenne:.0f}%.')

#%% Exemple de nuage de points
    
x = np.random.randn(500)
y = np.random.randn(500)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

#%% Exemple de nuage de points complet

x1 = np.random.randn(20)
y1 = np.random.randn(20)

x2 = np.random.randn(40)
y2 = np.random.randn(40)

plt.scatter(x1, y1, marker = '^', color = 'green', s = 80, label = 'Série 1')
plt.scatter(x2, y2, marker = 's', color = 'blue', s = 40, label = 'Série 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()

#%% Importer curve fit

from scipy.optimize import curve_fit

#%%

données = np.loadtxt('sinus_experimental.csv', delimiter = ';', usecols = [0,1])
temps = données[:,0]
position = données[:,1]

def sinus(t, A, w, phi):
    return A*np.sin(w*t + phi)

z, cov = curve_fit(sinus, temps, position)
incertitudes = np.sqrt(np.diag(cov))

print(f'Paramètres de la courbe de tendance: {z}')
print(f'Incertitudes sur les paramètres: {incertitudes}')

#Graphique avec nuage de points et courbe de tendance
plt.scatter(temps, position, color = 'green')
x = np.linspace(min(temps), max(temps), 500)
plt.plot(x, sinus(x, *z), color = 'red')
plt.title(f'Équation de la courbe: {z[0]:.3f}sin({z[1]:.3f}t + {z[2]:.3f})')
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.show()

#%% Exercice: Analyse d'une chute libre

# Importer les données expérimentales dans Python
chute = np.loadtxt('chute_experimentale.csv', delimiter = ';', usecols = [0,1])
temps = chute[:,0]
hauteur = chute[:,1]

# Définir l’équation pour la courbe de tendance d'une chute libre en 1D
def chutelibre(t, y0, vy0, ay):
    return y0 + vy0*t + 1/2*ay*t**2

# Appliquer curve_fit aux données expérimentales
z, cov = curve_fit(chutelibre, temps, hauteur)
incertitudes = np.sqrt(np.diag(cov))

# Imprimer les paramètres de la courbe de tendance et leurs incertitudes.
print(f'Paramètres de la courbe de tendance: {z}')
print(f'Incertitudes sur les paramètres: {incertitudes}')

# Calculer la valeur de la courbe de tendance pour chaque données expérimentales de temps
hauteur_courbe_tendance = chutelibre(temps, *z)

# Calculer la différence entre les hauteurs expérimentales et la courbe de tendance
residus = hauteur - hauteur_courbe_tendance

# Nuage de points expérimental avec courbe de tendance
plt.subplot(2,1,1)
plt.scatter(temps, hauteur, color = 'green')
x = np.linspace(min(temps), max(temps), 500)
plt.plot(x, chutelibre(x, *z), color = 'red')
plt.title(f'Équation de la courbe: {z[0]:.3f} + {z[1]:.3f}t + 1/2*({z[2]:.3f})$t^2$')
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.grid()

# Nuage de points des résidus
plt.subplot(2,1,2)
plt.scatter(temps, residus, color = 'green')
plt.xlabel('Temps (s)')
plt.ylabel('Résidus (m)')
plt.grid()

plt.tight_layout()
plt.show()

#%%