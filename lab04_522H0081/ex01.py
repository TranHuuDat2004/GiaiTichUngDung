import sympy as sp
import math
x = sp.symbols('x')


fa = abs(x**2 -x -7)
lm1a = sp.limit(fa, x, 3)
print("1a - Giới hạn f(x) tại x = 3 là " + str(lm1a) )


fb = ( abs(x - 1) / (x**2 -1 ) )
lm1b = sp.limit(fb, x, 1)
print("1b - Giới hạn f(x) tại x = 1 là " + str(lm1b) )


fc = sp.exp(1/x)
lm1c = sp.limit(fc, x, 1)
print("1c - Giới hạn f(x) tại x = 1 là " + str(lm1c) )


fd = (x**4 -16) / (x-2)
lm1d = sp.limit(fd, x, 2)
print("1d - Giới hạn f(x) tại x = 2 là " + str(lm1d) )


fe = ((x**3 - x**2 - 5*x -3) / (x + 1)**2)
lm1e = sp.limit(fe, x, -1)
print("1e - Giới hạn f(x) tại x = -1 là " + str(lm1e) )


ff = (x*x -9) / ((x*x + 7)**(1/2) -4)
lm1f = sp.limit(ff, x, 3)
print("1f - Giới hạn f(x) tại x = 3 là " + str(lm1f) )


fg = abs(x) / sp.sin(x)
lm1g = sp.limit(fg, x, 1)
print("1g - Giới hạn f(x) tại x = 1 là " + str(lm1g) )


fh = (1 - sp.cos(x)) / x*sp.sin(x)
lm1h = sp.limit(fh, x, 0)
print("1h - Giới hạn f(x) tại x = 0 là " + str(lm1h) )

fi = 2*x*x / (3 - 3*sp.cos(x))
lm1i = sp.limit(fi, x, 0)
print("1i - Giới hạn f(x) tại x = 0 là " + str(lm1i) )


fj = ((3 + x) / (-1 + x))**x
lm1j = sp.limit(fj, x, +sp.oo)
print("1j - Giới hạn f(x) tại x = oo là " + str(lm1j) )


fk = ( 1 - (2 / (3 + x)) )**x
lm1k = sp.limit(fk, x, +sp.oo)
print("1k - Giới hạn f(x) tại x = oo là " + str(lm1k) )


fl = (1/x)**(1/x)
lm1l = sp.limit(fl, x, +sp.oo)
print("1l - Giới hạn f(x) tại x = oo là " + str(lm1l) )

fm = ( (-x**(1/3) + (1+x)**(1/3)) / (-x**(1/2) + (1 + x)**(1/2) ) )
lm1m = sp.limit(fm, x, +sp.oo)
print("1m - Giới hạn f(x) tại x = +oo là " + str(lm1m) )


fn =  sp.factorial(x) / x**x
lm1n = sp.limit(fn, x, +sp.oo)
print("1n - Giới hạn f(x) tại x = +oo là " + str(lm1n) )


