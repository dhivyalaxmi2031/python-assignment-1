def union_sets(set1, set2):
    return set1 | set2

def add_element(set1,set2):
    return set1.add(set2)

def is_subset(set1,set2):
    return set1 <= set2

def intersection_sets(set1, set2):
    return set1 & set2

def symmetric_difference(set1, num):
    return set1 ^ num

def  remove_element(set1, set2):
    result = set1.remove(set2)
    return result

def difference_sets(set1,set2):
    return set1 - set2

def is_disjoint(set1, set2):
    return set.isdisjoint(set2)

def clear_set(set1):
    return set1.clear()
