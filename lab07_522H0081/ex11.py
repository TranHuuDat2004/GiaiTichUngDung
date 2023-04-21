import sympy as sp
import math

P = 28000
i = 3/100
a = lambda n: P*(1+i)**n
for n in range(1, 4, 1):
    b = a(n)
    print(b)
