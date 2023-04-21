import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt
import math
x = sp.symbols('x')
h = sp.symbols('h')

def getlimit(fx , x0):
    dx = sp.symbols('dx')
    g = (fx.subs(x, x0+dx) - fx.subs(x, x0)) / dx
    return (sp.limit(g, dx, 0))


print('câu 7a')
fa = x**3 + 2*x 
x0a = 0
xa = np.linspace(x0a - 1/2, x0a + 3)
ya = [fa.subs(x, it) for it in xa]
plt.plot(xa, ya)



q = (fa.subs(x, x0a+ h) - fa.subs(x, x0a)) /h
print(q)
print(sp.limit(q, h, 0))

def drawTangent(h0):
    y = fa.subs(x, x0a) + q.subs(h, h0) * (x - x0a)
    ytsa = [y.subs(x, it) for it in xa]
    plt.plot(xa, ytsa)
for h0 in [3, 2, 1]:
    drawTangent(h0)
plt.grid()
plt.show()



print('câu 7b')
fb = x + 5/x
x0b = 1
xb = np.linspace(x0b - 1/2, x0b + 3)
yb = [fb.subs(x, it) for it in xb]
plt.plot(xb, yb)


q = (fb.subs(x, x0b + h) - fb.subs(x, x0b)) /h
print(q)
print(sp.limit(q, h, 0))

def drawTangent(h0):
    y = fb.subs(x, x0b) + q.subs(h, h0) * (x - x0b)
    ytsb = [y.subs(x, it) for it in xb]
    plt.plot(xb, ytsb)
for h0 in [3, 2, 1]:
    drawTangent(h0)
plt.grid()
plt.show()



print('câu 7c')
fc = x + sp.sin(2*x)
x0c = math.pi/2
xc = np.linspace(x0c - 1/2, x0c + 3)
yc = [fc.subs(x, it) for it in xc]
plt.plot(xc, yc)


q = (fc.subs(x, x0c + h) - fc.subs(x, x0c)) /h
print(q)
print(sp.limit(q, h, 0))

def drawTangent(h0):
    y = fc.subs(x, x0c) + q.subs(h, h0) * (x - x0c)
    ytsc = [y.subs(x, it) for it in xc]
    plt.plot(xc, ytsc)
for h0 in [3, 2, 1]:
    drawTangent(h0)
plt.grid()
plt.show()



print('câu 7d')
fd = sp.cos(x) + 4*sp.sin(2*x)
x0d = math.pi
xd = np.linspace(x0d - 1/2, x0d + 3)
yd = [fd.subs(x, it) for it in xd]
plt.plot(xd, yd)


q = (fd.subs(x, x0d + h) - fd.subs(x, x0d)) /h
print(q)
print(sp.limit(q, h, 0))

def drawTangent(h0):
    y = fd.subs(x, x0d) + q.subs(h, h0) * (x - x0d)
    ytsd = [y.subs(x, it) for it in xd]
    plt.plot(xd, ytsd)
for h0 in [3, 2, 1]:
    drawTangent(h0)
plt.grid()
plt.show()