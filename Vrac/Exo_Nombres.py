import time
import math

# Dans cette activité, tous les entiers sont positifs.
# Soit n un entier.
# On dit que d est un "diviseur strict" de n si d divise n et d<n.
# On dira que deux entiers n et m sont "freres" si :
# la somme des diviseurs stricts de n est égale à m et la somme des
# diviseurs stricts de m est égale à n.
# NB : n et m peuvent avoir la même valeur (un entier peut donc
# être frere avec lui même).

# Ecrivez la fonction Booléenne qui prend en entrée deux entiers et
# retourne la valeur Bolléenne vrai si ces deux entiers sont freres.

def sont_freres(n, m):
    s0 = s1 = 1;
    for i in range(2,int(math.sqrt(max(n,m))+1)):
        if n%i == 0:
            s0 += i+n//i;
        if m%i == 0:
            s1 += i+m//i;
    return s0 == m and s1 == n;

def frere_De(n):
    s = 1;
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            s += i+n//i;
    return s;

# Ecrivez la fonction qui prend en entrée un entier n_max et affiche toutes
# les paires n, m d'entiers freres pour tout n < n_max.
# Chaque paire ne doit être affichée qu'une seule fois.

def affiche_tous_freres(n_max):
    for i in range(6,n_max):
            a = frere_De(i)
            if  a <= i and frere_De(a) == i: 
                print(f"{i} avec {a}");
            

begin = time.time()
affiche_tous_freres(1_000)
print(f"Duration = {time.time() - begin} seconds to complete.")
print("-"*50)

begin = time.time()
affiche_tous_freres(10_000)
print(f"Duration = {time.time() - begin} seconds to complete.")
print("-"*50)

begin = time.time()
affiche_tous_freres(500_000)
print(f"Duration = {time.time() - begin} seconds to complete.")
print("-"*50)
