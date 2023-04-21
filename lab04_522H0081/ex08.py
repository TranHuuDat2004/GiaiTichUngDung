import sympy as sp
import math
x = sp.symbols('x')

f = 1 - (1 - x**2)**(1/2)
fa = sp.limit(f, x, -1 )
print ("Giới hạn f(x) tại x = -1 là " , fa )
fb = sp.limit(f, x, 1)
print ("Giới hạn f(x) tại x = 1 là " , fb )
if (fa == fb):
    lm = fa
else:
    lm = None
print(lm)
