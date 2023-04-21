import sympy as sp
import matplotlib.pyplot as plt
import math

n = sp.symbols('n')


# print('Câu a')
an = 1 - (0.2)**n
l = []
for n in range(1, 10, 1):
    an = 1 - (0.2)**n
    l.append(an)

plt.plot(l) # x tự động thêm, y = l
plt.title('Câu a')
plt.grid()
plt.show()


# print('Câu b')
an = 2*n / (n*n + 1)
l = []
for n in range(1, 10, 1):
    an = 2*n / (n*n + 1)
    l.append(an)

plt.plot(l) # x tự động thêm, y = l
plt.title('Câu b')
plt.grid()
plt.show()


# print('Câu c')
an = (-1)**(n-1) / 5**n
l = []
for n in range(1, 10, 1):
    an = (-1)**(n-1) / 5**n
    l.append(an)

plt.plot(l) # x tự động thêm, y = l
plt.title('Câu c')
plt.grid()
plt.show()


# print('Câu d')
an = 1 / (sp.factorial(n+1))
l = []
for n in range(1, 10, 1):
    an = 1 / (sp.factorial(n+1))
    l.append(an)

plt.plot(l) # x tự động thêm, y = l
plt.title('Câu d')
plt.grid()
plt.show()


# print('Câu e')
a = 1
l = [a]
for a in range(2, 6, 1):
    a = 5*a -3
    l.append(a)

plt.plot(l) # x tự động thêm, y = l
plt.title('Câu e')
plt.grid()
plt.show()


# print('Câu f')
a = 2
l = [a]
for a in range(2, 6, 1):
    a = a / (a + 1)
    l.append(a)

plt.plot(l) # x tự động thêm, y = l
plt.title('Câu f')
plt.grid()
plt.show()
