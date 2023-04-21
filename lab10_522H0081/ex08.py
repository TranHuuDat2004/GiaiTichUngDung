import sympy as sp
from math import pi

x = sp.symbols('x')

print('Câu a')
f = 1 - x
a, b = 0, 1
sp.plotting.plot(f)
integrals = sp.integrate(f, (x, a, b))
print(integrals)
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)

print('Câu b')
f = x**2 + 1
a, b = 0, 1
sp.plotting.plot(f)
integrals = sp.integrate(f, (x, a, b))
print(integrals)
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)

print('Câu c')
f = sp.cos(x)
a, b = -pi, pi
sp.plotting.plot(f)
integrals = sp.integrate(f, (x, a, b))
print(integrals)
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)

print('Câu d')
f = sp.Abs(x)
a, b = -1, 1
sp.plotting.plot(f)
integrals = sp.integrate(f, (x, a, b))
print(integrals)
average = 1 / (b - a) * sp.integrate(f, (x, a, b))
print(average)