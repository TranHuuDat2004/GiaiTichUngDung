import math

print('Câu a')
fa = lambda x,y: x*x + x*y**3
points = [(0, 0), (-1, 1), (2, 3), (-3, -2)]
for p in points:
    a, b = p
    print(fa(a, b))

print('Câu b')
fb = lambda x,y,z: (x-y)/(y*y+z*z)
points = [(3, -1, 2), (1, 1/2, 1/4), (0, -1/3, 0), (2, 2, 100)]
for p in points:
    a, b, c = p
    print(fb(a, b, c))