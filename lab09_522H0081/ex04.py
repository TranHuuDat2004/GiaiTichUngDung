import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

x = sp.symbols('x')

def plot_graph(f, a, b, xs, ys): # vẽ biểu đồ
    lx = np.linspace(a, b, 1000)
    ly = [f.subs(x, it).evalf() for it in lx]
    plt.plot(lx, ly)
    plt.scatter(xs, ys)

# a
print('\nCâu a')
f = x**2 -2*x -5
a, b = 0, 2 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu a')
plt.show()


# b
print('\nCâu b')
f = 3*x + x**3 + 5
a, b = -4, 4 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)



# c
print('\nCâu c')
f = sp.sin(x) + 3*x**2
a, b = -2, 2 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
# lx = sp.solve(df)
# print('x = ',lx)



# d
print('\nCâu d')
f = sp.exp(x**2) + 3*x
a, b = -1, 1 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu d')
plt.show()


# e
print('\nCâu e')
f = x**3 - 3*x
a, b = -3, 0 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu e')
plt.show()


# f
print('\nCâu f')
f = x**3 - 3*x
a, b = 0, 3 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu f')
plt.show()


# g
print('\nCâu g')
f = sp.sin(x)
a, b = 0, math.pi # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu g')
plt.show()


# h
print('\nCâu h')
f = sp.sin(2*x)
a, b = 0, 2 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu h')
plt.show()


# i
print('\nCâu i')
f = sp.cos(x)
a, b = math.pi/2 , 3*math.pi/2 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu i')
plt.show()


# j
print('\nCâu j')
f = sp.tan(x)*sp.tan(x)
a, b = -math.pi/4, math.pi/4  # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu j')
plt.show()


# k
print('\nCâu k')
f = sp.exp(x)*sp.sin(x)
a, b = 0, math.pi # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu k')
plt.show()


# l
print('\nCâu l')
f = x**4 * 3*x**2
a, b = -4, 0 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu l')
plt.show()


# m
print('\nCâu m')
f = x**4 - 3*x**2
a, b = 0, 4 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu m')
plt.show()


# n
print('\nCâu n')
f = x**5 - 5*x**3
a, b = -4, 0 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu n')
plt.show()


# o
print('\nCâu o')
f = x**6 - 5*x**2
a, b = -1, 1 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)



# p
print('\nCâu p')
f = x**3 - 9*x
a, b = -3, 0 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu p')
plt.show()


# q
print('\nCâu q')
f = x**3 - 9*x
a, b = 0, 3 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b ] + [a, b])
print('x = ',lx)
ly = np.array([f.subs(x, x0).evalf() for x0 in lx])
print('y = ',ly)
indices = np.array([np.argmin(ly), np.argmax(ly)])
print('indices = ', indices)
xs = lx[indices]
print('xs = ',xs)
ys = ly[indices]
print('ys = ',ys)
plot_graph(f, a, b, xs, ys)
plt.title('Câu q')
plt.show()


# r
print('\nCâu r')
f = x**3 + 9*x
a, b = -1, 1 # unpacking
print('f = ',f)
print('a, b = ', a, b)
df = f.diff()
print("f' = ",df)
lx = sp.solve(df)
print('x = ',lx)
