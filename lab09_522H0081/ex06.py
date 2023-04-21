import sympy as sp
import math

x = sp.symbols('x')

def fibonacci_search (f, a, b, epsilon):
    F = lambda n:n    
    n = 2
    while b - a >= epsilon:
        d = b - a
        x1 = b - d * (F(n-1) / F(n))
        x2 = a + d * (F(n-1) / F(n))
        if f.subs(x, x1) <= f.subs(x, x2):
            b = x2
        else:
            a = x1

        n = n + 1
        
    return (a + b)/2



epsilon = 0.3
a, b = -2, 1
f = x**2
x0 = fibonacci_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))
