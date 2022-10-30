"""Automates finis deterministes (AFD).
Un automate est un tuple :
(alphabet, ens. des états, état initial, ens. de états accepteurs, delta) 
La fonction de transition delta est un dictionnaire dont les clés sont des
tuples (q,c) avec q un état et c un caractère.
Déterministe = pour tout état p et tout caractère c de l'alphabet, il
existe exactement un état q tel que : delta(p,c)=q.
L'automate a exactement un état initial.
Un mot est accepté ssi en partant de l'état initial l'automate est dans un
état accepteur après avoir traité l'intégralité du mot. 
Un état est une chaine de caractères.
"""

def alphabet(automate):
    """Retourne l'alphabet de l'automate."""
    return automate[0]


def ens_etats(automate):
    """Retourne l'ens. des états de l'automate."""
    return automate[1]


def etat_initial(automate):
    """Retourne l'état initial de l'automate."""
    return automate[2]


def ens_etats_accepteurs(automate):
    """Retourne l'ens. des états accepteurs de l'automate."""
    return automate[3]


def delta(automate):
    """Retourne la fonction de transition de l'automate."""
    return automate[4]


def construit_alphabet_a_partir_de_delta(dico_delta):
    """Retourne l'ens. alphabet de l'automate dont la fonction delta est donnée
    sous forme de dictionnaire."""
    alphabet = set()
    for t in dico_delta.keys():
        (_,l) = t  
        alphabet.add(l)
    return alphabet


def construit_ens_etats_a_partir_de_delta(dico_delta):
    """Retourne l'ens. des états de l'automate dont la fonction delta est
    donnée sous forme de dictionnaire."""
    etat = set()
    for t in dico_delta.keys():
        (e,_) = t  
        etat.add(e)
    return etat

    
def est_mot_compatible(automate, mot_w):
    """Fonction Booléenne retournant True ssi les caractères du mot sont tous
    dans l'alphabet de l'automate."""
    for c in mot_w:
        if not c in alphabet(automate):
            return False
    return True

def delta_etoile(automate, etat_q, mot_w):
    """Retourne l'état de l'automate après le traitement du mot à partir de
    l'état q de l'automate."""
    delta_automate = delta(automate)
    for c in mot_w:
        etat_q = delta_automate.get((etat_q,c))
    return etat_q
    


def est_accepte(automate, mot_w):
    """Fonction Booléenne retournant True ssi mot_w est accepté par l'automate
    déterministe."""
    if not est_mot_compatible(automate,mot_w):
        return False
    return delta_etoile(automate,etat_initial(automate),mot_w) in ens_etats_accepteurs(automate)

def affiche_facteur(mot, indice_deb, indice_fin):
    """Affiche le facteur du mot entre des deux indices donnés,
    encadré par [...]"""
    print(mot[:indice_deb] + "[" + mot[indice_deb:indice_fin+1] + ']' + mot[indice_fin+1:])

def affiche_facteur_dans_mot(automate, mot_m, indice_i):
    """Affiche tous les facteurs f du mot mot_m, à partir de l'indice indice_i
    de celui-ci, avec la propriété que f est un mot (non vide) accepté par
    l'automate."""
    for j in range(indice_i,len(mot_m)-1):
        if est_accepte(automate,mot_m[indice_i:j+1]):   
            affiche_facteur(mot_m,indice_i,j)

def affiche_tous_les_facteurs(automate, mot_w):
    """Affiche tous les facteurs f du mot mot_w tels que f est un mot (non
    vide) accepté par l'automate. L'affichage est de la forme ...[...]...
    Le mot peut contenir des caractères qui ne sont pas dans l'alphabet de
    l'automate."""   
    for i in range(0,len(mot_w)):
        affiche_facteur_dans_mot(automate,mot_w,i)
        

def est_automate_deterministe(automate):
    """Fonction Booléenne retournant True ssi l'automate est déterministe."""
    pass


#---- Construction de l'automate 1
etat_initial_1 = 'q1'
ensemble_etats_accepteurs_1 = {'q3'}
delta_1 ={('q1','a') : 'q3', ('q1','b') : 'q1',
          ('q2','a') : 'q2', ('q2','b') : 'q1',
          ('q3','a') : 'q2', ('q3','b') : 'q3'}
automate_1 = (construit_alphabet_a_partir_de_delta(delta_1),
              construit_ens_etats_a_partir_de_delta(delta_1),
              etat_initial_1, ensemble_etats_accepteurs_1, delta_1)


#---- Construction de l'automate 2 : mots contenant un nombre pair de a dans
#---- ceux composés de a et de b uniquement.
etat_initial_2 = 'q1'
ensemble_etats_accepteurs_2 = {'q1'}
delta_2 ={('q1','a') : 'q2', ('q1','b') : 'q1',
          ('q2','a') : 'q1', ('q2','b') : 'q2'}
automate_2 = (construit_alphabet_a_partir_de_delta(delta_2),
              construit_ens_etats_a_partir_de_delta(delta_2),
              etat_initial_2, ensemble_etats_accepteurs_2, delta_2)


#---- Tests de diverses fonctions.
w = "abbaabbXYba"
if est_mot_compatible(automate_1, w):
    print(f'Le mot "{w}" est ' + 'accepté' if est_accepte(automate_1, w) else
          'refusé')
else:
    print(f'Le mot "{w}" contient des caractères qui ne sont pas '
          'dans l\'alphabet')

print("--"*10 + f'Facteurs de "{w}" de l\'Automate 1 :')
affiche_tous_les_facteurs(automate_1, w)

print("--"*10 + f'Facteurs de "{w}" de l\'Automate 2 :')
affiche_tous_les_facteurs(automate_2, w)

##--- Pour vous aider, voici ce que doit afficher cette dernière ligne :
##--------------------Facteurs de "abbaabbXYba" de l'Automate 2 :
##[abba]abbXYba
##a[b]baabbXYba
##a[bb]aabbXYba
##a[bbaa]bbXYba
##a[bbaab]bXYba
##a[bbaabb]XYba
##ab[b]aabbXYba
##ab[baa]bbXYba
##ab[baab]bXYba
##ab[baabb]XYba
##abb[aa]bbXYba
##abb[aab]bXYba
##abb[aabb]XYba
##abbaa[b]bXYba
##abbaa[bb]XYba
##abbaab[b]XYba
##abbaabbXY[b]a
