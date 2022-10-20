import random

print("A M O N G U S")

#region cours

#region Exemple de if

# if 10>3:
#     print("Oui 10 est supérieur à 5")

#endregion
#region Conversion String Int

# x=5
# y="Salut"
#
# print(x)
# print(y)
#
# print(str(x) + y) #passage de x en string

#endregion
"""
Exemple de commentaire
"""
#region Instanciation de type

# x = str(3) #type string
# y = int(3) #type Integer
# z = float(3) #type numérique float
#
# print(x)
# print(y)
# print(z)

#endregion
#region Récupéré le type

# x = str(3) #type string
# y = int(3) #type Integer
# z = float(3) #type numérique float
#
# print(type(x))
# print(type(y))
# print(type(z))

#endregion
#python est sensible à la casse
#region notation

#notation CAMEL

maVariable = "Salut"

#notation SNAKE

ma_variable = "Salut"

#notation PASCAL

MaVariable = "Salut"

#endregion
#region Assignation variable

# a,b,c = "Voila", "Python", "Cool"
#
# print(a)
# print(b)
# print(c)
#
# a=b=c= "Hello"
# print(a)
# print(b)
# print(c)

# legumes = ["patate", "tomate"]
# a,b = legumes
# print(a)
# print(b)

# x = "Hello"
# y = 5
# print(x, y)

# x = 5
# y = 10
# print(x,y)

#endregion
#region def

# X = "Salut"
#
# def maFonction():
#     print("Tiens " + X)
#
# maFonction()

# X = "Salut"
# def maFonction():
#     X="superbe"
#     print("Tiens " + X)
#
# maFonction()
# print("Tiens " + X)

# X = "Salut"
# def maFonction():
#     global X #Sa change la variable globale X qui passe de Salut a Superbe
#     X = "Superbe"
#
# maFonction()
# print("Tiens " + X)

#endregion
"""
type texte = str
Numérique = int, float, complex
Séquence = list, tuple, range
Mapping = dict
Type de set = set, frozenset
Booléens = bool
Binaire = bytes, bytearray, memoryview
Type None = NoneType
"""

#exemple complexe

# x = 1j

#exemple scientitfique

# y = 12E4
# print(y)
# z = -50.7e100
# print(z)
#
# a = 3 + 5jy
# b = 5j
# c = -5j

# x = 2
# a = float(x)
# print(a)
#
# y = 2.5
# b = int(y)
# print(b)
#
# z = 1j
# c = complex(z)
# print(c)

# import random
#
# print(random.randrange(1,10))

# a = """
# Mais c'est vrais qu'au fond,
# Manger du chien c'est pas très bon
# """
# print(a)

# a = "Bonjour"
# print(a[2])

# for x in "Salut":
#     print(x)

# x = "Voila python"
# print(len(x))

# chaine = "Voila est ce que Python"
# if "Python" in chaine:
#     print("Trouvé")

# c = "Salut les amis"
# print(c.strip())

# d = "Salut python salut"
# print(d.replace("u","1",1))

#endregion
#region cours 2

# chaine = "Je connais\"Michel\"se petit mec"
# print(chaine)
#
# chaine2 = "Je suis \n PAPA"
# print(chaine2)

# liste9 = ["pomme", "poire", "cerise"]
# print(liste9.pop(2))

# liste10 = ["pomme", "poire", "cerise"]
# del liste10[1] #il faut enlever le [] pour supprimer toute la liste
# print(liste10)

# liste11 = ["pomme", "poire", "cerise"]
# liste11.clear()
# print(liste11)

# liste12 = ["pomme", "poire", "cerise"]
# for x in liste12:
#     print(x)
# for x in range(len(liste12)):
#     print(liste12[x])



#endregion

#region Exercice 001

# prenom = "Pierre"
# age = int(20)
# majeur = True
# compte_en_banque = float(20135.284)
# amies = ["Marie", "Julien", "Adrien"]
# parents = ("Marc", "Caroline")
#
# print(prenom)
# print(age)
# print(compte_en_banque)
# print(majeur)
# print(amies)
# print(parents)

#endregion
#region Exercice 002

# site_web = "voila"
# print(site_web)

#endregion
#region Exercice 003

# nombre = 15
# print("Le nom est" + nombre)

#endregion
#region Exercice 005

a = 2
b = 6
c = 3

# print(a,"+",b,"+",c) #la solution facile

# print(f"{a} + {b} + {c}") #solution avec f string

# print(a, b, c, sep=" + ") #solution avec separator

#endregion
#region Exercice 006

# list1 = range(3)
# list2 = range(5)
#
# print(list(list2)) #list est un mot réserver il faut donc modifier list en liste ou list1

#endregion
#region Exercice 007

# prenom = "Pierre"
# if isinstance(prenom,str):
#     print('La variable est une chaine de caractères')
# prenom = 0
# if isinstance(prenom,str):
#     print('La variable est une chaine de caractères')

#endregion
#region Exercice 008
#
# phrase = "Bonjour les amis"
# nouvelle_phrase = phrase.replace("Bonjour", "Salut")
# print(nouvelle_phrase)

#endregion
#region Exercice 009

# chaine = ["pomme", "abricot", "cerise", "fraise", "orange"]
# chaine.sort()
# print(chaine)
#
# chaine = "pomme,abricot,cerise,fraise,orange"
# chaine1 = chaine.split(",")
# chaine1.sort()
# chaine2 = ",".join(chaine1)
# print(chaine2)

#endregion
#region Exercice 010

"""
Créer un programme qui nous permet d'afficher le volume d'une sphère
Extension (si expérience) : Créer un programme qui permet de calculer le volume d'une sphère, d'un parallèlépipède au choix de l'utilisateur
"""

# import math
#
#
# r= 100.0
# pi = math.pi
# v_sphere = (4*pi/3) * (r**3)
#
# print(v_sphere)
#
# lo = 10
# la = 30
# ha = 20
#
# v_par = lo * la * ha
#
# print(v_par)

#endregion
#region Exercice 011

# """
# Créer une liste de nombres de 10 à 100 et les afficher
# """
#
# ListeNb = list(range(10,101))
# print(ListeNb)
#
# """
# Créer une liste de nombres pairs de 1 à 200 et les afficher
# """
#
# ListePair = [i for i in range(201) if i%2 == 0]
# print(ListePair)


#endregion
#region Exercice 012

"""
Créer un générateur de lancé de dés, les valeurs aléatoire vont de 1 à 6
"""

# Lancer_Des = random.randint(1,6)
# if Lancer_Des == 4:
#     print(Lancer_Des)

"""
Faire la moyene des lancer
"""

# Nb_lancer = 4
# sommes = 0
# for i in range(Nb_lancer):
#     sommes += random.randint(0, 6)
#     Moyenne_Lancer = sommes / Nb_lancer
#
# print(Moyenne_Lancer)

#endregion
#region Exercice 013

"""
Compter le nom D occurence D une lettre dans une chaine
"""

# lettre_a_chercher = "a"
# phrase = "voila les amis. Alors ça va ?"
#
# count_l = phrase.lower().count(lettre_a_chercher.lower())
# print(count_l)

"""
Afficher la lettre la plus fréquente d'une chaîne...
"""
# lettre2 = 0
# lettre_re = 0
#
# for lettre1 in phrase:
#     for lettre2 in phrase:
#         if lettre1 == lettre2:
#             lettre_re = lettre_re +  1
#     nombre_l = ['lettre1'] -> [lettre_re]
# print(nombre_l)
#endregion