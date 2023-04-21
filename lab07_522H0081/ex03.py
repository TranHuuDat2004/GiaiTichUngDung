import sympy as sp
import math

x = sp.symbols('x')

print('Câu a')
fa = sp.cos(x)
a_taylor = fa.series(x, x0 = sp.pi / 3, n = 6) # x = x0 = sp.pi/3, Mũ = n = 6
print(a_taylor) # định luật Taylor


print('Câu b')
fb = sp.log(x)
b_taylor = fb.series(x, x0 = 2, n = 10)
print(b_taylor)

print('Câu c')
fc = sp.exp(x)
c_taylor = fc.series(x, x0 = 3, n = 12)
print(c_taylor)
