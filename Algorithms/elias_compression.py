from math import log

def log_2(x):
    return log(x,2)

def binary(x: int, l: int=1):
    fmt = '{0:0%db}' % l
    return fmt.format(x)

def unary(x: int):
    return (x-1) * '1' + '0'


def elias_generic(lencoding: callable, x: int):
    if x == 0:
        return '0'

    first_part = 1 + int(log_2(x))
    
    a = x - 2**(int(log_2(x)))

    k = int(log_2(x))
    
    return lencoding(first_part) + binary(a, k)

def elias_gamma(x):
    return elias_generic(unary, x)

def elias_delta(x):
    return elias_generic(elias_gamma, x)


# test

# Elias Gamma
print("---- Elias Gamma ----")
print(elias_gamma(1)) # returns -> "0"
print(elias_gamma(2)) # returns -> "100"
print(elias_gamma(3)) # returns -> "101"
print(elias_gamma(4)) # returns -> "11000"

# Elias Delta
print("---- Elias Delta ----")
print(elias_delta(1)) # returns -> "0"
print(elias_delta(2)) # returns -> "1000"
print(elias_delta(3)) # returns -> "1001"
print(elias_delta(4)) # returns -> "10100"

