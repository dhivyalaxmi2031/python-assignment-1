def reverse_string(a):
    return a[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count

def to_uppercase(a):
    b = a.upper()
    return b

def is_palindrome(s):
    result = ''.join(char.lower() for char in s)
    return result == result[::-1]

def replace_substring(s, old, new):
    return s.replace(old,new)
 
def split_string(s,sp):
    return s.split(sp)

def join_strings(s,delimiter):
    return delimiter.join(s)
    
def find_substring(s,target):
    return s.find(target)
    
def capitalize_string(s):
    return s.capitalize()
