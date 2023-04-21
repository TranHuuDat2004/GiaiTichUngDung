import sympy as sp
import math

x = sp.symbols('x')

print("Câu a")
f = x**2 * sp.cos(x)
print(sp.integrate(f, (x, -4, 9)))

print("Câu b")
a = 1/2
f = sp.exp(-a*x**2)
print(sp.integrate(f, (x, sp.oo, -sp.oo)))