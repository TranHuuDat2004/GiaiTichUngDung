import sympy as sp
import math

x, y = sp.symbols('x, y')

print("Câu a")
f = x**3 - 3*sp.sin(x)*sp.cos(x)
integrals = sp.integrate(f, (x, 0, math.pi/2))
print(integrals)
sp.plotting.plot(f)

print("Câu b")
f = sp.sin(x**2)*sp.sin(x**2)
integrals = sp.integrate(f, (x, 0, 1))
print(integrals)
sp.plotting.plot(f)

print("Câu c")
g = lambda g:(x+1)
f = sp.sqrt(1 + g(x**2)+ (g(x))**2)
integrals = sp.integrate(f, (x, 0, 3))
print(integrals)
sp.plotting.plot(f)

print("Câu d")
fx = x*2*y
integrals_fx = sp.integrate(fx, (x, 0, 3))
integrals = sp.integrate(integrals_fx,(y, 1, 2))
print(integrals)
sp.plotting.plot(f)




