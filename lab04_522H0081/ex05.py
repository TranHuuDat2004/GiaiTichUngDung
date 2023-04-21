import sympy as sp
import math
x = sp.symbols('x')

fa = x*x -7
lm5a = sp.limit(fa, x, 1)
print("5a - Giới hạn f(x) tại x = 1 là " + str(lm5a) )

fb = (2*x -3)**(1/2)
lm5b = sp.limit(fb, x, 2)
print("5b - Giới hạn f(x) tại x = 2 là " + str(lm5b) )