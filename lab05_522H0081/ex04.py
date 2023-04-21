import sympy as sp
import math

x = sp.symbols('x')
dx = sp.symbols('dx') #denta_x

y = (-2* x**2) / 3 + x
x0 = 0
fx = (y.subs(x, x0+dx) - y.subs(x, x0)) / dx 
print('công thức đạo hàm bằng định nghĩa:',fx)
print('Kết quả đạo hàm =',sp.limit(fx, dx, 0))


