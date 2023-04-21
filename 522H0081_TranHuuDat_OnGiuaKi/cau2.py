import matplotlib.pyplot as plt
import numpy as np
import math

# câu a
f = lambda x: x**2
g = lambda x: x**3

# câu b
fb = f(g(1234)) + g(f(1234)) + g(g(1234))
print('cau b:', fb)

# câu c
xc = np.arange(-100, 100+0.1, 0.1)
yc = list( map(f, xc) )

plt.plot(xc, yc, color = 'red')
plt.title('câu 2c')
plt.grid()
plt.show()

# câu d
xd = np.arange(-5, 5+0.1, 0.1)
yd = list( map(g, xd) )

plt.plot(xd, yd, color = 'blue')
plt.title('câu 2d')
plt.grid()
plt.show()