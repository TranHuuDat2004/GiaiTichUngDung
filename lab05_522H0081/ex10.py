import sympy as sp
import math

x = sp.symbols('x')
dx = sp.symbols('dx')

x0 = 1
f1 = (x-1)**(1/3)
df1 = (f1.subs(x, x0+dx) + f1.subs(x, x0) ) / dx
print('đạo hàm=',df1)
a = df1.subs(x, 1)
print(a)

if x <= -2:
    f2 = -(x+2)
elif x > -2:
    f2 = (x+2)

if x >= 0:
    f3 = x*x
elif x == 0:
    f3 = 0