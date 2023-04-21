import sympy as sp
from sympy.plotting import plot3d
import math

x,y = sp.symbols('x, y')


print('Câu a')
f = 2*x*x - 3*y -4
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu b')
f = 2*x*x - 3*y -4
dx = f.diff(x)
print(dx)
dy = f.diff(y)
print(dy)

plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))

print('Câu c')
f = x**2 -x*y + y**2
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu d')
f = 5*x*y - 7*x**2 - y**2 + 3*x -6*y +2
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu e')
f = (x*y -1)**2
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu f')
f = (2*x -3*y)**3
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu g')
f = sp.sqrt(x**2 + y**2)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu h')
f = (x**3 + (y/2)) ** (2/3)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu i')
f = 1 / (x + y)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, -1, 1), (y, -1, 1)))


print('Câu j')
f = x / (x**2 + y**2)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu k')
f = (x + y)/(x*y -1)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu l')
f = sp.atan(y/x)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu m')
f = sp.exp(x + y + 1)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu n')
f = sp.exp(-x) * sp.sin(x + y)
dx = f.diff(x)
print(dx)
dy = f.diff(y)

print(dy)
plot3d(f,
       dx,
       (dy, (x, 1, 5), (y, 1, 5)))


print('Câu o')
f = sp.log(x + y)
dx = f.diff(x)
print(dx)
dy = f.diff(y)
print(dy)
plot3d((f, (x, 1, 5), (y, 1, 5)),
       (dx, (x, 1, 5), (y, 1, 5)),
       (dy, (x, 1, 5), (y, 1, 5)))