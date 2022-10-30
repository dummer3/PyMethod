"""Création de plannings de cours à partir de colorations de graphes.
Chaque cours a un nom qui est une chaine de caractères.
Chaque élève a un nom qui est une chaine de caractères.
Chaque cours doit être suivi par un ensemble donné d'élèves.
La durée de chaque cours est de 1h et doit être placé dans un créneau de 1h.
Il faut planifier chaque cours dans un créneau de telle manière
que si deux cours sont planifiés pendant le même créneau, ils ne doivent
pas concerner les mêmes élèves (un élève ne peut pas assister à plusieurs
cours en même temps). 

Les données sont à lire dans un fichier. Ce dernier est découpé en lignes,
chacune relative à un cours. 
Chaque ligne est composée de la manière suivante C:E1,E2,...,Ek ou C est un
cours et les Ei sont les élèves qui doivent suivre ce cours. 
À partir d'un tel fichier il faut construire un dico, nommé
dico_ens_élèves_du_cours qui a pour clés les cours et la valeur associée à
un cours C est l'ensembles des élèves devant suivre ce cours. 

À partir de ce dico. il faut construire un graphe dont les sommets sont les
cours et dans lequel il y a une arête entre deux sommets si ces deux cours
ont deux ensembles non disjoints d'élèves. La présence d'une arête dans le
graphe indique donc que les deux cours ne peuvent pas être planifiés dans
le même créneau horaire.

Il faut ensuite colorier ce graphe en utilisant le moins possible de couleurs.
Un créneau correspondra à une couleur et sera rempli avec tous les cours ayant
reçu la même couleur.
Il suffit ensuite de décider dans quel ordre les créneaux vont se succéder
(ici cela n'a pas d'importance). Ils seront simplement nommés "Créneau 1,
créneau 2,...". Le nombre de créneaux est donc égal au nombre de couleurs.
La durée totale du planning est justement ce nombre (puisque chaque créneau
dure 1h). 
"""

import random
# Utilisation de votre bibliothèque de manipulation de graphes à remomer
# Graphs.py. Ne laissez dans cette bibliothèque que la def. des fonctions.
import Exo_Graphs as gr

        
def créer_dico_depuis_fichier(fichier):
    """Prend en entrée le nom d'un fichier.
    Construit et retourne un dico ayant pour clés les cours et chaque cours c
    a pour valeur l'ensemble des élèves qui doivent suivre ce cours. Ces infos.
    sont à extraire du fichier."""
    dico = {}
    with open(fichier,"r",encoding="utf-8") as f:
        
        for l in f:
            s = l.strip().split(':')
            dico[s[0]] = s[1].split(',')
    return dico


def ens_des_élèves(dico_ens_élèves_du_cours):
    """Retourne l'ensemble de tous les élèves."""
    s = set()
    for el in dico_ens_élèves_du_cours.values() :
            s = s.union(el)
    return s;

def créer_graphe_depuis_dico(dico_ens_élèves_du_cours):
    """Retourne un graphe (dico (voir bibliothèque)) dont les sommets sont les
    cours. On place une arête entre le cours c et c' si c et c' ont au moins un
    élève en commun."""
    dico = {}
    for c in dico_ens_élèves_du_cours.keys() :
        l = set()
        for v in dico_ens_élèves_du_cours.keys() :
            if(c != v and len(set(dico_ens_élèves_du_cours[c]) & set(dico_ens_élèves_du_cours[v])) != 0):
                l.add(v)
        dico[c] = l
                   
    return dico
    


def affiche_créneaux_élève(élève, dico_ens_élèves_du_cours, coloration):
    """Affiche la liste des cours de l'élève ainsi que, pour chacun d'eux, le
    créneau du cours auquel il est planifié."""
    l = []
    for  cours in dico_ens_élèves_du_cours :
        if élève in dico_ens_élèves_du_cours[cours]:
            l.append(coloration[cours])
    print(l)
            

def affiche_planning_tous_élèves(dico_ens_élèves_du_cours, coloration):
    """Affiche les créneaux de chaque élève auquel il a cours. Affichage par
    ordre croissant des noms des élèves."""
    for eleve in ens_des_élèves(dico_ens_élèves_du_cours):
        affiche_créneaux_élève(eleve, dico_ens_élèves_du_cours, coloration)

def affiche_planning_des_cours(dico_ens_élèves_du_cours, coloration):
    """Affiche pour chaque créneau (par numéro croissant) les cours qui
    se déroulent pendant ce créneau."""
    pass


def affiche_nb_créneaux(coloration):
    """Affiche le nombre de créneaux nécessaires pour plannifier suivant la
    coloration donnée en paramètre."""
    s = set([coloration[cours] for cours in coloration])
    print(len(s))


# Utilisation de vos fonctions. 
dico_des_cours = créer_dico_depuis_fichier("Données_Panification_2")
graphe = créer_graphe_depuis_dico(dico_des_cours)
print(ens_des_élèves(dico_des_cours))
#print(graphe)
color = gr.color_graph_by_random_lists(graphe,20)
print(color)
affiche_créneaux_élève("E12",dico_des_cours,color)

# Coloriez le graphe (en utilisant ce qui est dans votre bibliothèque Graphs).
# Affichez ensuite vos résultats... Notament le nombre de créneaux.
