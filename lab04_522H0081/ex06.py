import sympy as sp
import math
x = sp.symbols('x')


print('câu 6a')
fa = (x*x -x -6) / (x - 3)
faLeft = sp.limit(fa, x, 0, '-')
print ("Left limit = " , faLeft )
faRight = sp.limit(fa, x, 0, '+')
print ("Right limit = " , faRight )
a = 5
if (faLeft == faRight == a):
    lma = faLeft
else:
    lma = None
print(lma)


print('câu 6b')
fb = (x**3 - 8) / (x**2 - 4)
fbLeft = sp.limit(fb, x, -2)
print ("Left limit = " , fbLeft )
fbRight = sp.limit(fb, x, 2)
print ("Right limit = " , fbRight )
b1 = 3
b2 = 4
if (fbLeft == fbRight == b1 == b2):
    lmb = fbLeft
else:
    lmb = None
print(lmb)

print('câu 6c')
fc = (x*x -x -2) / (x-2)
fcLeft = sp.limit(fc, x, 2, '-')
print ("Left limit = " , fcLeft )
fcRight = sp.limit(fc, x, 2, '+')
print ("Right limit = " , fcRight )
c = 1
if (fcLeft == fcRight == c):
    lmc = fcLeft
else:
    lmc = None
print(lmc)


print('câu 6d')
fd = 1/(x*x)
fdLeft = sp.limit(fc, x, 0, '-')
print ("Left limit = " , fdLeft )
fdRight = sp.limit(fc, x, 0, '+')
print ("Right limit = " , fdRight )
d = 1
if (fdLeft == fdRight == d):
    lmd = fdLeft
else:
    lmd = None
print(lmd)