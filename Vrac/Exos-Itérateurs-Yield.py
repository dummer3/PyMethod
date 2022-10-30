# Exercices Python sur les itérateurs, yield, yield from.
# Utilisez chaque itérateur pour produire des éléments. 

#------------------------------------------------------------------------------
def iter_syracuse(n):
    if n > 1: 
        if n%2 :
            n = n*3+1;
        else :
            n = n//2;
            
        yield n;
        yield from iter_syracuse(n);

#------------------------------------------------------------------------------
def iter_fibo():
    yield from iter_fibo_aux(1,1);

def iter_fibo_aux(a,b):
    c = a+b;
    yield a+b
    yield from iter_fibo_aux(c,a);

#------------------------------------------------------------------------------
def look_and_say_iter(z, k=1):
    if(k > 0):
        valDeRef = z[0]
        
        s = ''
        compt = 1;
        if len(z) == 1 :
            z = '1'+z;
        else :
            for c in z[1:]:
                if valDeRef == c:
                    compt += 1;
                else:
                    s += str(compt);
                    compt = 1;
                    s += valDeRef;
                    valDeRef = c;
           
            s += str(compt);  
            s += valDeRef;
            z = s
        yield z
        yield from look_and_say_iter(z,k-1)
        

#------------------------------------------------------------------------------
def iter_tous_les_facteurs(mot):
    yield from iter_tous_les_facteurs_aux(mot,0,1);


def iter_tous_les_facteurs_aux(mot,depart,arrive):
    if depart < len(mot) :
        yield mot[depart:arrive];

        if arrive == len(mot):
            depart += 1;
            arrive = depart+1;
        else :
            arrive += 1;
            
        yield from iter_tous_les_facteurs_aux(mot,depart,arrive);

#------------------------------------------------------------------------------
def iter_toutes_les_listes_binaires(n):
    """Itérateur produisant toutes les listes de {0, 1} de taille n."""
    yield from iter_toutes_les_listes_binaires_aux(n,0);

def iter_toutes_les_listes_binaires_aux(n,v):
    v_save = v+1;
    if v < 2**n:
        l = []
        for _ in range(n):
            l.append(v%2);
            v = v // 2;

        yield l; 
        yield from iter_toutes_les_listes_binaires_aux(n,v_save);
            

    #------------------------------------------------------------------------------
def iter_nombres_premiers(v=2):
    
    if estPremier(v):    
        yield v
        
    v += 1;
        
    yield from iter_nombres_premiers(v+1);

def estPremier(v):
    
    import math  
    for i in range(2,int(math.sqrt(v)) + 1):
        if v%i == 0:
            return False
            
    return True

#------------------------------------------------------------------------------
def iter_tous_les_sous_ensembles(ensemble):
    
    def aux(ensembleDeBase,ensemble):
        if(len(ensembleDeBase) > 0):
            yield from aux(ensembleDeBase[1:],ensemble.copy())
            ensemble.append(ensembleDeBase[0])
            yield from aux(ensembleDeBase[1:],ensemble.copy())
        else:
            yield ensemble

    yield from aux(list(ensemble),[])
    yield ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
    yield from iter_tous_les_sous_ensembles_aux(ensemble,0)
    
def iter_tous_les_sous_ensembles_aux(n,v):
    v_save = v+1;
    
    if v < 2 ** len(n):
        l = []
        for i in n:
            if v%2 == 1 :
                l.append(i)
            v = v // 2

        yield l 
        yield from iter_tous_les_sous_ensembles_aux(n,v_save)

it = iter_tous_les_sous_ensembles({1,2,3,4,5,6,7})
for i in it:
    print (i)
