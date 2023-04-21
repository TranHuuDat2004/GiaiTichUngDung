import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)


# a
f = lambda x, y: x + y + x*y
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu a')
plt.show()


# b
f = lambda x, y: np.sin(x*y)
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu b')
plt.show()


# c
f = lambda x, y: x**2*y + np.cos(y) + y*np.sin(x)
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu c')
plt.show()


# d
f = lambda x, y: x*np.exp(y) + y + 1
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu d')
plt.show()


#  e
f = lambda x, y: np.log(x + y)
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu e')
plt.show()


# f 
f = lambda x, y: np.arctan(y/x) 
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu f')
plt.show()


# g
f = lambda x, y: x**2 * np.tan(x*y)
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu g')
plt.show()


# h
f = lambda x, y: y * np.exp(x**2 -y)
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu h')
plt.show()


# i
f = lambda x, y: x*np.sin(x**2*y)
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu i')
plt.show()


# j
f = lambda x, y: (x-y)/(x**2 +y)
Z = f(X, Y)

ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z,)
plt.title('Câu j')
plt.show()







