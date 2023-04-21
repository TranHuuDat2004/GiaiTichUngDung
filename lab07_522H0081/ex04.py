import sympy as sp
import math

x = sp.symbols('x')

print('Câu a')
f = sp.cos(x)
a_maclaurin = f.series(x, x0 = 0, n = 6)
print(a_maclaurin)  # định luật Maclaurin giống Taylor với x0 = 0

print('Câu b')
f = sp.exp(x)
b_maclaurin = f.series(x, x0 = 0, n = 12)
print(b_maclaurin)

print('Câu c')
f = 1/(1-x)
c_maclaurin = f.series(x, x0 = 0, n = 12)
print(c_maclaurin)

print('Câu d')
f = sp.atan(x)
d_maclaurin = f.series(x, x0 = 0, n = 12)
print(d_maclaurin)