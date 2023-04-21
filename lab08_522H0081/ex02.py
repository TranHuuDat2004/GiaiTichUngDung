import sympy as sp
from sympy.plotting import plot3d
import math

x,y = sp.symbols('x y')

print('Câu a')
fa =  sp.cos(x) * sp.cos(y) * sp.exp(-sp.sqrt(x*x +y*y)/4)
plot3d(fa)  # vẽ đồ thị 3d

print('Câu b')
fb = -(x*y*y) / (x*x+y*y)
plot3d(fb)

print('Câu c')
fc = (x*y*(x*x-y*y))/(x*x+y*y)
plot3d(fc)

print('Câu d')
fd = y**2 - y**4 - x**2
plot3d(fd)