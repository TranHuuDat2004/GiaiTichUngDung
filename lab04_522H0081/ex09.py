import sympy as sp
import math

x = sp.symbols('x')
y = sp.sin(10 * math.pi /x)
P = (1, 0)

def computeSlope(x0):
    Q = (x0, y.subs(x, x0))
    slope = (Q[1] - P[1]) / (Q[0] - P[0])
    return slope

xs = [2, 1.5, 1.4, 1.3, 1.2, 1.1, 0.5, 0.6, 0.7, 0.8, 0.9]
for x0 in xs:
    slope = computeSlope(x0)
    print(slope)
