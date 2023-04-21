import sympy as sp
from math import pi

x = sp.symbols('x')

# a
f = x**3 + 2*x**2 + 3
print("Câu a:", sp.integrate(f,(x, 1, 2)))

# b
f = (1/x**3) + (1/x**2)+ x
print("Câu b:", sp.integrate(f,(x, 1, 4)))

# c
f = (x**3 + x*sp.sqrt(x) + x ) / (x**2)
print("Câu c:", sp.integrate(f,(x, 1, 4)))

# d
f = (2/x) + x**3
print("Câu d:", sp.integrate(f,(x, 1, 2)))

# e
f = x**2 * ((1/x) + 2*x)
print("Câu e:", sp.integrate(f,(x, 1, 2)))

# f
f = (sp.sqrt(x) - 1) * (x + sp.sqrt(x) + 1)
print("Câu f:", sp.integrate(f,(x, 0, 1)))

# g
f = 1 - (2 / (sp.sin(x) * sp.sin(x)))
print("Câu g:", sp.integrate(f,(x, pi/4, pi/2)))

# h
f = 1 / ((sp.sin(x) * sp.sin(x))/(sp.cos(x) * sp.cos(x)))
print("Câu h:", sp.integrate(f,(x, pi/6, pi/4)))

# i
f = sp.exp(x) * (1 -  (sp.exp(-x)/ ( sp.cos(x) * sp.cos(x) )))
print("Câu i:", sp.integrate(f,(x, 0, pi/4)))

# j
f =  sp.exp(x) * (2 + (sp.exp(-x)/ sp.exp(x)))
print("Câu j:", sp.integrate(f,(x, 0, sp.log(2))))

# k
f =  2**x + (2/x)
print("Câu k:", sp.integrate(f,(x, 1, 2)))

# l
f =  x**2 * (x-1)**2
print("Câu l:", sp.integrate(f,(x, 0, 1)))

# m
f =  1 / (x* (x+1))
print("Câu m:", sp.integrate(f,(x, 1, 2)))

# n
f =  sp.Abs(1-x)
print("Câu n:", sp.integrate(f,(x, 0, 2)))

# o
f =  sp.Abs(2*x - x**2)
print("Câu o:", sp.integrate(f,(x, 0, 3)))

# p
f =  sp.sqrt(x**2 - 3*x + 2)
print("Câu p:", sp.integrate(f,(x, 2, 4)))

# q
# f =  sp.sqrt(1 + sp.cos(2*x))
# print("Câu q:", sp.integrate(f,(x, 0, pi)))