import sympy as sp
import math

x = sp.symbols('x')

print("Câu a")
y = sp.exp(-x**2)
a, b = 0, 1
trapezoidal_rule = (b - a) * (1/2)*(y.subs(x, a) + y.subs(x, b))
print('%.4f'%(trapezoidal_rule.evalf()))

print("Câu b")
y = 2*x**2 + 5*x + 12 
a, b = -1, 5
trapezoidal_rule = (b - a) * (1/2)*(y.subs(x, a) + y.subs(x, b))
print('%.4f'%(trapezoidal_rule.evalf()))

print("Câu c")
y = x**3 + 2*x**2 - 5*x - 2
a, b = 0, 2
trapezoidal_rule = (b - a) * (1/2)*(y.subs(x, a) + y.subs(x, b))
print('%.4f'%(trapezoidal_rule.evalf()))

print("Câu d")
y = x*sp.exp(-x)
a, b= 0.2, 3.8
trapezoidal_rule = (b - a) * (1/2)*(y.subs(x, a) + y.subs(x, b))
print('%.4f'%(trapezoidal_rule.evalf()))