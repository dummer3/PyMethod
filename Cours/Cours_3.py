#------------------------------------------------------------------------------
# Cours sur La création d'itérateurs avec yield
# + Exemples d'utilisations.

# Version python utilisée : 3.7, codage utf8
# Lire les commentaires et le code exécutable.
# christian.laforest@isima.fr
#------------------------------------------------------------------------------

# Une autre façon de créer des itérateurs : avec des fonctions et yield.

# Voici un exemple.
# Ne cherchez pas de sens à la fonction f, c'est une simple illustration.
# Cette fonction n'a pas de return (mais elle pourrait en avoir un).

def f(x):
    y = x**2
    print(f"1ère print : x = {x} et y = {y}")
    yield y
    y = y + x
    print(f"2ème print x = {x} et y = {y}")
    yield y
    print(f"3ème print")
    yield "Fin"  # Il est possible de yielder des objets de différents types
    print("Fin de la fonction")
 
# Utilisons maintenant cette fonction.

it = f(15) # PAS l'appel à la fonction mais la création d'un itérateur.
print(it)   

# Tant que l'itérateur n'est pas utilisé, il ne "fait" rien. 
# it peut être utilisé, par exemple avec next(it).
# La fonction est exécutée jusqu'au prochain yield rencontré et retourne alors
# la valeur associée. La fonction est ensuite "mise en pause" jusqu'au prochain
# appel à l'itérateur. La fin d'exécution provoque l'exception StopIteration.
# Yield est donc une sorte de return mais qui ne termine pas la fonction. 

#print(">>>>> 1er next(it): ")
#print(next(it))
#print(">>>>> 2ème next(it): ")
#print(next(it))
#print(">>>>> 3ème next(it): ")
#print(next(it))
#print(">>>>> 4ème next(it): ")
#print(next(it))

# Pour éviter l'exeption StopIteration on peut utiliser une boucle for :

for x in it:
    print(x)


#------------------------------------------------------------------------------
# Itérateurs recursifs
#------------------------------------------------------------------------------

# Créons une fonction itérateur g qui a besoin de s'appeler elle-même.
# Voici un exemple naïf pour calculer les carrés des entiers entre n et 1
# de manière décroissante.

def g(n):
    if n >= 1:
        yield n**2
        g(n-1)

#it = g(10)
#next(it)
#next(it)

# Qu'est-ce qui ne va pas avec cette fonction ?
# L'instruction g(n-1) ne fait PAS un appel récursif à la fonction
# mais crée un itérateur : g(n-1) est un itérateur.
# Ce n'est donc pas cela que l'on veut ! Pour résoudre, utiliser "yield from".
# Voici la nouvelle version de g.

def g(n):
    if n >= 1:
        yield n**2
        yield from g(n-1)

# Il est possible de l'utiliser avec une boucle for. 

it = g(4)

for x in it:
    print(f"{x}", end=" ")
print(" ")

# Il est aussi possible d'utiliser des next(it) pour générer les éléments.
# Attention à l'arrivée d'une exception si vous itérez trop. 


#----------------------
# La suite look and say
#----------------------

# Version 'classique', avec des prints au fur et à mesure. Ne retourne rien.

def look_and_say(z, k=1):
    w = z
    print(w)
    for x in range(k):  # k est le nombre de termes à calculer.
        result = ""  # Le prochain terme va être "accumulé" dans result.
        i = 0
        l = len(w)
        while i <= l - 1:
            j = 0
            # Cherche le plus long mot composé uniquement du caractère w[i] :
            while i + j <= l - 1 and w[i + j] == w[i]:
                j += 1   
            result += str(j) + w[i] # j = nbre d'occurences de w[i].
            i = i + j
        # Prochain terme à traiter = resultat de la précédente itération.
        w = result  
        print(w)

print("Exécution de la version 'classique' de Look and Say")
look_and_say("1", 5)

# La même version mais mise en oeuvre sous forme d'itérateur.
# Pas de changement dans la stratégie de constructions des termes.

def look_and_say_iter(z, k=1):
    w = z
    yield w
    for x in range(k):
        result = ""
        i = 0
        l = len(w)
        while i <= l - 1:
            j = 0
            while i + j <= l - 1 and w[i + j] == w[i]:
                j += 1
            result += str(j) + w[i]
            i = i + j
        w = result
        yield w


print("Exécution de la version 'itérateur' de Look and Say :")
sira = look_and_say_iter("1", 5)  # sira est un itérateur. 
for x in sira:
    print(x)


#--------------------------------------
# Applications des itérateurs récursifs
#--------------------------------------

# Un itérateur (récursif) produisant toutes les listes de {0, 1} de taille n.

def iter_toutes_les_listes_binaires(n):
    def h(i): # Fonction locale de travail sur l'indice i de la liste.
        if i == n: # Cas terminal de la récursion. 
            yield resultat # La liste est remplie, on la yielde.
        else:
            resultat[i] = 0  
            yield from h(i + 1)
            resultat[i] = 1
            yield from h(i + 1)
    
    # Réservation d'une liste de taille n. 
    resultat = ["RIEN"]*n # Son contenu initial n'est pas important.
    yield from h(0) # Cette liste va être modifiée au fur et à mesure dans h.


it = iter_toutes_les_listes_binaires(4) # Création de l'itérateur.
for x in it: # Utilisation de l'itérateur. 
    print(x) 


#--------------------------------
# Le problème des nombres frères (ou amis) résolu avec un itérateur.
#--------------------------------

# Notez que n//d est le quotient entier de la division de d par n.

import time
import math

def speed_sum_of_divisors(n):
    sum_div = 1  # 1 is a universal divisor
    square_root = int(math.sqrt(n))
    for d in range(2, square_root + 1): # Just take int. between 2 and sqrt(n)
        if (n % d) == 0:
            sum_div += d + n//d  # If d is a divisor then n/d also. Add both.
    if square_root**2 == n:  # If n=p^2, p was added twice. Remove one.
        sum_div -= square_root
    return sum_div


def are_friends(n, m):
    return n == speed_sum_of_divisors(m) and m == speed_sum_of_divisors(n)


def iter_all_friends(n_max):
    for n in range(1, n_max + 1):
        m = speed_sum_of_divisors(n)  # If n has a friend it must be this m.
        if n <= m:  # This test is to avoid repetitions of pairs of friends.
            if n == speed_sum_of_divisors(m):
                yield n, m  # Here we yield a 2-tuple.


begin = time.time()
it = iter_all_friends(400_000)
for x, y in it: # Notez la syntaxe pour récupérer les 2 composantes du tuple.
    print(f"{x} and {y} are friends")
print(f"Duration = {time.time() - begin} seconds to complete.")
