import sympy as sp
import math

x, y, z, t =sp.symbols('x, y, z, t')


print('Câu a')
x = sp.cos(t)
y = sp.sin(t)
w = x**2 + y**2

print('x = ',x)
print('y = ',y)
print('w = ',w)
print('w(t) = ', w.subs(t, sp.pi))  # thế t vào hàm w


print('\nCâu b')
x = sp.cos(t) + sp.sin(t)
y = sp.cos(t) - sp.sin(t) 
w = x**2 + y**2

print('x = ',x)
print('y = ',y)
print('w = ',w)
print('w(t) = ', w.subs(t, 0))


print('\nCâu c')
x = sp.cos(t)*sp.cos(t)
y = sp.sin(t)*sp.sin(t)
z = 1/t
w = (x/z) + (y/z)

print('x = ',x)
print('y = ',y)
print('z = ',z)
print('w = ',w)
print('w(t) = ', w.subs(t, 3))


print('\nCâu d')
x = sp.log(t**2 + 1)
y = sp.atan(t)
z = sp.exp(t)
w = 2*y*sp.exp(x) - sp.log(z)

print('x = ',x)
print('y = ',y)
print('z = ',z)
print('w = ',w)
print('w(t) = ', w.subs(t, 1))


print('\nCâu e')
x = t
y = sp.log(t)
z = sp.exp(t-1)
w = z - sp.sin(x*y)

print('x = ',x)
print('y = ',y)
print('z = ',z)
print('w = ',w)
print('w(t) = ', w.subs(t, 1))