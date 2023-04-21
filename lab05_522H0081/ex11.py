import sympy as sp
import math

x = sp.symbols('x')
dx = sp.symbols('dx')

f1 = x*sp.sin(1/x)
df1 = (f1.subs(x, x0+dx) + f1.subs(x, x0) ) / dx


f2 = (x*x)*sp.sin(1/x)
df2 = (f2.subs(x, x0+dx) + f2.subs(x, x0) ) / dx

