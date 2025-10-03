#%% Exercice de révision: Chapitre 3
    
for i in range(31):
    if i % 3 == 0 and i <= 15:
        print('Chat')
    elif i % 5 == 0 and i > 15:
        print('Chien')
    elif i % 7 == 0 or i % 11 == 0:
        print('Hamster')
    else:
        print(i)

#%% Tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6, 7)
tuple3 = tuple1 + tuple2
tuple4 = tuple2 + tuple1

print(tuple3)
print(tuple4)

#%%

vecteur = (4, -7, 15)

print(vecteur[0])
print(vecteur[1])
print(vecteur[2])

print(vecteur[-1])
print(vecteur[-2])
print(vecteur[-3])

#%%

x = vecteur[0]
y = vecteur[1]
z = vecteur[2]

print(x)
print(y)
print(z)

#%% Listes

nombres = [2, 3, 4]

print(nombres[0])
print(nombres[1])
print(nombres[2])

#%%

nombres = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(nombres[0:5])
print(nombres[3:5])
print(nombres[0:7:2])
print(nombres[0:7:3])

#%% 

nombres = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

nombres[0] = 5
nombres[5] = 123
nombres[-1] = nombres[2] + nombres[3]

print(nombres)

#%% Types de listes

liste1 = ['a', 'salut', 'david']

liste2 = [True, False, False]

liste3 = [4, True, 1.79, 'bonjour']

#%% len et index

age = [31, 17, 23, 44, 79, 44]

print(len(age))

print(age.index(44))

print(23 in age)
print(200 in age)

#%% append

test = [1, 2, 3, 4]

test.append(10)
test.insert(0, -5)
test.insert(2, 99)

print(test)

#%% pop

test = [1, 2, 3, 4, 5, 6]

test.pop()
print(test)

test.pop(1)
print(test)

premier = test.pop(0)
print(test)
print(premier)

#%% min, max et sum

test = [1, 2, 3, 4]

valeur_min = min(test)
valeur_max = max(test)
somme = sum(test)

print(valeur_min)
print(valeur_max)
print(somme)

#%% sort et sorted
   
age = [31, 17, 23, 44, 79]
    
age.sort()
print(age)

age.sort(reverse = True)
print(age)

croissant = sorted(age)
décroissant = sorted(age, reverse = True)

print('Liste en ordre croissant:', croissant)
print('Liste en ordre décroissant:', décroissant)

#%% Opérations avec des listes

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']

print(liste1 + liste2)
print(liste2 + liste1)
print(liste1 * 2)
print(liste2 * 3)

#%%

mot = 'Bonjour David'

print(len(mot))
print(mot.index('j'))
print(mot.count('o'))

#%% Exercice: Notes d'examen

notes = [78, 61, 65, 91, 83, 77, 56, 89]

notemax = max(notes)
notemin = min(notes)
diff = notemax - notemin
print(f'La note la plus haute est {notemax}, la plus basse est {notemin} et la différence est {diff}.')

moyenne = sum(notes) / len(notes)
print(f'La moyenne est {moyenne}.')

notes_décroissant = sorted(notes, reverse = True)
print(f'Notes en ordre décroissant: {notes_décroissant}')

notes.pop(notes.index(notemin))
notes.pop(notes.index(notemax))

#notes = notes + [43, 51, 98]
notes += [43, 51, 98]
notes.sort()

print(f'Notes finales en ordre croissant: {notes}')

#%% Dictionnaire

personnes = {'Alice':25, 'Bob':31, 'Charlie':47}

print(personnes['Alice'])
print(personnes['Bob'])
print(personnes['Charlie'])

#%%

personnes['David'] = 28
print(personnes)

personnes['Bob'] = 91
print(personnes)

del personnes['Charlie']
print(personnes)

#%% Listes dans une liste

tableau = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]

print(tableau[0])
print(tableau[2])

print(tableau[0][0])
print(tableau[0][3])
print(tableau[1][2])

#%%

matrice = [ [1, 3], [2, 4]]

print(matrice[0][0])
print(matrice[0][1])
print(matrice[1][0])
print(matrice[1][1])

#%% Dictionnaires dans une liste

étudiants = [{'prenom': 'Alice', 'age': 25, 'programme':'SN'}, 
             {'prenom': 'Bob', 'age': 31, 'programme':'SH'},
             {'prenom': 'Charlie', 'age': 47, 'programme':'TES'}]

print(étudiants[0])
print(étudiants[0]['prenom'])
print(étudiants[1]['age'])
print(étudiants[2]['programme'])

#%% Listes dans un dictionnaire

notes_prog = {'Alice':[65, 73, 81], 'Bob':[85, 79, 67], 'Charlie':[65, 52, 71]}

print(notes_prog['Bob'])
print(notes_prog['Alice'][0])
print(notes_prog['Bob'][0])
print(notes_prog['Charlie'][2])

#%% Dictionnaires dans un dictionnaire

cours = {'phys': {'prof':'David', 'local':'B203', 'heure':'8h30'},
         'math': {'prof':'Yanick', 'local':'A201', 'heure':'11h30'},
         'bio': {'prof':'Laurie', 'local':'C203', 'heure':'13h00'}}
         
print(cours['phys'])
print(cours['phys']['prof'])
print(cours['math']['local'])
print(cours['bio']['heure'])

#%% Exercice: Tableaux imbriqués

matrice = [ [1, 2], [3, 4], [5, 6], [7, 8] ]

print(matrice[1][0])
print(matrice[3][1])

matrice[2][1] = matrice[1][0] + matrice[3][1]
print(matrice)

#%%

JS_inc = {'directeur':{'étage':3, 'salaire':350000,'nombre employé':1},
          'programmeur':{'étage':2, 'salaire':120000, 'nombre employé':5},
          'réceptionniste':{'étage':1, 'salaire':80000, 'nombre employé':2},
          'vendeur':{'étage':1, 'salaire':60000, 'nombre employé':3}}

print(JS_inc['directeur']['salaire'])
print(JS_inc['programmeur']['étage'])
print(JS_inc['réceptionniste']['salaire'])
print(JS_inc['vendeur']['nombre employé'])

#%%