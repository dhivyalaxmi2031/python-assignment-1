def find_max(lst):
    return max(lst)

def list_sum(lst):
    return sum(lst)

def append_element(lst,num):
    lst.append(num)
    return lst

def average(lst):
    return sum(lst) / len(lst)


def remove_element(lst,num):
    if num in lst:
        lst.remove(num)
    return lst

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def count_occurrences(lst,num):
    return lst.count(num)

def find_index(lst,num):
    return lst.index(num)
