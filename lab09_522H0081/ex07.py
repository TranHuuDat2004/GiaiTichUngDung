import sympy as sp
import math

x = sp.symbols('x')
m = sp.symbols('m')

f = x**3 - 3*m*x**2 + 3*(m**2 -1)*x -(m**2 -1)
x0 = 1
print('f = ',f)
df = f.diff(x, 1)
print("f' = ",df)
d2f = f.diff(x, 2)
print("f'' = ",d2f)

df_x0 = df.subs(x, x0)
print("f'(x0) = ", df_x0)
d2f_x0 = d2f.subs(x, x0)
print("f''(x0) = ", d2f_x0)

ms = sp.solve(df_x0)
print('m = ',ms)
list_d2f_x0 = [d2f_x0.subs(m, it).evalf() for it in ms]
print('list_d2f_x0 = ',list_d2f_x0)
result = [it for it in ms if d2f_x0.subs(m, it).evalf() < 0]
print('result = ',result)
