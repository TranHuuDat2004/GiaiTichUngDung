import sympy as sp
import math

x = sp.symbols('x')

print('\nCâu a')
f = 3*x**4 - 16*x**3 + 18*x**2 -9
print('f = ',f)
df = f.diff()
print("f' =", df)
lx = sp.solve(df)
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
d2f = f.diff(x, 2) # đao hàm cấp 2
print("f'' =", d2f)
kinds = ['max' if d2f.subs(x, x0).evalf() < 0 else 'min' for x0 in lx]   # if d2f.subs(x, x0).evaif() < 0: print('max'), else: print('min')
print(kinds)                                                                       
sp.plotting.plot(f)


print('\nCâu b')
f = (x + 2) / (2*x**2)
print('f = ',f)
df = f.diff()
print("f' =", df)
lx = sp.solve(df)
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
d2f = f.diff(x, 2) # đao hàm cấp 2
print("f'' =", d2f)
kinds = ['max' if d2f.subs(x, x0).evalf() < 0 else 'min' for x0 in lx]   
print(kinds)                                                                       
sp.plotting.plot(f)


print('\nCâu c')
f = -(x**2/3) + x**2 + 3*x +4
print('f = ',f)
df = f.diff()
print("f' =", df)
lx = sp.solve(df)
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
d2f = f.diff(x, 2) # đao hàm cấp 2
print("f'' =", d2f)
kinds = ['max' if d2f.subs(x, x0).evalf() < 0 else 'min' for x0 in lx]   
print(kinds)                                                                       
sp.plotting.plot(f)


print('\nCâu d')
f = (5*x**2 + 5)/ x
print('f = ',f)
df = f.diff()
print("f' =", df)
lx = sp.solve(df)
print('x = ',lx)
ly = [f.subs(x, x0) for x0 in lx]
print('y = ',ly)
d2f = f.diff(x, 2) # đao hàm cấp 2
print("f'' =", d2f)
kinds = ['max' if d2f.subs(x, x0).evalf() < 0 else 'min' for x0 in lx]   
print(kinds)                                                                       
sp.plotting.plot(f)
