import numpy as np

f1 = lambda x: x+5
f2 = lambda x: x**2 - 3

fa = f1(f2(3))
print('a.',fa)

fb = f2(f1(3))
print('b.',fb)

fc = f1(f1(-5))
print('c.',fc)

fd = f2(f2(2))
print('d.',fd)