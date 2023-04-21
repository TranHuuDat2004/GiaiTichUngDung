import sympy as sp
import math

x = sp.symbols('x')
dx = sp.symbols('dx') #denta(x)

def getLim(fx, x0):
    g = (fx.subs(x, x0+dx) - fx.subs(x, x0)) /dx
    return sp.limit(g, dx, 0)  #thề dx=0 vào biến g

print('câu 5a')
fa = 4 - x*x
for x0 in [-3, 0, 1]:
    print(getLim(fa, x0))  # hàm def getLim(fx, x0):


print('câu 5b')
fb = (x - 1) **2 +1 
for x0 in [-1, 0, 2]:
    print(getLim(fb, x0))

print('câu 5c')
fc = 1 / (x*x)
for x0 in [-1, 2, sp.sqrt(3)]:
    print(getLim(fc, x0))

print('câu 5d')
fd = (1-x) / 2*x
for x0 in [-1, 1, sp.sqrt(2)]:
    print(getLim(fb, x0))


