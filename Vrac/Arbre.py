"""Library to manipulate Binary search tree (named ABR here).
 An ABR is a list of 4 elements:
 [0] A left tree (an ABR),
 [1] A key: a tuple (value, label) where value must be numeric and
    label is any format.
 [2] A right tree (an ABR).
 [3] The parent (None if the node is the root of the ABR).
 Organisation of keys:
    + Keys of all nodes of left tree must have values strictly less than
    to the one of the node.
    + Keys of all nodes of right tree must have values greater than or equal
    to the one of the node.
    + An empty sub-tree (left or right) is referenced by a None value.
 Warning:
     + multiple keys having the same value are allowed here.
     + Multiple same keys are allowed here (this is not a set structure).
"""


def val_abr(abr):
    """Return the value of the ABR."""
    return abr[1][0]


def key_abr(abr):
    """Return the key of the ABR."""
    return abr[1]


def left_tree_abr(abr):
    """Return the left tree of the ABR."""
    return abr[0]


def right_tree_abr(abr):
    """Return the right tree of the ABR."""
    return abr[2]


def parent_abr(abr):
    """Return the parent tree of the ABR."""
    return abr[3]


def create_abr(key, parent=None):
    """Create and return an ABR with given key and parent."""
    return [None, key, None, parent]


def insert_abr(key, abr):
    """Insert Key=(value, label) in ABR. Warning: Does NOT verify if the key
    is already in ABR. Insertion in place (modification of the ABR)."""
    test = True
    while test:

        if key[0] < abr[1][0] and abr[0] is not None:
            abr = abr[0]

        elif key[0] >= abr[1][0] and abr[2] is not None:
            abr = abr[2]

        elif key[0] < abr[1][0] and abr[0] is None:
            abr[0] = create_abr(key, abr)
            test = False

        elif key[0] >= abr[1][0] and abr[2] is None:
            abr[2] = create_abr(key, abr)
            test = False


def find_minimum_key_abr(abr):
    """Find and return a key with minimum value of ABR.
    If several keys have minimum value, return one of them."""
    while left_tree_abr(abr) != None:
        abr = left_tree_abr(abr)
    return key_abr(abr)


def find_maximum_key_abr(abr):
    """Find and return a key with maximal value of ABR.
    If several keys have maximal value, return one of them."""
    while right_tree_abr(abr) != None:
        abr = right_tree_abr(abr)
    return key_abr(abr)


def find_abr(value, abr):
    """"Find and return a subtree of abr whose key have the value.
    If several keys have this value, return one of them and return None if
    the value is not present."""
    if val_abr(abr) > value:
        if left_tree_abr(abr) != None:
            return find_abr(value,left_tree_abr(abr))
        else:
            return None
    elif val_abr(abr) < value:
        if right_tree_abr(abr) != None:
            return find_abr(value,right_tree_abr(abr))
        else:
            return None
    return abr


def find_minimum_subtree_abr(sub_abr):
    """Find and return a subtree whose root key has maximum value of ABR.
    If several keys have maximal value, return one of these trees."""
    return find_abr(find_minimum_key_abr(sub_abr)[0], sub_abr)


def list_of_keys_abr(abr):
    """Return the list of all the keys of ABR. Sorted in increasing values.
    """
    l = []
    if left_tree_abr(abr) != None:
        l += list_of_keys_abr(left_tree_abr(abr))
    l += [key_abr(abr)]
    if right_tree_abr(abr) != None:
        l += list_of_keys_abr(right_tree_abr(abr))

    return l


def iter_on_keys_abr(abr):
    """An iterator on the keys of the ABR."""
    yield key_abr(abr)
    if left_tree_abr(abr) != None:
        yield from iter_on_keys_abr(left_tree_abr(abr))
    if right_tree_abr(abr) != None:
        yield from iter_on_keys_abr(right_tree_abr(abr))


def len_abr(abr):
    """Return the number of keys in ABR. If several keys are the same, they are
    multiply counted."""
    return len(list_of_keys_abr(abr))


def print_abr(abr):
    """Print a "flat" (list) view of the ABR."""
    print(7 * "-")
    print(f"The root key of the ABR is {key_abr(abr)} and ABR is: \n{abr}")


def pretty_print_abr(abr, level=0):
    """Print a horizontal tree-like view of the ABR.
    Does NOT print parent field."""
    def dec(l):
        return (4 * l) * " "

    if left_tree_abr(abr) is not None:
        pretty_print_abr(left_tree_abr(abr), level + 1)
    else:
        print(dec(level + 1) + "Empty")
    print(dec(level) + f"{key_abr(abr)}")
    if right_tree_abr(abr) is not None:
        pretty_print_abr(right_tree_abr(abr), level + 1)
    else:
        print(dec(level + 1) + "Empty")


def error_structure_abr(message):
    print(f"ERROR: ABR not coherent. " + message)
    return False


def is_coherent_abr(abr):
    """Check is the ABR is well structured."""
    current_value = val_abr(abr)
    result = True
    if left_tree_abr(abr) != None:
        if val_abr(left_tree_abr(abr)) < current_value:
            result &= is_coherent_abr(left_tree_abr(abr))
        else:
            return False
    if right_tree_abr(abr) != None:
        if val_abr(right_tree_abr(abr)) >= current_value:
            result &= is_coherent_abr(right_tree_abr(abr))
        else:
            return False

    return result


def destroy_abr(abr):
    """Remove the 4 fields of the ABR with pop().
    Warning: at the end abr is a reference to an empty list []."""
    if left_tree_abr(abr) != None:
        destroy_abr(left_tree_abr(abr))

        if right_tree_abr(abr) != None:
            destroy_abr(right_tree_abr(abr))

        for _ in range(4):
            abr.pop()


# -------- The next function is used later to delete a node with a given key. --
def find_next_abr(sub_abr):
    """Find and return a subtree whose root key has a value that is the next
    one of val_abr(sub_abr). Return None if it is the maximum value.
    Note that the result is necessarily in this sub_abr."""
    def next_abr(value, abr):
        if right_tree_abr(abr) != None and val_abr(right_tree_abr(abr)) > value:
            return right_tree_abr(abr)
        elif val_abr(parent_abr(abr)) > value:
            return parent_abr(abr)
        else:
            return next_abr(value, parent_abr(abr))

    return next_abr(val_abr(sub_abr), sub_abr)


# ------- This fonction is used to delete a node with a given value. -----------
def delete_val_abr(val, abr):
    """Find any key with value val and delete it form abr.
    If the value val is not in the ABR, only a warning message is printed.
    IMPORTANT: the modification is in place but the function returns the new
    reference on the new ABR since the root may change.
    Usage should be of the form: abr = delete_val_abr(10, abr)."""
    def delete_key_subabr_abr(sub_abr):
        """Delete the key at the root of the sub_abr in the ABR. """
        nonlocal abr  # The root of ABR may change during deletion.
        minimum = find_minimum_subtree_abr(right_tree_abr(sub_abr))
        sub_abr[1] = key_abr(minimum)
        if right_tree_abr(minimum) != None:
            right_tree_abr(minimum)[3] = parent_abr(minimum) 
        parent_abr(minimum)[0] =  right_tree_abr(minimum)

        

    if abr[2] != None:
        delete_key_subabr_abr(find_abr(val, abr))
        return abr
    else:
        abr[0][3] = None
        return abr[0]


class ValueNotInAbr(Exception):
    pass


def find_next_key_abr(val, abr):
    """Find and return the key of ABR whose value is the next one of val.
    Return None if val is the maximum value of the ABR.
    Raise ValueNotInAbr exception if the value is not in the ABR."""
    sub_abr = find_abr(val, abr)
    if sub_abr == None:
        raise ValueNotInAbr
    else:
        return key_abr(find_next_abr(sub_abr))
    
# ----------- Tests --------------
abr_global = create_abr((20, "A"))
print_abr(abr_global)
insert_abr((10, "B"), abr_global)
print_abr(abr_global)
insert_abr((15, "C"), abr_global)
print_abr(abr_global)
insert_abr((40, "D"), abr_global)
print_abr(abr_global)
insert_abr((25, "E"), abr_global)
print_abr(abr_global)
insert_abr((10, "F"), abr_global)  # Support many equal values.
print_abr(abr_global)
insert_abr((30, "G"), abr_global)
print_abr(abr_global)
abr_global = delete_val_abr(10, abr_global)
print_abr(abr_global)
abr_global = delete_val_abr(20, abr_global)
print_abr(abr_global)
insert_abr((100, "Z"), abr_global)
print_abr(abr_global)

print(f"The min key of the current ABR is: {find_minimum_key_abr(abr_global)}")
print(f"The max key of the current ABR is: {find_maximum_key_abr(abr_global)}")
print(f"The list of keys is {list_of_keys_abr(abr_global)}")
print(f"The ABR contains {len_abr(abr_global)} elements")
print(f"Key of the next value of 15 is {find_next_key_abr(15, abr_global)}")
pretty_print_abr(abr_global, 0)
print(f"Is ABR coherent? {is_coherent_abr(abr_global)}")

print("------ Test of iterator ------")
it = iter_on_keys_abr(abr_global)
for x in it:
    print(x)
