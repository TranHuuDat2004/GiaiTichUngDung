import sympy as sp
import math
x = sp.symbols('x')
z = sp.symbols('z')

def getLim(fx):
    g = (fx.subs(x, z) - fx) / (z - x)
    return sp.limit(g, z, x)

print('câu 6a')
fa = 1 / (x-2)
print(getLim(fa))

print('câu 6b')
fb = x*x -3*x +4
print(getLim(fb))

print('câu 6c')
fc = x / (x - 1)
print(getLim(fc))

print('câu 6d')
fd = 1 + sp.sqrt(x)
print(getLim(fd))




