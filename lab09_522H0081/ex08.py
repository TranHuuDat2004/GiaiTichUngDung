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


print('\nCâu a')
epsilon = 1/9
a, b = -5, 5
f = -2*x**2 +x +4
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))


print('\nCâu b')
epsilon = 1/10
a, b = -6, 6
f = -4*x**2 + 2*x + 2
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))


print('\nCâu c')
epsilon = 1/10
a, b = -5, -2
f = x**3 + 6*x**2 + 5*x -12
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))


print('\nCâu d')
epsilon = 1/100
a, b = 0, 3
f = 2*x - x*x
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))


print('\nCâu e')
epsilon = 1/5
a, b = -10, 10
f = x*x - x - 10
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))


print('\nCâu f')
epsilon = 1/8
a, b = -10, 10
f = -(x+6)**2 + 4
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))


print('\nCâu g')
epsilon = 1/8
a, b = -3, 5
f = -2*x**2 + 3*x + 6
x0 = golden_search(f, a, b, epsilon)
print('f(x0) = ',f.subs(x, x0))
sp.plot(f, (x, a, b))