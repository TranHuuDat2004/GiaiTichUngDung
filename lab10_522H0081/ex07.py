import sympy as sp
import math

t = sp.symbols('t')

H = sp.sqrt(t+1) + 5*t**(1/3)

print('t = 0, H =', '%.4f'%(H.subs(t, 0)))
print('t = 4, H =', '%.4f'%(H.subs(t, 4)))
print('t = 8, H =', '%.4f'%(H.subs(t, 8)))

a, b = 0, 8
average = (1 / (b-a)) * sp.integrate(H, (t, a, b))
print("average height = ", '%.4f'%(average))