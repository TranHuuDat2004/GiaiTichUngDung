import sympy as sp
import math

x, y =sp.symbols('x, y')

print('\nCâu a')
f = y**2 * x**4 * sp.exp(x) + 2
f_d3y = f.diff(y, 3)
print('f_d3y = ', f_d3y)   
# ∂3f / ∂3y, đạo hàm biến y cấp 3

f_d3y_d2x = f_d3y.diff(x, 2)
print('f_d3y_d2x = ',f_d3y_d2x)
#∂5f / (∂2x ∂3y), đạo hàm biến y cấp 3 trước, đạo hàm biến x cấp 2 sau    

print('\nCâu b')
f =y**4 + y*(sp.sin(x) - x**4)
f_d3y = f.diff(y, 3)
print('f_d3y = ', f_d3y)
f_d3y_d2x = f_d3y.diff(x, 2)
print('f_d3y_d2x = ',f_d3y_d2x)


print('\nCâu c')
f = x**5 + 5*x*y + sp.sin(x) + 7*sp.exp(x)
f_d3y = f.diff(y, 3)
print('f_d3y = ', f_d3y)
f_d3y_d2x = f_d3y.diff(x, 2)
print('f_d3y_d2x = ',f_d3y_d2x)


print('\nCâu d')
f = x * sp.exp(y**4 / 2)
f_d3y = f.diff(y, 3)
print('f_d3y = ', f_d3y)
f_d3y_d2x = f_d3y.diff(x, 2)
print('f_d3y_d2x = ',f_d3y_d2x)