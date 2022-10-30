import random


"""Each agency has a name (a string) and each candidate has a name (a string).
The same number n of agencies and candidates. 
An instance is:
    + A dictionary containing the choices of the agencies: 
    its keys are the names of agencies and the value of an entry 
    is the list of choices of this agency. 
    + A dictionary containing the choices of the candidates: 
    its keys are the names of candidates and the value of an entry 
    is the list of choices of this candidate.
Each list must be a permutation of the n elements of the choices.

An assignment is: 
    a candidate C for each agency A and 
    an agency A for each candidate C.
    This must be symmetric: A->C iff C->A.
An assignment is represented by two dictionaries. Each element (candidate or 
agency) is a key and its assigned element is a value. 
"""


#------------------------------------------------------------------------------
def extract_instance_from_file(file):
    number = 0
    cA = {}
    cC = {}
    with open (file,"r",encoding="utf-8") as f:
        number =  int(f.readline())
        for _ in range(number):
            l = f.readline().strip()
            liste = l.split(":")
            cA[liste[0]] = liste[1:]

        for _ in range(number):
            l = f.readline().strip()
            liste = l.split(":")
            cC[liste[0]] = liste[1:]

    return number,cA,cC
    
#------------------------------------------------------------------------------
def is_coherent(choices_agencies, choices_candidates):
    """Function that verifies if the two dictionaries are coherent i.e. if
     each value is a list containing each appropriated element exactly once.
      Returns True if it is the case and raises an
      Exception('Incorrect choices') otherwise."""

    print("Test cohérence choix\n")
    for a in choices_agencies:
        if set(choices_candidates.keys()) == set(choices_agencies[a]) and len(choices_agencies) == len(choices_agencies[a]):
            print(f"Choix cohérent pour {a}")
        else:
            raise ValueError(f"Choix incohérent avec {a}")
    for c in choices_candidates:
        if set(choices_candidates[c]) == set(choices_agencies.keys()) and len(choices_candidates) == len(choices_candidates[c]):
            print(f"Choix cohérent pour {c}")
        else:
            raise ValueError(f"Choix incohérent avec {c}")

#------------------------------------------------------------------------------
def generate_random_instance(n, version_number=1):
    """Generate a random instance with n agencies, n candidates and put the
    result in a file that is named GSEntries_Rand_{n}_{version_number}
    (for example GSEntries_Rand_10_3) to distinguish different random files."""
    with open(f"GSEntries_Rand_{n}_{version_number}","w",encoding = "utf-8") as f:
        listAgency = list(f"A{x}" for x in range(1,n+1))
        listCandidate = list(f"C{x}" for x in range (1,n+1))

        f.write(str(n) + "\n")

        for a in listAgency:
            f.write(f"{a}:{':'.join(random.sample(listCandidate,len(listCandidate)))}\n")
        for c in listCandidate:
            f.write(f"{c}:{':'.join(random.sample(listAgency,len(listAgency)))}\n")

        
      
        


#------------------------------------------------------------------------------
def is_assignment_symmetric(agen_assignment, candidate_assignment):
    """Boolean function that returns True if the assignments are coherent,
    symmetric."""

    print("Test symétrie assignement")
    
    for a in agen_assignment:
        if candidate_assignment[agen_assignment[a]] != a:
            return False
    return True


#------------------------------------------------------------------------------
def number_of_non_stable_couples(agencies_assign, candidates_assign,
                                 agencies_choices, candidates_choices):
    """Returns the number of non stable couples in the assignment."""

    number = 0
    choiceCandidateFind = False
    
    for a in agencies_choices.keys(): 
        for c in agencies_choices[a]:
            
            if choiceCandidateFind == False:
                if c == agencies_assign[a]:
                    break;
                
                for v in candidates_choices[c]:
                    
                    if v == candidates_assign[c]:
                        break;
                    elif v == a:
                        number += 1
                        choiceCandidateFind = True
                        break;
        
        choiceCandidateFind = False
    print(number)
    return number


#------------------------------------------------------------------------------
def generate_random_assignment(agencies_choices, candidates_choices):
    """Returns a random assignment as a 2 tuple of dictionaries."""
    
    aA = {}
    aC = {}
    l =random.sample(candidates_choices.keys(), len(candidates_choices))
    
    for i,a in enumerate(agencies_choices.keys()):
        aA[a] = l[i];
        aC[l[i]] = a;

    print("Selection Alea :")
    for a in aA:
        print (f"{a} --> {aA[a]}")
    print()
    for c in aC:
        print (f"{c} --> {aC[c]}")
    
    return aA,aC
    
#------------------------------------------------------------------------------
def Gale_Shapley(choiceAgency,choiceCandidate):
    
    aA,aC = generate_random_assignment(choiceAgency,choiceCandidate)
    choiceCandidateFind = False

    while number_of_non_stable_couples(aA,aC,choiceAgency,choiceCandidate) > 0:
        
        for a in choiceAgency.keys():
            for c in choiceAgency[a]:
                
                if choiceCandidateFind == False: 
                    if c == aA[a]:
                        break;
                    
                    for v in choiceCandidate[c]:
                        
                        if v == aC[c]:
                            break;
                        elif v == a:
                            aC[aA[a]] = aC[c]
                            aA[aC[c]] = aA[a]
                            aC[c] = a
                            aA[a] = c
                            choiceCandidateFind = True
                            break;
                        
            choiceCandidateFind = False

    return aA,aC

    
#------------------------------------------------------------------------------

choiceAgency = {}
choiceCandidate = {}
assignationCandidateSide = {}
assignationAgencySide = {}

generate_random_instance(10)

number,choiceAgency,choiceCandidate = extract_instance_from_file("GSEntries_Rand_10_1")

##for a in choiceAgency:
##    print (f"{a} --> {choiceAgency[a]}")
##print()
##for c in choiceCandidate:
##    print (f"{c} --> {choiceCandidate[c]}")



print("\n--------------------------------------\n")

is_coherent(choiceAgency,choiceCandidate)

print("\n--------------------------------------\n")

assignationAgencySide,assignationCandidateSide = Gale_Shapley(choiceAgency,choiceCandidate);

print("\n--------------------------------------\n")

print(f"L'assignement est-elle symétrique ? --> {is_assignment_symmetric(assignationAgencySide,assignationCandidateSide)}")

print("\n--------------------------------------\n")

for a in assignationAgencySide:
    print (f"{a} --> {assignationAgencySide[a]}")
print()
for c in assignationCandidateSide:
    print (f"{c} --> {assignationCandidateSide[c]}")

print("\n-------------------FIN-----------------\n")

    
