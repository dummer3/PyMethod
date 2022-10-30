#------------------------------------------------------------------------------
# Quelques éléments importants pour le cours MRP Prep'ISIMA 2.
# La version de python utilisée est la 3.7
# Le codage est utf8.
# Attention : ce n'est PAS exhaustif.
# Lire les commentaires et le code exécutable.
# N'hésitez pas à me faire des retours sur ce support de cours
# pour que je puisse l'améliorer, le compléter etc.
# christian.laforest@isima.fr
#------------------------------------------------------------------------------

print("Hello word !")
# Pour exécuter avec idle, appuyer sur la touche F5 après avoir sauvé.

# Ceci est un commentaire, non exécuté.

# Sauvegarder les fichiers en format utf8 (encodage portable)

#------------------------------------------------------------------------------
# Les chaines de caractères et print.
#------------------------------------------------------------------------------

print("-"*28 + "\n Les chaines de caractères \n" + "-"*28)
# Délimiteurs/constructeurs : "" ou ''

"Ceci est une chaine de caractères." 
'Ceci est aussi une chaine de caractères'

# Pour utiliser un caractère ' à l'intérieur d'une chaine : utiliser ""
# Pour utiliser un caractère " à l'intérieur d'une chaine : utiliser ''

print("Essai d'affichage d'une chaine")
print('Un autre "essai" pour voir la différence')

# NB : print fait un passage à la ligne automatique à la fin d'exécution

print("Pour forcer un passage à la ligne, utiliser '\\n'")
print("Pour contrôler vos passages à la ligne \n dans un print\n \n")

# Pour afficher des valeurs variables dans une chaine : les f strings
x = 4
print(f"La valeur de x est : {x} et son carré est {x**2}")

# Les strings sont des objets. Ils ont des méthodes.
s = "Bonjour M. Bond soyez le bienvenu chez nous"

print(f'Quelques exemples de méthodes utilisées sur la chaine s "{s}" : ') 
print(f"s.upper() : {s.upper()}") # Pour tout mettre en majuscule
print(f"s.lower() : {s.lower()}") # Pour tout mettre en minuscule
print(f"s.title() : {s.title()}") # Chaque mot débute par une majuscule
print("Repetition 4 fois"*4)

# split() : une méthode très intéressante pour obtenir la liste des mots.
l = s.split()
print(f'Avec s.split() la liste des mots de la chaine "{s}" est : \n {l}')

# Il est possible de "spliter" sur autre chose que les blancs
print(f'Spliter sur autre chose "a,b,,c,d".split(",") : {"a,b,,c,d".split(",")}')

# La méthode join(it) est aussi très intéressante.
print("Illustration de la méthode join() d'une chaine de caractère")
print(" Séparateur ".join(l))
print("".join(l))
print("*".join(l))

s = "0123456789"

# s[5]  :  caractère d'indice 5 de la chaine s
# len(s) : longueur de la chaine (son nombre de caractères).
print(f'La chaine "{s}" est de longueur {len(s)}')
print(f'Le caractère d\'indice 0 de "{s}" est : {s[0]}')
print(f'Le caractère d\'indice 5 de "{s}" est : {s[5]}')

print(f"Exemples d'utilisations de slices sur la chaine {s}")
# Utilisation des slices [d:f:p] : d=début, f=fin, p=pas
print(s[3:6]) # Par défaut le pas est de 1
print(s[6:])
print(s[:8])
print(s[::2]) # Le dernier indice est le pas ici 2
print(s[::-1]) # On peut afficher la chaine inversée comme ça.
print(s[-2:-5:-1]) # -2 = caractère d'indice 2 en partant de la droite de s.

# ATTENTION ! une chaine est immuable (non modifiable). On ne peut pas
# faire s[6] = 9 par exemple.

# Par contre une chaine est itérable.

print(f'Voici les caractères de "{s}" obtenus avec une boucle for : ')
for x in s:
    print(x)

# Cette forme est à préférer à :
# for i in range(len(s)):
#     print(s[i])

# Concaténer des chaines avec +
print(f'Concat de 2 chaines avec + : "Bonjour"+" Bye" = "{"Bonjour"+" Bye"}"')

#------------------------------------------------------------------------------
# Les listes
#------------------------------------------------------------------------------

print("-"*12 + "\n Les Listes \n" + "-"*12)
# Constructeur de liste avec [ et ]

l = [12, 55, 77] 

# Les listes peuvent être hétérogènes :

l = [-9, 7.77, "Bonjour vous", [1, 2]]
print(f"Voici le contenu de la liste l : {l}")

print(f"Son premier élément est à l'indice 0 : {l[0]}")
print(f"Sa longueur est : {len(l)}")

# Une liste est un objet mutable (modifiable)
# Modifier le contenu d'une case d'une liste

l[1] = -44
print(f"Après modification de l'élément d'indice 1, la liste est : {l}")

# Ajouter un élément à la fin d'une liste
l = [1, 2, 3, 4, 5, 6]
print(f"Un nouveau contenu pour la liste l : {l}")
l.append(7)
print(f"La liste l après l.append(7) : {l} (insèré à la fin)")

# Supprimer le dernier éléments d'une liste avec pop()
l.pop()
print(f"La liste l après l.pop() : {l} (supprime le dernier)")

# Supprimer l'élément d'indice i avec l.pop(i) 
l.pop(3)
print(f"La liste l après l.pop(3) : {l} (supprime l'élément d'INDICE 3)")

# Concaténer deux listes avec +
l1 = [1, 2, 3, 4, 5, 6]
l2 = ["a", "b", "c"]
print(f"\nVoici deux nouvelles listes l1={l1} et l2={l2}")
print(f"Résultat de l1 + L2 : {l1 + l2} (contact)")

# Slices sur des listes : similaire à ce qui a été vu avec les strings
print(f"Slice sur la liste l1 : l1[2:5] = {l1[2:5]}")

# Références de listes : attention !
print(f"\nRappel l1={l1}")
l2 = l1
print(f"l2 = l1. l2 référence la liste {l2}")
l1[1] = 999
print(f"Modification du contenu d'une case l1 : {l1}")
print(f"Impact sur l2 : {l2}")
print(f"l1 et l2 sont deux références sur le même objet")

# Il est possible d'utiliser la méthode copy() pour faire une copie
# "physiquement" séparée.
l2 = l1.copy()
print(f"\nEn utilisant l2 = l1.copy(), l2 est : {l2}")
l1[1] = "Coucou c'est moi !"
print(f"Modifions l1 : {l1}")
print(f"Aucun impact sur l2 : {l2}")

# Une liste est un objet itérable
print("Itération sur la liste avec une boucle for : ")
for x in l1:
    print(x)

#------------------------------------------------------------------------------
# Les ranges
#------------------------------------------------------------------------------

print("-"*12 + "\n Les ranges \n" + "-"*12)

# range(d,f) : intervalle [d,f[
# range(f) = range(0,f)
# Un range est itérable

print("Un range est itérable")
for i in range(3):
    print(i)

# Attention : un range n'est PAS une liste. Un range est un... range.
print(f"range(5) : {range(5)}")

# Pour obtenir une liste à partir d'un range : list(...)
print("Transformer un range en liste : list(range(3, 10)) :")
print(list(range(3, 10)))

#------------------------------------------------------------------------------
# Les sets (ensembles)
#------------------------------------------------------------------------------

print("-"*20 + "\n Les sets (ensembles) \n" + "-"*20)

# Créer un ensemble en utilisant { et }
s = {2, -9, 7.33, "Bond"}
print(f"Voici un ensemble référencé par s : {s}")

# Un set est un objet itérable
print("Un set est itérable")
for x in s:
    print(x)

s = {12+5, 'a', 17}
print("Voici l'ensemble : {12+5, 'a', 17} :" + f"{s}")
print("Le système a simplifié pour ne garder qu'une seule occurence !!")

# Un set est mutable
s = {1, 33, 8}
print(f"Le set s : {s}")
s.add(9)
print(f"Après ajout d'un élément avec la méthode s.add(...) : {s}")
s.discard(8)
print(f"Après la suppression de l'élément 8 avec la méthode s.discard(8): {s}")

l = list(range(5)) + [2, 1]
print(f"Voici une liste l : {l}")
print(f"La liste l transformée en set : set(l) : {set(l)}")
print("Dans le sens set -> liste avec list(...)")
s = {2, 5, 7, 8, 5}
print("list({2, 5, 7, 8, 5}) : " + f"{list(s)}")

# Attention : pour un ensemble vide, utiliser set() et PAS {}

#------------------------------------------------------------------------------
# Les dictionnaires
#------------------------------------------------------------------------------

print("-"*26 + "\n Les dictionnaires \n" + "-"*26)

# Créer un dico avec la syntaxe {... : ...}
age = {"Albert" : 77, "Lola" : 15, "Kevin" : 20}
print(f"Le dictionnaire age est : {age}")
print(f"Le contenu de la case 'Lola' est age['Lola'] : {age['Lola']}")
# Ici les indices de la structure ne sont pas nécessairement des entiers.
# C'est très pratique ! Le système détermine la case grâce à un procédé de
# hachage. Attention : il faut que les indices soient immuables. 

# Un dico est mutable (modifiable)
age['Zoe'] = 33
print(f"Ajoutons un élément : age['Zoe'] = 33")
print(f"Le dictionnaire est maintenant : {age}")
del(age["Lola"])
print(f"Supprimer un élément : del(age['Lola'])")
print(f"Le dictionnaire après suppression : {age}")

# Un dico est itérable
print("Itérons sur le dictionnaire")
for x in age:
    print(x)
print("Pour obtenir le contenu des cases on peut faire :")
for x in age:
    print(age[x])

# On peut utiliser auss les méthodes age.keys() (les indices) et age.values()
# (les valeurs).
# Attention : ces méthodes ne donnent pas des listes mais des objets itérables.
# Les deux boucles for précédentes peuvent aussi s'écrire :
##for x in age.keys():
##    print(x)
##for x in age.values():
##    print(x)

#------------------------------------------------------------------------------
# Les tuples
#------------------------------------------------------------------------------

print("-"*15 + "\n Les tuples \n" + "-"*15)
# Construire un tuple avec ( et )
t = (2, -77.8, "Clermont")
print(f"Voici un tuple t : {t}")
print(f"t[1] : {t[1]}")

# Un tuple à un seul élément 14 par exemple n'est PAS (14) mais (14,)
# Attention, (14) vaut 14 et PAS le tuple (14)

# Un tuple est immuable. On ne peut pas faire t[1] = 22 par exemple.
# Oui MAIS :
l = [1, 2]
t = ("a", l, 8) # La liste l est un élément du tuple
print(f"l : {l} t = ('a', l, 8) : {t}")
l.append(3)
print(f"Modifions l avec l.append(3) : {l}")
print(f"Impact sur le tuple t : {t}") # Le contenu du tuple est modifié

# Un tuple est itérable
t = (1, 2, 3)
print(f"Voici un tuple t {t} et ses composantes, lues avec une boucle for :")
for x in t:
    print(x)

# Il est possible, connaissant la taille d'un tuple, de récupérer ses
# composantes en une seule affectation
a, b, c = t
print(f"L'affecation a, b, c = t donne a={a}, b={b}, c={c}")

# Attention, un tuple est défini même sans les paranthèses : 1, 2, 3 est
# le tuple (1, 2, 3). Conseil : mettez les ( et ) pour clarifier.

print(f"La taille du tuple t {t} est len(t) {len(t)}")
print(f"Slice sur les tuples : t[0:2] donne {t[0:2]}")
print(f"Transformer un tuple en liste list(t) {list(t)}")
print(f"Transformer une liste en tuple avec tuple(l)")

# Pour accéder directement aux composantes de tuples stockés dans une liste l
l = [("x"+str(i), "y"+str(i), "z"+str(i)) for i in range(3)]
print(f"Accéder aux composantes de chaque tuple de la liste l {l}") 
for a, b, c in l:
    print(a + b + c)

#------------------------------------------------------------------------------
# Les compréhensions
#------------------------------------------------------------------------------

print("-"*19 + "\n Les compréhensions \n" + "-"*19)

# Objectif : construire une structure (une liste ou un set par exemple)

# Une manière classique :
print("Construire une liste avec une classique boucle for")
l = []
for x in range(99,106):
    l.append(chr(x))  # chr(x) = caractère numéro x dans la table
print(f"La liste résultat l est : {l}")

# Ici LA manière "à la python" de faire est la suivante :
l = [chr(x) for x in range(99,106)]
print(f"Construction par compéhension l = [chr(x) for x in range(99,106)] {l}")

# Possible d'imbriquer (attention à la lisibilité et à l'ordre des boucles !)
l = [chr(x) for y in range(1,4) for x in range(97,97 + y)] 
print(f"Une liste construire par compréhension avec 2 boucles : {l}")

# La même chose mais pour construire un set
s = {chr(x) for y in range(1,4) for x in range(97,97 + y)} 
print(f"Un set construit par compréhension avec 2 boucles imbriquées : {s}")

# Application : construire la liste des caractères d'une chaine avec une
# compréhension
s = "abcd"
l = [x for x in s]
print(f'La liste des caractères de la chaine "{s}"' +
      f"obtenue par l = [x for x in s] :{l}")
print(f'Pour faire l\'opération inverse "".join(l) : {"".join(l)}')

#------------------------------------------------------------------------------
# Les conditionnelles
#------------------------------------------------------------------------------

print("-"*33 + "\n Les conditionnelles (if...elif.. else) \n" + "-"*33)

print("Les entiers pairs entre 0 et 8, calculés avec une boucle for et if")
for i in range(9):
    if i % 2 == 0: # a % b : a modulo b. Le reste de la division est a//b
        print(i)

# Illustration de la syntaxe avec un exemple
# Notez qu'il n'y a pas d'indentation cumulée (elif au même niveau que le if)
print("if: ... elif ... elif ... else")
note = 13
print(f"Votre note est {note}. Voici votre mention :")
if note < 0:
    print(f"Erreur : note {note} négative !")
elif note < 10:
    print("Echec")
elif note < 12:
    print("Passable")
elif note < 14:
    print("AB")
elif note < 16:
    print("B")
elif note < 18:
    print("TB")
elif note <= 20:
    print("Félicitations !")
else:
    print(f"Erreur, note {note} > 20 impossible")
         
# Le if else sous forme d'EXPRESSION (le else est obligatoire)
print("Le if... else EXPRESSION." +
      "Exemple : élever x au carré s'il est pair et au cube sinon.")
x = 9
x**2 if x % 2 == 0 else x**3 # Ceci est une expression, qui a une valeur.
print(f"Ici x = {x}")
print(f"x**2 if x % 2 == 0 else x**3 : {x**2 if x % 2 == 0 else x**3}")

# Voila le bon endroit pour introduire les Booléens :
# True et False (notez les majuscules)
print(f"Les valeurs de vérité {True} et {False}")
print(f"Des opérateurs logiques : or, and, not")
print(f"Une expression du type 2 > 5 a une valeur Bolléenne {2 > 5}")
print(f"ATTENTION : dans une conditionnele, une valeur non nulle est ")
print("considérée comme True et les autres False")
if 4:
    print(4)
else:
    print("Pas 4")

#------------------------------------------------------------------------------
# Les fonctions
#------------------------------------------------------------------------------

print("-"*14 + "\n Les fonctions \n" + "-"*14)

# Mot clé pour définir une fonction : def
def f(x, y, z):
    result = x + y + z
    print(f"La somme des paramètres d'entrée {x, y, z} est : {result}")

# f est le nom de la fonction. ATTENTION : donnez des noms qui ont un sens.
# x, y, z sont les 3 paramètres formels de cette fonction.
# result est une variable locale (non connue à l'extérieur de f).
# Le reste est le corps de la fonction, un bloc d'instructions.
# Notez au passage : pass = instruction qui ne fait rien.

print(f"Utilisation de la fonction f")
f(1, 2, 3)
f('Toto', ' a ', 'perdu')

# Ici les paramètres passés sont souvent appelés les paramètres effectifs.
# La valeur de l'appel d'une fonction est... ça dépend :
# S'il n'y a pas de return, c'est la valeur None.
# Sinon c'est la valeur du premier return rencontré lors de l'exécution.

print("Le premier return rencontré retourne la valeur associée et stoppe" +
      "l'exécution de la fonction")
def g(x):
    if x%2 == 0:
        return "Pair"
    else:
        return "Implair"
    
print(f"Valeur de g(4) : {g(4)}")
print(f"Valeur de g(7) : {g(7)}")

# Une fonction peut définir et utiliser une (ou plusieurs) fonction locale
def message_parite(x):
    """ On peut placer une documentation de la fonction (docstring).
        Celle-ci peut tenir sur plusieurs lignes.
        help(nom_de_la_fonction) pour l'afficher.
        Ceci est une pratique recommandée pour documenter son code."""
    def parite(x):
        return "Pair" if x%2 == 0 else "Impair"
    print(f"Le paramètre {x} est {parite(x)}")

message_parite(66)
message_parite(9)
print("Voici la docstring de la fonction :")
help(message_parite)
# Notez : la fonction locale parite() retourne une valeur mais PAS la fonction
# message_parite qui ne fait qu'afficher un message.

# Les bibliothèques contiennent des fonctions déjà écrites.
# Par exemple la bibliothèque math contient la fonction sqrt(...)
# Pour y accéder, on peut faire : import math pour importer la totalité de la
# bibliothèque ou faire des imports plus ciblés.
from math import sqrt
print("Après l'import à partir de math, la fonction sqrt est disponible : " +
      f"sqrt(5)={sqrt(5)}")

# Si une fonction a beaucoup de paramètres il est parfois difficile de se
# souvenir de l'ordre.
def affiche_personne(nom, prenom, age, sexe):
    if age < 18:
        print(f"Salut ! Tu est {prenom} {nom}, tu as {age} ans")
        print(f"Tu est un{' garçon' if sexe == 'H' else 'e fille'}")
    else:
        print(f"Bonjour {'Madame' if sexe == 'F' else 'Monsieur'}")
        print(f"Vous êtes {prenom} {nom} et vous avez {age} ans.")

affiche_personne("Bond", "James", 50, "H")
affiche_personne("Petit", "Léa", 12, "F")

# Possible d'exprimer les paramètres effectifs comme ça (notez l'ordre
# quelconque dans ce cas)
affiche_personne(age=17, prenom="Tom", sexe="H", nom="Pouce")
# Il est possible de mélanger les deux. ATTENTION à bien maitriser l'ordre !
affiche_personne("Depardieu", "Gérard", sexe="H", age = 70)

# Il est possible de donner une valeur par défaut à un paramètre d'une fonction
def multiplier_message(n, message_a_dupliquer="Message par défaut."):
    return message_a_dupliquer*n

# Cette fonction retourne une valeur mais n'affiche rien. 
print(multiplier_message(3, "Toto"))
print(multiplier_message(2))
print(multiplier_message(message_a_dupliquer="m", n=8))
print(multiplier_message(2, [1, 2, 3])) # Ca marche aussi avec des listes ici.

# Quelques fonctions utiles. 
# La fonction sum est très pratique pour faire des sommes de valeurs numériques

print("La fonction sum pour faire la somme d'éléments d'un range :" +
      f" {sum(range(7))}")
print(f"Ou la somme des éléments d'une liste : {sum([2, 77, -8])}")

# Tirages ou choix aléatoires avec la bibliothèque random : import random
# Voici quelques exemples dans ce qui suit. D'autres choses sont disponibles.
import random

print(f"Pour obtenir une valeur aléatoire entre 0 et 1 : {random.random()}")
print(f"Pour obtenir un entier aléatoire entre a et b: random.randint(a, b) :")
print(f"{random.randint(7, 11)}")
print(f"Pour obtenir une valeur parmi plusieurs random.choice(...) :")
print(random.choice([12, "Toto", False]))

