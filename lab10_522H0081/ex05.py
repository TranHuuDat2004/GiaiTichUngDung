import sympy as sp
import math

t = sp.symbols('t')

v = 160 - 32*t
print('Quãng đường hòn đá rơi là:', sp.integrate(v,(t, 0, 8)))