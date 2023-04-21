import math 
import numpy as np

print('Câu a:')
def fa(x):
    return 2 + (x**2 / (x**2 + 4))
    
def ta():
    min = math.inf
    max = -math.inf

    for x in np.arange(-2, 2.1, 0.1):
        y = fa(x)
        if y < min:
            min = y
        if y > max:
            max = y

    return min, max

res = ta()
print(type(res))
a, b = ta()     # a = min, b = max 
print('min là','%.4f'%a)
print('max la','%.4f'%b)


print('\nCâu b:')
def fb(x):
    return math.sqrt(5 * x + 10)
    
def tb():
    min = math.inf
    max = -math.inf

    for x in np.arange(0, 5.25, 0.25):
        y = fb(x)
        if y < min:
            min = y
        if y > max:
            max = y

    return min, max

res = tb()
a, b = tb()
print('min là','%.4f'%a)
print('max la','%.4f'%b)


print('\nCâu c:')
def fc(x):
    return 2 / (x**2 - 16)
    
def tc():
    min = math.inf
    max = -math.inf

    for x in np.arange(5, 11, 1):
        y = fc(x)
        if y < min:
            min = y
        if y > max:
            max = y

    return min, max

res = tc()
a, b = tc()
print('min là','%.4f'%a)
print('max la','%.4f'%b)


print('\nCâu d:')
def fd(x):
    return x**4 + (3*x**2) - 1
    
def td():
    min = math.inf
    max = -math.inf

    for x in np.arange(-3, 3.25, 0.25):
        y = fd(x)
        if y < min:
            min = y
        if y > max:
            max = y

    return min, max

res = td()
a, b = td()
print('min là','%.4f'%a)
print('max la','%.4f'%b)


print('\nCâu e:')
def fe(x):
    if x >= 0:
        return x

    else:
        return - x
    
def te():
    min = math.inf
    max = -math.inf

    for x in np.arange(-3, 3.25, 0.25):
        y = fe(x)
        if y < min:
            min = y
        if y > max:
            max = y

    return min, max

res = te()
a, b = te()
print('min là','%.4f'%a)
print('max la','%.4f'%b)
