import sympy as sp
import math

x, y, dx=sp.symbols('x, y, dx')

print('Câu a')
f = 1 - x + y - 3*(x**2)*y
num = f.subs([(x, 1+dx), (y, 2)], simultaneous=True) \
    - f.subs([(x, 1), (y, 2)], simultaneous=True)  # đạo hàm bằng định nghĩa
denom = dx
print(sp.limit(num/denom, dx, 0))  # tử / mẫu


print('Câu b')
f = 4 + 2*x - 3*y
num = f.subs([(x, 1+dx), (y, 2)], simultaneous=True) \
    - f.subs([(x, 1), (y, 2)], simultaneous=True)  # đạo hàm bằng định nghĩa
denom = dx
print(sp.limit(num/denom, dx, 0))  # tử / mẫu
