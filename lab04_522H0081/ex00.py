import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20, 20, 0.1)
f1 = lambda x: -x + 5
f2 = lambda x: x/2 + 2

y1 = list(map(f1, x))
y2 = list(map(f2, x))

plt.plot(x, y1)
plt.plot(x, y2)

x = sp.symbols('x')
sf1 = -x + 5
sf2 = x/2 + 2

xi = sp.solve(sf1 - sf2)[0] # sf1 - sf2 = 0
yi = sf1.subs(x, xi)

plt.plot([xi], [yi], 'ro')
plt.title('Giao điểm của f1(x) = -x + 5 và f2(x) = x/2 + 2')
plt.show()