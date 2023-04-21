import sympy as sp
import math

x = sp.symbols('x')

def golden_search(f, a, b, epsilon):
    d = b - a
    while b - a >= epsilon:
        d = 0.618*d
        x1 = b - d
        x2 = a + d 
        if f.subs(x, x1) <= f.subs(x, x2):
            b = x2
        else:
            a = x1
        print('.',(a+b)/2)

    return (a + b)/2


epsilon = 0.3
a, b = -2, 1
f = x**2
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))
