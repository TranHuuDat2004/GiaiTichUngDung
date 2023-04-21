import sympy as sp
from sympy.plotting import plot3d

x, y = sp.symbols('x y')

f = x**2 - x*y + (1/2)*y**2 + 3

A =[3, 2]
dfx = f.diff(x)
dfy = f.diff(y)

slope_x = dfx.subs([(x, A[0]), (y, A[1])], simultaneous=True)
print('slope_x = ',slope_x)
slope_y = dfy.subs([(x, A[0]), (y, A[1])], simultaneous=True)
print('slope_y = ','%.4f'%(slope_y))
y_tangent = slope_x*(x-A[0]) + slope_y*(y-A[1])
print('y_tangent = ',y_tangent)
plot3d(f, (y_tangent, (x, -10, 10), (y, -10, 10)))