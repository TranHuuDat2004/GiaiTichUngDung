import sympy as sp
import math

n = sp.symbols('n')

print('Câu a')
an = 1 - (0.2)**n
a = sp.limit_seq(an)  #sp.limit_seq(an) = sp.limit(an, n, sp.oo)
print(a)

print('Câu b')
an = n**3 / (n**3 + 1)
b = sp.limit_seq(an)
print(b)

print('Câu c')
an = (3 + 5*n*n)/(n + n*n)
c = sp.limit_seq(an)
print(c)

print('Câu d')
an = n**3 / (n + 1)
d = sp.limit_seq(an)
print(d)

print('Câu e')
an = sp.exp(1/n)
e = sp.limit_seq(an)
print(e)

print('Câu f')
an = sp.sqrt((n+1)/(9*n+1))
f = sp.limit_seq(an)
print(f)

print('Câu g')
an = ((-1)**(n+1)*n) / (n + sp.sqrt(n))
g = sp.limit_seq(an)
print(g)

print('Câu h')
an = sp.tan((2*n*sp.pi)/(1 + 8*n))
h = sp.limit_seq(an)
print(h)

print('Câu i')
an = sp.factorial(2*n -1)/sp.factorial(2*n +1)
i = sp.limit_seq(an)
print(i)

print('Câu j')
an = sp.log(2*n*n + 1) - sp.log(n*n + 1)
j = sp.limit_seq(an)
print(j)