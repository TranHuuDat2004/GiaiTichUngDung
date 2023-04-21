import sympy as sp
import math

x = sp.symbols('x')

c = 1 / (2 * sp.sqrt(x))
tien = sp.integrate(c, (x, 2, 100)).evalf()
print("Giá tiền để in poster là:", '%.4f'%(tien) , "dollars")