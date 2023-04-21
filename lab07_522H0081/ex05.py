import sympy as sp
import math

n = sp.symbols('n')

print('Câu a')
fa = (4*n*n + 1) / (3*n*n + 2)
a = sp.limit(fa, n, sp.oo)
print(a)

print('Câu b')
fb = sp.sqrt(n*n + 1) - n
b = sp.limit(fb, n, sp.oo)
print(b)

print('Câu c')
fc = sp.sqrt(2*n + sp.sqrt(n)) - sp.sqrt(2*n + 1 )
c = sp.limit(fc, n, sp.oo)
print(c)

print('Câu d')
fd = (3*(5**n) - (2**n)) / ((4**n) + 2.5**n)
d = sp.limit(fd, n, sp.oo)
print(d)

print('Câu e')
fe = (n* sp.sin(sp.sqrt(n))) / (n*n + n -1)
e = sp.limit(fe, n, sp.oo)
print(e)