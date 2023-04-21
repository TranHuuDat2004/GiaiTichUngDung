import sympy as sp
import math

x = sp.symbols('x')

print("Câu a")
f = x**2 - 1
a, b = 0, sp.sqrt(3)
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)

print("Câu b")
f = -(x**2) / 2
a, b = 0, 3
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)

print("Câu c")
f = -3*x**2 - 1
a, b = 0, 1
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)

print("Câu d")
f = x**2 - x
a, b = -2, 1
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)