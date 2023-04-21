import sympy as sp
import math

n = sp.symbols('n')
phi = 1.618034

print('Câu a')
def a(n):
    if n == 0 or n == 1:
        return 1
    return a(n-1) + a(n-2) # Fibonacci sequence

for n in range(2, 10, 1):
    b = a(n)
    print(b, end=',')

print('\nCâu b')
def b(i):
    b = 1
    for i in range(2, 6, 1):
        b = b + (phi**i - (1 - phi))/ sp.sqrt(5)
    return b

for i in range(1, 6, 1):
    print(b(i), end=',')

print('\nCâu c')
def c(i):
    a = 1
    for i in range(2, i+1, 1):
        a = a*phi
    return int(a)

for i in range(1, 6, 1):
    print(c(i), end=',')