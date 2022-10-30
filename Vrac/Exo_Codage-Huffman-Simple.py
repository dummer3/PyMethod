"""Codage de Huffman.
Cette verion est purement pédagogique et ne pourrait pas servir de mise en
production efficace.
Chaque étape donne lieu à des objets intermédiares qui peuvent être affichés,
visualisés, contrôlés.
Cette version code des fichiers en UTF8 dont certains caractères sont codés sur
un, deux, trois ou quatre octets."""


def construit_liste_ss_arbres_caracteres_nombres(fichier, affiche = True):
    """Pour chaque caractère c du fichier, constuit une liste :
    [(c,n), None, None] où n est le nombre de fois que c est présent dans le
    fichier. Une telle liste sera vue plus tard comme une feuille.
    Si affiche == True, afficher les paires (c,n) dans l'ordre croissant de n.
    """
    liste = []
    
    with open(fichier,"r",encoding="utf-8") as f:
        dico = dict()
        for l in f:
            for c in l:
                try:
                    dico[c]+=1
                except KeyError:
                    dico[c]=1
        for c in dico.keys():
            liste.append([(c,dico[c]),None,None])

        liste = sorted(liste, key=lambda t: t[0][1])

        if affiche == True:
            print(liste)

        return liste
              
                
def construit_arbre_huffman_depuis_liste(liste_car_nbre):
    """À partir de la liste composée de listes du type [(c,n), None, None],
    construit et retourne l'arbre de Huffman suivant l'algorithme classique.
    Le résultat (l'arbre) est une liste composée de listes du type :
    [(c,n), a_1, a_2] avec :
    + n un entier.
    + c un caractère ; dans ce cas a_1 et a_2 sont None et c'est une feuille
        ou c est None ; Dans ce cas c'est un noeud interne et a_1 et a_2 sont
        des sous-arbres. Par convention, a_1 est le sous-arbre gauche codant 0
        et a_1 le sous-arbre droit codant 1."""
    while len(liste_car_nbre) > 1:
        nouv = [(None,liste_car_nbre[0][0][1]+liste_car_nbre[1][0][1]),liste_car_nbre[0],liste_car_nbre[1]]
        liste_car_nbre.pop(0);
        liste_car_nbre.pop(0);
        liste_car_nbre.append(nouv)
    return liste_car_nbre[0]
                                            
                                            
def construit_table_codage_depuis_arbre_huffman(arbre):
    """Construit la table de codage à partir de l'arbre de Huffman.
    Le resultat est un dictionnaire dont les clés sont les caractères et les
    valeurs sont les codes binaires correspondant issus de l'arbre. Un code
    binaire est retourné ici sous forme de chaine de cararctères de '0' et '1'.
    """
    def table_recursive(arbre,chaine):
        if(arbre[1] is not None):
            yield from table_recursive(arbre[1],chaine+"0")
        if(arbre[2] is not None):
            yield from table_recursive(arbre[2],chaine+"1")
        if(arbre[1] is None and arbre[2] is None):
            yield (arbre[0][0],chaine)
        


    dico = dict()
    it = table_recursive(arbre,"")
    for char,chaine in it:
        dico[char] = chaine
    print(dico)
    return dico


def code_fichier(fichier, table_codage):
    """Code chaque caractère du fichier avec la table de codage dont les clés
    sont les caractères et les valeurs les codes binaires sous forme de chaines
    de '0' et de '1'.
    Le résultat est une chaine de caractères de '0' et de '1'."""
    s=""
    with open(fichier,"r",encoding="utf-8") as r:
        for l in r:
            for c in l:
                s += table_codage.get(c)          
    with open(fichier + "[encodée]","w",encoding="utf-8") as w:
        w.write(s)
    return s

def decode_message(message_binaire, arbre):
    """Prend en entrée une chaine de caractères de '0' et de '1' (message codé)
    + un arbre de huffman. Retourne le décodage sous forme d'une chaine de
    caractères."""

    def decodage(message_binaire,sous_arbre,arbre):
        if len(message_binaire) > 0 and message_binaire[0] == '0' and sous_arbre[1] is not None :
            yield from decodage(message_binaire[1:],sous_arbre[1],arbre)
        elif len(message_binaire) > 0 and message_binaire[0] == '1' and sous_arbre[2] is not None :
            yield from decodage(message_binaire[1:],sous_arbre[2],arbre)
        else:
            yield sous_arbre[0][0]
            if len(message_binaire)>0:
                yield from decodage(message_binaire,arbre,arbre)

    s=""
    it = decodage(message_binaire,arbre,arbre)
    for c in it:
         s += c
    return s
        


#----- Manipulations de ces fonctions.

# Partie codage du fichier : 
fichier = "FICHIER_ESSAI_HUFFMAN.py"
#fichier = "Exo_Codage-Huffman-Simple.py" # Pour coder le fichier source...
liste_feuilles = construit_liste_ss_arbres_caracteres_nombres(fichier, True)
arbre = construit_arbre_huffman_depuis_liste(liste_feuilles)
table = construit_table_codage_depuis_arbre_huffman(arbre)
message_codé = code_fichier(fichier, table) # Codage Huffman en bin. du fichier 

print(f"Le message codé est :\n{message_codé}")
print(10*"---")
print(f"La taille du message codé est de : {len(message_codé)} bits, soit " +
      f"{len(message_codé)/8} octets.")
print(10*"---")

# Partie décodage :

message_décodé = decode_message(message_codé, arbre)
print(f"Le message décodé est : \n{message_décodé}")
