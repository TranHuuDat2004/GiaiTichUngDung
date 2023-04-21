import math
import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt


x = sp.symbols('x')

print('cáu 8a')
fa = x**3 - 3*x + 1
x0 = 3
dfa = fa.diff()
sa = dfa.subs(x, x0)    #f'(x0)
y = fa.subs(x, x0)
tta = sa*(x - x0) + y
print(tta)

print('cáu 8b')
fb = x + (5/x)
x0 = 3
dfb = fb.diff()
sb = dfb.subs(x, x0)    #f'(x0)
y = fb.subs(x, x0)
ttb = sb*(x - x0) + y
print(ttb)

fc = x**3 -3*x +1
print('cáu 8c')
A = (2/3, -1)
dfc = fc.diff()
sc = dfc.subs(x, 2/3)
ttc = sc*(x - A[0]) + A[1]
print(ttc)