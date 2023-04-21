import numpy as np
import sympy as sp
import math
x = sp.symbols('x')

fa = sp.sin(x) / x
lm10a = sp.limit(fa, x, 0)
print("10a - Giá trị L là " + str(lm10a) )

fb = (x*x +x -6) / (x*x -4)
lm10b = sp.limit(fb, x, 2)
print("10b - Giá trị L là " + str(lm10b) )
