import sympy as sp
import math
x = sp.symbols('x')
z = sp.symbols('z')
t = sp.symbols('t')

fa= 4 - x*x
print('1a.', fa.diff())

fb = (x-1)**2 +1
print('1b.', fb.diff())

fc = 1 / (t*t)
print('1c.', fc.diff())

fd = (1-z) / (2*z)
print('1c.', fc.diff())

fe = sp.sqrt(3*z)
print('1e.', fe.diff())

ff = sp.sqrt(2*z + 1)
print('1f.', ff.diff())