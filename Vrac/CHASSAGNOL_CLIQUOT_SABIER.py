import random


"""Data structure of a formula F.
   -----------------------------
    A variable is a string (with no ',', no '&', no ' ' and no '-')
    A positive literal is a variable. 
    A negative literal is a variable with an additional '-' as first character.
    A clause is a list of literals.
    A formula is a list of clauses.
    
    The dictionary of a formula is the dictionary whose keys are the variables
    of the formula. 

   Boolean values of variables, literals, clauses, formulas.
   ---------------------------------------------------------
    An assignment for a formula is a Boolean value for each variable of the 
    dictionary of the formula. 
    Given a formula F and an assignment A:
        The boolean value of a positive literal with variable x is the Boolean
            value of A[x].
        The boolean value of a negative literal with variable x (-x) is the 
            Boolean value of not(A[x]).
        The boolean value of a clause is the logical OR Boolean value 
            of its literals. A clause is 'satisfied' if its value is True.
        The boolean value of a formula is the logical AND Boolean value 
            of its clauses. A formula is 'satisfied' if its value is True.
    
    Illustration.
    ------------
    F = [['a', '-b', 'c'], ['-a', 'b', '-d'], ['a', 'b', 'c'], ['-b', 'd', '-e']]
    The dictionary of F has keys 'a', 'b', 'c', 'd', 'e'
    An example of an assignment:
    {'a':False, 'b':True, 'c':True, 'd':False, 'e':False}
"""


def get_formula_from_file(file):
    """Extract a formula from file and returns it as a list.
    In file:
        A variable is a string (with no ',', no '&', no ' ' and no '-').
        A literal is either:
            a variable (positive literal) or a variable beginning with
            '-' (negative literal).
        Literals in clauses are separated by ','.
        Clauses are separated by '&'.
        Formula is on one line in the file.
    Example of formula: a,-b,cloclo&b,-a,-c&d,-a,-b&-cloclo,-name,-a,-b
    """

    with open (file,"r",encoding = "utf-8") as f:
        list_of_clauses =  next(f).strip().split("&")
        formula = []
        for c in list_of_clauses :
             formula.append(c.split(","))
    return formula


def variable_of_literal(literal):
    """Returns the name of the variable of the literal."""
    return literal.replace("-","");


def sign_of_literal(literal):
    """Returns the sign of the literal: '-' for a negative literal and
    '+' otherwise."""
    return '-' if literal[0] == '-' else '+'; 


def set_of_variables_from_formula(f):
    """Returns the set of the names of variables appearing in the formula."""
    return set(variable_of_literal(x) for t in f for x in t)

def construct_dictionary_from_vars(set_of_vars):
    """Constructs a dictionary from the set of variables.
    The value of each entry is None (no assignment)."""
    return {x : None for x in set_of_vars}       


def random_assignment(d):
    """Takes a dictionary as input and puts a random Boolean value to each
    variable. """
    for i in d:
        d[i] = True if random.randint(0, 1) == 1 else False


def boolean_value_of_literal(assignment, literal):
    """Given an assignment and a literal, returns the Boolean value of the
       literal."""
    return not assignment[variable_of_literal(literal)] if sign_of_literal(literal) == '-' \
           else assignment[variable_of_literal(literal)]


def boolean_value_of_clause(assignment, clause):
    """Given an assignment and a clause, returns the Boolean value of the
       clause."""
    result = False
    it = iter(clause)
    while not(result):
        try:
            result |= boolean_value_of_literal(assignment, next(it))
        except StopIteration:
            break

    return result


def boolean_value_of_formula(assignment, formula):
    """Given an assignment and a formula, returns the Boolean value of the
       formula."""
    result = True
    it = iter(formula)
    while result:
        try:
            result &= boolean_value_of_clause(assignment, next(it))
        except StopIteration:
            break

    return result


def number_of_true_clauses(assignment, formula):
    """Given an assignment and a formula, returns the number of clauses having
       a Boolean value True."""
    nbr = 0
    for clause in formula:
        nbr += 1 if boolean_value_of_clause(assignment,clause) == True else 0
    return nbr


def number_of_clauses(formula):
    """Returns the number of clauses of the formula."""
    return len(formula)


def pretty_print_formula(formula):
    """Print a nice/readable view of the formula."""
    for c in formula :
        for l in c[:-1]:
            print(f'{l:>2} or ',end = "")
        print(f'{c[-1]:>2}')
        

def pretty_print_assigned_formula(assignment, formula):
    """Print a nice/readable view of the formula with each variable replaced
       by its Boolean value; also print the value of each clause. Illustration
       True       not(False) True        = True
       not(True)  False      not(True)   = False
       True       False      True        = True"""

    for c in formula:
       for l in c :
           s = f"not({assignment[variable_of_literal(l)]})" if sign_of_literal(l) == '-' else f"{assignment[variable_of_literal(l)]}"
           tmp = 11-len(s)
           s += " "*tmp
           print(s,end="")
       print(" = "+str(boolean_value_of_clause(assignment,c)))
    print()
    
def random_formula(n=26, c=10, min_len=1, max_len=10, file="FX"):
    """Generate a random formula with at most n variables, exactly c clauses,
       each with at least min_len literals and at most max_len literals.
    Put the final formula in file.
    Each variable must be a non capital letter (a, b, c,...,z). """
    list_variable = [chr(ord('a')+i) for i in range(n)]

    with open(file,'w',encoding='utf8') as f:
        for nbClause in range(c-1):

            lenClause = random.randint(min_len,max_len)

            random.shuffle(list_variable)
            
            f.write(','.join([list_variable[i] if random.randint(0,1) == 1 \

                     else '-'+list_variable[i] for i in range(lenClause)])+ '&')

        lenClause = random.randint(min_len,max_len)
        random.shuffle(list_variable)
        f.write(','.join([list_variable[i] if random.randint(0,1) == 1 \
                     else '-'+list_variable[i] for i in range(lenClause)]))
        
            


def iter_all_assignments(d):
    """An iterator to generate all the possible assignments of a dictionary d.
    NB: the call returns an iterator of assignments, not the assignments."""
    all_assignments = []
    n = len(d)
    for x in range(2 ** n):
        l = [(x >> i) % 2 for i in range(n)]
        for i, litt in enumerate(d):
            d[litt] = False if l[i] == 0 else True

        all_assignments.append(d.copy())

    return iter(all_assignments)


def evaluate_all_assignments(formula):
    """Returns, for each possible assignment of the variables of the formula,
    the list of the number of satisfied clauses (with Boolean value True)."""
    d = construct_dictionary_from_vars(set_of_variables_from_formula(formula))
    it = iter_all_assignments(d)
    result = []
    while True:
        try:
            assignment = next(it)
            count = 0
            for clause in formula:
                if boolean_value_of_clause(assignment, clause):
                    count += 1
            result.append(count)
        except StopIteration:
            break

    return result


"""
Example of pretty print of formula a,-b,c&-a,b,-d&a,b,c&-b,d,-e&a,-c,e :
 a or -b or  c
-a or  b or -d
 a or  b or  c
-b or  d or -e
 a or -c or  e

Example of a pretty print of an assignment for this formula:

False      not(False) False       = True
not(False) False      not(False)  = True
False      False      False       = False
not(False) False      not(True)   = True
False      not(False) True        = True """

random_formula(n = 4,c = 3, min_len = 1,max_len = 3)
f = get_formula_from_file("FX")
s = set_of_variables_from_formula(f)
d = construct_dictionary_from_vars(s)
random_assignment(d)

all_assign = evaluate_all_assignments(f)

"""Voici du code de test à ajouter après la définition de vos fonctions
(à la fin de votre fichier).
Interdiction de modifier les lignes suivantes. Interdition d'utiliser
une autre bibliothèque que random. Seuls les résultats des appels suivants
doivent s'afficher, rien d'autre. """

f1 = [['aa', '-bbbb', '-c'], ['-aa', '-bbbb', '-dd'], ['aa', 'bbbb', 'c'],
     ['-bbbb', 'd', '-e']]
dico_f1 = construct_dictionary_from_vars(set_of_variables_from_formula(f1))
print("La formule est :", f1)
print(f"L'ens. de ses var. est : {set_of_variables_from_formula(f1)}.")

print(f"La variable contenue dans le litéral {'aa'} est : " + 
      variable_of_literal('aa'))

print(f"La variable contenue dans le litéral {'-dd'} est : " +
      variable_of_literal("-dd"))

for var in dico_f1:
    dico_f1[var] = True

print("Voici une affectation où toutes les varaibles sont à True :\n",
      dico_f1)

print("Avec cette affectation on a les valeurs Boll. suivantes :")

une_clause = f1[0]
for litéral in une_clause:
      print(f"Le litéral {litéral} a la valeur : ",
            boolean_value_of_literal(dico_f1, litéral))

for clause in f1:
    print(f"La clause {clause} a la valeur : ",
        boolean_value_of_clause(dico_f1, clause))  

print(f"La formule a la valeur : ",
      boolean_value_of_formula(dico_f1, f1))

print(f"La formule a {number_of_true_clauses(dico_f1, f1)} clauses à Vrai.")

liste_nbr_clauses_vraies = evaluate_all_assignments(f1)
liste_nbr_clauses_vraies.sort()
print(f"Liste (triée) du nombre de clauses vraies de la formule : ")
print(liste_nbr_clauses_vraies)
print(f"La longueur de cette listes est : {len(liste_nbr_clauses_vraies)}.")
##print("Construisons un itérateur d'affectations un peu plus gros...")
##dico = {chr(i) : None for i in range(65, 65 + 26)} 
##it = iter_all_assignments(dico)
##print("Voici l'itérateur généré : ", it)
##print("Explorons un peu cet itérateur...")
##for _ in range(3):
##    print(next(it))
##


