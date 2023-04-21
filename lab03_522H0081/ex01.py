import math

def fa(x):
    return math.sqrt(x)
print('a.',fa(4))

def fb(x):
    return x**(1/3)
print('b.',fb(9))

def fc(x):
    return x**(2/3)
print('c.',fc(27))

def fd(x):
    return (x**3)/3 - (x**2)/2 - 2*x + 1/3
print('d.',fd(3))

def fe(x):
    return ((2* (x**2) - 3) / (7*x + 4))
print('e.',fe(4))

def ff(x):
    return ( ( ( 5* (x**2) + 8*x ) -3 ) / (3*(x**2) +2 ) )
print('f.',ff(4))

def fg(x):
    return math.sin(x)
print('g.',fg(4))

def fh(x):
    return math.cos(x)
print('h.',fh(4))

def fi(x):
    return 3**x
print('i.',fi(4))

def fj(x):
    return 10**(-x)
print('j.',fj(4))

def fk(x):
    return math.exp(pow(x, x))
print('k.',fk(1))

def fl(x):
    return math.log(x, 2)
print('l.',fl(8))

def fm(x):
    return math.log(x, 10)
print('m.',fm(100))

def fn(x):
    return math.log(x, math.exp(1))
print('n.',fn(20))
