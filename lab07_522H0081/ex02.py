import sympy as sp
import math
n = sp.symbols('n')

print('Câu a')
a = 5
d = 20 - 5
an = a + (n - 1)*d
print('d =',d)
a55 = a + (55-1)*d
print('a55 =',a55)
print(sp.solve(an-230))


print('\nCâu b')
a = 120
r = 60/120
an = a*(r)**(n-1)
print('r =',r)
a10 = a * (r)**(10-1)
print('a10 =',a10)
print(sp.solve ( an-(15/32) ) )
