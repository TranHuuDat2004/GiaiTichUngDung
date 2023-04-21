import sympy as sp
from sympy.plotting import plot
import math
x = sp.symbols('x')

def draw(fx, y):
    g1 = plot(fx, show=False)
    g2 = plot(y, show=False)
    g1.append(g2[0])
    g1.show()


print('câu 2a')
fa = x*x + 1
P = (2, 5)
dfa = fa.diff()
print('đạo hàm là:', dfa)
sa = dfa.subs(x, 2)
print('thế x = 2 vào', sa)
ya = sa*(x-P[0])  - P[1] 
print(ya)
print(ya)
draw(fa, ya)  # hàm def draw(fx, y), fa = fx, ya = y

print('\n câu 2b')
fb = x -2*(x**2)
P = (1, 1)
dfb = fb.diff()
print('đạo hàm là:', dfb)
sb = dfb.subs(x, 1)
print('thế x = 1 vào', sb)
yb = sb*(x-P[0])  - P[1] 
print(yb)
print(yb)
draw(fb, yb)


print('\n câu 2c')
fc = x / (x-2)
P = (3, 3)
dfc = fc.diff()
print('đạo hàm là:', dfc)
sc = dfc.subs(x, 3)
print('thế x = 3 vào', sc)
yc = sc*(x-P[0])  - P[1] 
print(yc)
draw(fc, yc)

print('\n câu 2d')
fd = 8 / (x*x)
P = (2, 2)
dfd = fd.diff()
print('đạo hàm là:', dfd)
sd = dfd.subs(x, 2)
print('thế x = 2 vào', sd)
yd = sd*(x-P[0])  - P[1] 
print(yd)
draw(fd, yd)

print('\n câu 2e')
fe = sp.sqrt(x)
P = (4, 2)
dfe = fe.diff()
print('đạo hàm là:', dfe)
se = dfe.subs(x, 4)
print('thế x = 4 vào', se)
ye = se*(x-P[0])  - P[1] 
print(ye)
draw(fe, ye)

print('\n câu 2f')
ff = x**3 + 3*x
P = (1, 4)
dff = ff.diff()
print('đạo hàm là:', dff)
sf = dff.subs(x, 1)
print('thế x = 1 vào', sf)
yf = sf*(x-P[0])  - P[1] 
print(yf)
draw(ff, yf)

print('\n câu 2g ')
fg = 8 / (sp.sqrt(x - 2))
P = (6, 4)
dfg = fg.diff()
print('đạo hàm là:', dfg)
sg = dfg.subs(x, 6)
print('thế x = 6 vào', sg)
yg = sg*(x-P[0])  - P[1] 
print(yg)
draw(fg, yg)

print('\n câu 2h')
fh = 1 + sp.sqrt(4-x)
P = (3, 2)
dfh = fh.diff()
print('đạo hàm là:', dfh)
sh = dfh.subs(x, 3)
print('thế x = 3 vào', sh)
yh = sh*(x-P[0])  - P[1] 
print(yh)
draw(fh, yh)   # hàm def draw(fx, y), fh = fx, yh = y
