import sympy as sp
import math

print('Câu a')
f = lambda n: 4*n+1
for n in range(0, 10, 1):
    a = f(n)  
    print(a, end=',')

print('\nCâu b')
f = lambda n: 3**n
for n in range(0, 10, 1):
    b = f(n)  
    print(b, end=',')

print('\nCâu c')
f = lambda n: n**3
for n in range(0, 10, 1):
    c = f(n)  
    print(c, end=',')


print('\nCâu d')
def x(n):
    if n == 0 or n == 1:
        return 1
    return x(n-1) + x(n-2) # Fibonacci sequence

for n in range(2, 10, 1):
    b = x(n)
    print(b, end=',')
