import sympy as sp
import math
x = sp.symbols('x')

print('câu 1')
f1 = (x*x -x -2) / (x-2)
f1Left = sp.limit(f1, x, 2, '-')
print ("Left limit = " , f1Left )
f1Right = sp.limit(f1, x, 2, '+')
print ("Right limit = " , f1Right )
if (f1Left == f1Right):
    lm1 = f1Left
else:
    lm1 = None
print(lm1)

print('câu 2')
f2 = (x*x -2*x -3) / (2*x-6)
f2Left = sp.limit(f2, x, 3, '-')
print ("Left limit = " , f2Left )
f2Right = sp.limit(f2, x, 3, '+')
print ("Right limit = " , f2Right )
if (f2Left == f2Right):
    lm2 = f2Left
else:
    lm2 = None
print(lm2)

