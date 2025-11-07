#%%
import numpy as np
import matplotlib.pyplot as plt

#%% Exemple de graphique avec 5 valeurs

x = np.array([-2, -1, 0, 1, 2])
y = x**2

plt.plot(x,y)
plt.show()

#%% Exemple de graphique avec 9 valeurs

x = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
y = x**2

plt.plot(x,y)
plt.show()

#%% Array de valeurs avec np.linspace()

test1 = np.linspace(0, 5, 10)
print(test1)

#%%

test2 = np.linspace(-2.5, 2.5, 15)
print(test2)

#%% Array de valeurs avec np.arange()

test3 = np.arange(0, 10 + 0.5, 0.5)
print(test3)

#%%

test4 = np.arange(-2, 2 + 0.2, 0.2)
print(test4)

#%% Graphique avec np.linspace()

x = np.linspace(-2, 2, 100)
y = x**2
    
plt.plot(x,y)
plt.show()

#%% Graphique avec fonctions numpy

x = np.linspace(0, 5, 500)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)
y5 = np.log(x)
y6 = np.log10(x)

#plt.plot(x, y1)
#plt.plot(x, y2)
#plt.plot(x, y3)
#plt.plot(x, y4)
#plt.plot(x, y5)
#plt.plot(x, y6)

plt.show()

#%% Graphique avec fonction personnalisée

def sinus_xcarré(x):
    return np.sin(x**2)

x = np.linspace(-5, 5, 500)
y = sinus_xcarré(x)

plt.plot(x, y)
plt.show() 

#%% Ajouter un titre et nommer les axes

t = np.linspace(0, 5, 500)
y = (t**2)*np.sin((t)**(1/2))

plt.title('Courbe de la fonction $t^2$sin($\\sqrt{t}$)')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (m)')

plt.plot(t, y)
plt.show() 

#%% Nommer les courbes et ajouter une légende

x = np.linspace(0, 5, 500)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = 'sin(x)')
plt.plot(x, y2, label = 'cos(x)')

plt.legend()
plt.show()

#%% Modifier les limites des axes

x = np.linspace(0, 5, 500)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = 'sin(x)')
plt.plot(x, y2, label = 'cos(x)')

plt.xlim(0, 5)
plt.ylim(-1.5, 1.5)
plt.legend()
plt.grid()
plt.show()

#%% Exemple de graphique complet avec 2 courbes
    
t = np.linspace(0, 5, 500)
y1 = np.sin(t)
y2 = np.cos(t)
    
plt.plot(t, y1, '+', label = 'sin(t)', color = 'green', lw = 2, alpha = 0.8, markevery = 10)
plt.plot(t, y2, '--', label = 'cos(t)', color = 'red', lw = 6, alpha = 1)

plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (m)')
plt.xlim(0, 5)
plt.ylim(-1.5, 1.5)
plt.legend()
plt.grid()
plt.show()

#%% Exercice: Graphiques d'oscillations

t = np.linspace(0, 10, 1000)

def oscillation_libre(t):
    return 5*np.sin(2*t - np.pi/2)

def oscillation_amortie(t):
    return 5*np.exp(-0.2*t)*np.sin(4*t - np.pi/2)

plt.plot(t, oscillation_libre(t), ':', label = 'Oscillation libre', color = 'blue', lw = 2)
plt.plot(t, oscillation_amortie(t), label = 'Oscillation amortie', color = 'black', lw = 4)

plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (m)')
plt.xlim(0, 10)
plt.ylim(-6, 6)
plt.legend()
plt.grid()
plt.show()

#%%% Exporter automatique une figure

t = np.linspace(0, 5, 500)
y1 = np.sin(t)
y2 = np.cos(t)
    
plt.plot(t, y1, '+', label = 'sin(t)', color = 'green', lw = 2, alpha = 0.8, markevery = 10)
plt.plot(t, y2, '--', label = 'cos(t)', color = 'red', lw = 3, alpha = 0.3)

plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (m)')
plt.xlim(0, 5)
plt.ylim(-1.5, 1.5)
plt.legend()
plt.grid()
plt.savefig('Sincos.png')
plt.show()

#%% Plusieurs courbes avec boucle for

x = np.linspace(-10, 10, 500)

for a in np.arange(1, 6, 0.5):
    plt.plot(x, a*x**2, label= f'a = {a}')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(ncols = 2)
plt.grid()
plt.show()

##%% 3 graphiques côte-à-côte

x = np.linspace(0, 10, 500)

plt.subplot(1, 2, 1) # Graphique de sin
plt.plot(x, np.sin(x))
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()

plt.subplot(1, 2, 2) # Graphique de cos
plt.plot(x, np.cos(x))
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()

plt.tight_layout()
plt.show()

#%% Exercice: Projectile en 2D
    
def position_x(t):
    return 20*np.cos(np.radians(50))*t

def position_y(t):
    return 5 + 20*np.sin(np.radians(50))*t - 4.9*t**2

t = np.linspace(0, 3, 500)

plt.subplot(1, 3, 1) # Position x en fonction du temps
plt.plot(t, position_x(t), lw = 3, color = 'blue')
plt.xlabel('Temps (s)')
plt.ylabel('Position x (m)')
plt.grid()

plt.subplot(1, 3, 2) # Position y en fonction du temps
plt.plot(t, position_y(t), lw = 3, color = 'black')
plt.xlabel('Temps (s)')
plt.ylabel('Position y (m)')
plt.grid()

plt.subplot(1, 3, 3) # Position y en fonction de position x
plt.plot(position_x(t), position_y(t), lw = 3, color = 'green')
plt.xlabel('Position x (m)')
plt.ylabel('Position y (m)')
plt.grid()

plt.tight_layout()
plt.show()
    
#%%