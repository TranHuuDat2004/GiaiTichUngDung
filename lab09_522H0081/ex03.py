import sympy as sp
import math

x = sp.symbols('x')

print('\nCâu a')
f = x**3 -27*x
R = [0, 5]
print('f = ',f)
print('R = ',R)
df = f.diff()
print("f' = ", df)
lx = sp.solve(df)
print('x = ',lx)    # các giá trị x sau khi đạo hàm = 0, tìm x 
lx = [x0 for x0 in lx if R[0] <= x0 and x0 <= R[1]] + [R[0], R[1]]  # thêm các giá trị x của đề 
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
print('max = ', max(ly))
print('min = ', min(ly))
sp.plotting.plot(f, (x, R[0], R[1]))


print('\nCâu b')
f = (3/2)*x**4 - 4*x**3 + 4
R = [0, 3]
print('f = ',f)
print('R = ',R)
df = f.diff()
print("f' = ", df)
lx = sp.solve(df)
print('x = ',lx)    # các giá trị x sau khi đạo hàm = 0, tìm x 
lx = [x0 for x0 in lx if R[0] <= x0 and x0 <= R[1]] + [R[0], R[1]]  # thêm các giá trị x của đề 
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
print('max = ', max(ly))
print('min = ', min(ly))
sp.plotting.plot(f, (x, R[0], R[1]))


print('\nCâu c')
f = (1/2)*x**4 - 4*x**2 + 5
R = [1, 3]
print('f = ',f)
print('R = ',R)
df = f.diff()
print("f' = ", df)
lx = sp.solve(df)
print('x = ',lx)    # các giá trị x sau khi đạo hàm = 0, tìm x 
lx = [x0 for x0 in lx if R[0] <= x0 and x0 <= R[1]] + [R[0], R[1]]  # thêm các giá trị x của đề 
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
print('max = ', max(ly))
print('min = ', min(ly))
sp.plotting.plot(f, (x, R[0], R[1]))


print('\nCâu d')
f = (5/2)*x**4 - (20/3)*x**3 + 6
R = [-1, 3]
print('f = ',f)
print('R = ',R)
df = f.diff()
print("f' = ", df)
lx = sp.solve(df)
print('x = ',lx)    # các giá trị x sau khi đạo hàm = 0, tìm x 
lx = [x0 for x0 in lx if R[0] <= x0 and x0 <= R[1]] + [R[0], R[1]]  # thêm các giá trị x của đề 
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
print('max = ', max(ly))
print('min = ', min(ly))
sp.plotting.plot(f, (x, R[0], R[1]))


