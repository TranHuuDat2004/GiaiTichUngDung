import sympy as sp
import math


x = sp.symbols('x')

print('\nCâu a')
fa = 3*x**4 - 16*x**3 + 18*x**2 -9
print('f = ',fa)
dfa = fa.diff()
print("f' =", dfa)
lx = sp.solve(dfa)
print('Các điểm tới hạn là:',lx)
for x0 in lx: # thế từng giá trị x vào f, ra mỗi giá trị y
    print('(%.2f, %.2f)'%(x0, fa.subs(x, x0).evalf()))
sp.plotting.plot(fa)


print('\nCâu b')
fb = (x + 2) / (2*x**2)
print('f = ',fb)
dfb = fb.diff()
print("f' =", dfb)
lx = sp.solve(dfb)
print('Các điểm tới hạn là:',lx)
for x0 in lx: # thế từng x vào, ra các điểm y
    print('(%.2f, %.2f)'%(x0, fb.subs(x, x0).evalf()))
sp.plotting.plot(fb)


print('\nCâu c')
fc = -(x**2/3) + x**2 + 3*x +4
print('f = ',fc)
dfc = fc.diff()
print("f' =", dfc)
lx = sp.solve(dfc)
print('Các điểm tới hạn là:',lx)
for x0 in lx: # thế từng x vào, ra các điểm y
    print('(%.2f, %.2f)'%(x0, fc.subs(x, x0).evalf()))
sp.plotting.plot(fc)


print('\nCâu d')
fd = (5*x**2 + 5)/ x
print('f = ',fd)
dfd = fd.diff()
print("f' =", dfd)
lx = sp.solve(dfd)
print('Các điểm tới hạn là:',lx)
for x0 in lx: # thế từng x vào, ra các điểm y
    print('(%.2f, %.2f)'%(x0, fd.subs(x, x0).evalf()))
sp.plotting.plot(fd)