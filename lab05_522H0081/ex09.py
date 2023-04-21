import sympy as sp
from sympy.plotting import plot
import math

x = sp.symbols('x')
f = 4*x*x - x**3
df = f.diff()
A = (2, 8) # xA = A[0] = 2, # yA = A[1] = 8
B = (3, 9)

#tg1
tg1 = df.subs(x, A[0]) * (x-A[0]) + A[1] 
print(tg1)
#tg2
tg2 = df.subs(x, B[0]) * (x-B[0]) + B[1] 
print(tg2)

g = plot(f, (x, 0, 5), show=False)
g.append(plot(tg1, show=False)[0])
g.append(plot(tg2, show=False)[0])
g.show()

