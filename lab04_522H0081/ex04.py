import sympy as sp
import math
x = sp.symbols('x')

fx = sp.sin(1/x)
fLeft = 0
print ("Left limit = " , fLeft )
fRight = sp.limit(fx, x, 0, '-')
print ("Right limit = " , fRight )
f = 0
if (fLeft == fRight):
    lm = fLeft
else:
    lm = None
print(lm)

