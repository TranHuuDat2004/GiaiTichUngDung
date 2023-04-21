import sympy as sp
import math
x = sp.symbols('x')

print('câu 3.1:')
f1 = 1/( 1 + 2**(1/x) )
f1Right = sp.limit(f1, x, 0, '+')
print ("Right limit = " , f1Right )
f1Left = sp.limit(f1, x, 0, '-')
print ("Left limit = " , f1Left )
if (f1Left == f1Right):
    lm1 = f1Left
else:
    lm1 = None
print(lm1)

print('câu 3.2:')
f2 =  ( (x*x + x) / (x**3 + x**2)**(1/2) )
f2Right = sp.limit(f2, x, 0, '+')
print ("Right limit = " , f2Right )
f2Left = sp.limit(f2, x, 0, '-')
print ("Left limit = " , f2Left )
if (f2Left == f2Right):
    lm2 = f2Left
else:
    lm2 = None
print(lm2)

