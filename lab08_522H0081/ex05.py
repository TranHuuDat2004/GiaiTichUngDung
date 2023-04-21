import sympy as sp
import math

x, y =sp.symbols('x, y')

print('\nCâu a')
fxy = x*sp.sin(y) + y*sp.sin(x) + x*y
fyx = fxy.subs( [ (x, y),(y, x) ], simultaneous=True ) # thế đồng thời (simultaneous) x vào y, thế y vào x
s = fxy - fyx
print('fxy = ',fxy)
print('fyx = ',fyx)
print('s = ',s)
print(s.evalf() == 0)  #hàm sp.eval và chữ


print('\nCâu b')
fxy = sp.log(2*x + 3*y)
fyx = fxy.subs( [ (x, y),(y, x) ], simultaneous=True ) # thế đồng thời (simultaneous) x vào y, thế y vào x
s = fxy - fyx
print('fxy = ',fxy)
print('fyx = ',fyx)
print('s = ',s)
print(s.evalf() == 0)


print('\nCâu c')
fxy = x*y**2 + x**2*y**3 + x**3*y**4 
fyx = fxy.subs( [ (x, y),(y, x) ], simultaneous=True ) # thế đồng thời (simultaneous) x vào y, thế y vào x
s = fxy - fyx
print('fxy = ',fxy)
print('fyx = ',fyx)
print('s = ',s)
print(s.evalf() == 0)

print('\nCâu d')
fxy = sp.exp(x) + x*sp.log(y) + y*sp.log(x)
fyx = fxy.subs( [ (x, y),(y, x) ], simultaneous=True ) # thế đồng thời (simultaneous) x vào y, thế y vào x
s = fxy - fyx
print('fxy = ',fxy)
print('fyx = ',fyx)
print('s = ',s)
print(s.evalf() == 0)