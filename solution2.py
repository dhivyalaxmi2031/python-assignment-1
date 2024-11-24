def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')

def power(a,b):
    return a**b

def floor_division(a,b):
    return a//b

def modulus(a,b):
    return a%b
 
def is_greater(a,b):
    return a > b

def is_lesser(a,b):
    return a < b

def is_equal(a,b):
    return a == b
