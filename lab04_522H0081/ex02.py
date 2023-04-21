import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import math
x = sp.symbols('x')


#câu a
fa = abs(x**2 -x -7)
lm2a = sp.limit(fa, x, 3)

xa = np.arange(-3, 3.1, 0.1)  # xa nằm trong khoảng [-3, 3]
ya = [fa.subs(x, ia) for ia in xa] # thế từng xa vào ya

plt.plot(xa, ya)
plt.plot([lm2a])
plt.title("câu 2a")
plt.grid() 
plt.show()


#câu b
fb = ( abs(x - 1) / (x**2 -1 ) )
lm2b = sp.limit(fb, x, 0)

xb = np.arange(-3, 3.1, 0.1)
yb = [fb.subs(x, ib) for ib in xb]

plt.plot(xb, yb)
plt.plot([lm2b])
plt.title("câu 2b")
plt.grid()
plt.show()


#câu c
fc = sp.exp(1/x)
lm2c = sp.limit(fc, x, 1)

xc = np.arange(-1, 1.1, 0.1)
yc = [fc.subs(x, ic) for ic in xc]

plt.plot(xc, yc)
plt.plot([lm2c])
plt.title("câu 2c")
plt.grid()
plt.show()


#câu d
fd = (x**4 -16) / (x-2)
lm2d = sp.limit(fd, x, 2)

xd = np.arange(-2, 2.1, 0.1)
yd = [fd.subs(x, id) for id in xd]

plt.plot(xd, yd)
plt.plot([lm2d])
plt.title("câu 2d")
plt.grid()
plt.show()


#câu e
fe = (x**3 - x**2 - 5*x -3) / ((x + 1)**2)
lm2e = sp.limit(fe, x, -1)

xe = np.arange(-3, 3.1, 0.1)
ye = [fe.subs(x, ie) for ie in xe]

plt.plot(xe, ye)
plt.plot([lm2e])
plt.title("câu 2e")
plt.grid()
plt.show()


#câu f
ff = (x*x -9) / ((x*x + 7)**(1/2) -4)
lm2f = sp.limit(ff, x, 3)

xf = np.arange(-3, 3.1, 0.1)
yf = [ff.subs(x, iff) for iff in xf]

plt.plot(xf, yf)
plt.plot([lm2f])
plt.title("câu 2f")
plt.grid()
plt.show()


#câu g
fg = abs(x) / sp.sin(x)
lm2g = sp.limit(fg, x, 1)

xg = np.arange(-3, 3.1, 0.1)
yg = [fg.subs(x, ig) for ig in xg]

plt.plot(xg, yg)
plt.plot([lm2g])
plt.title("câu 2g")
plt.grid()
plt.show()


#câu h
fh = ( (1 - sp.cos(x)) / x*sp.sin(x) )
lm2h = sp.limit(fh, x, 0)

xh = np.arange(-1, 1.1, 0.1)
yh = [fh.subs(x, ih) for ih in xh]

plt.plot(xh, yh)
plt.plot([lm2h])
plt.title("câu 2h")
plt.grid()
plt.show()


#câu i
fi = (2*x**2) / (3 - 3*sp.cos(x))
lm2i = sp.limit(fi, x, 0)

xi = np.arange(-1, 1.1, 0.1)
yi = [fi.subs(x, ii) for ii in xi]

plt.plot(xi, yi)
plt.plot([lm2i])
plt.title("câu 2i")
plt.grid()
plt.show()


#câu j 
fj = ((3 + x) / (-1 + x))**x
lm2j = sp.limit(fj, x, +sp.oo)

xj = np.arange(-3, 3.1, 0.1)
yj = [fj.subs(x, ij) for ij in xj]

plt.plot(xj, yj)
plt.plot([lm2j])
plt.title("câu 2j")
plt.grid()
plt.show()


#câu k
fk = ( 1 - (2 / (3 + x)) )**x
lm2k = sp.limit(fk, x, +sp.oo)

xk = np.arange(-3, 3.1, 0.1)
yk = [fk.subs(x, ik) for ik in xk]

plt.plot(xk, yk)
plt.plot([lm2k])
plt.title("câu 2k")
plt.grid()
plt.show()


fl = (1/x)**(1/x)
lm2l = sp.limit(fl, x, +sp.oo)

xl = np.arange(-3, 3.1, 0.1)
yl = [fl.subs(x, il) for il in xl]

plt.plot(xl, yl)
plt.plot([lm2l])
plt.title("câu 2l")
plt.grid()
plt.show()

fm = ( (-x**(1/3) + (1+x)**(1/3)) / (-x**(1/2) + (1 + x)**(1/2) ) )
lm2m = sp.limit(fm, x, +sp.oo)

xm = np.arange(-3, 3.1, 0.1)
ym = [fm.subs(x, im) for im in xm]

plt.plot(xm, ym)
plt.plot([lm2m])
plt.title("câu 2m")
plt.grid()
plt.show()


fn =  sp.factorial(x) / x**x
lm2n = sp.limit(fn, x, +sp.oo)

xn = np.arange(-3, 3.1, 0.1)
yn = [fn.subs(x, inn) for inn in xn]

plt.plot(xn, yn)
plt.plot([lm2n])
plt.title("câu 2n")
plt.grid()
plt.show()



