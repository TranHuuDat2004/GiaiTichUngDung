import sympy as sp
import math
x = sp.symbols('x')

print(' câu 3a')
fa = 5*x - 3*(x**2)
x0 = 1
dfa = fa.diff()
s = dfa.subs(x, x0)
y = s*(x-x0) + fa.subs(x,x0) #
print('đạo hàm là:',dfa)
print('Thế x=1 vào đạo hàm',s)
print('Phương trình tiếp tuyến là:',y)

print('\n câu 3b')
fb = 1 / (x-1)
x0 = 3
dfb = fb.diff()
s = dfb.subs(x, x0)
y = s*(x-x0) + fb.subs(x,x0)
print('đạo hàm là:',dfb)
print('Phương trình tiếp tuyến là:',y)

print('\n câu 3c')
fc = x**3 - 2*x +7
x0 = -2
dfc = fc.diff()
s = dfc.subs(x, x0)
y = s*(x-x0) + fc.subs(x,x0)
print('đạo hàm là:',dfc)
print('Phương trình tiếp tuyến là:',y)

print('\n câu 3d')
fd = (x-1) / (x+1)
x0 = 0
dfd = fd.diff()
s = dfd.subs(x, x0)
y = s*(x-x0) + fd.subs(x,x0)
print('đạo hàm là:',dfd)
print('Phương trình tiếp tuyến là:',y)



