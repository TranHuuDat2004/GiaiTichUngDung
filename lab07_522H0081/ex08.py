import sympy as sp
import matplotlib.pyplot as plt
import math

n = sp.symbols('n')

# print('Câu a')
def fa(n):
    num = 1
    demon = 1
    for i in range (1, n+1, 1):
        num = -2 
        demon = math.e
    return 1 -( (num / demon) ** n) # tử / mẫu

a = [fa(i) for i in range (50)]
plt.plot(a)
plt.title('Câu a')
plt.grid()
plt.show()

# print('Câu b')
def fb(n):
    num = 1
    demon = 1
    for i in range (1, n+1, 1):
        num = sp.pi 
        demon = sp.sqrt(i)
    return sp.sqrt(n) * sp.sin(num / demon)   # tử / mẫu

a = [fb(i) for i in range (50)]
plt.plot(a)
plt.title('Câu b')
plt.grid()
plt.show()

# print('Câu c')
def fc(n):
    num = 1
    demon = 1
    for i in range (1, n+1, 1):
        num = 3 + 2*i**2
        demon = 8*i**2 + i
    return sp.sqrt(num / demon)   # tử / mẫu

a = [fc(i) for i in range (50)]
plt.plot(a)
plt.title('Câu c')
plt.grid()
plt.show()

# print('Câu d')
def fd(n):
    num = 1
    demon = 1
    for i in range (1, n+1, 1):
        num = i*i * sp.cos(i)
        demon = (1 + i*i)
    return (num / demon)   # tử / mẫu

a = [fd(i) for i in range (50)]
plt.plot(a)
plt.title('Câu d')
plt.grid()
plt.show()



# print('Câu e')
def fe(n):
    num = 1
    demon = 1
    for i in range (1, n+1, 1):
        num *= 2*i-1  # 1* 3* 5* 7* 9* ...* 2n-1  
        demon *= i  # 1* 2* 3* 4* 5* 6* ...* n
    return num / demon   # tử / mẫu

a = [fe(i) for i in range (50)]
plt.plot(a)
plt.title('Câu e')
plt.grid()
plt.show()

# print('Câu f')
def ff(n):
    num = 1
    demon = 1
    for i in range (1, n+1, 1):
        num *= 2*i-1  # 1* 3* 5* 7* 9* ...* 2n-1  
        demon *= (2*i)**i  # 2*1**1  *  2*2**2  *  2*3**3
    return num / demon   # tử / mẫu

a = [ff(i) for i in range (50)]
plt.plot(a)
plt.title('Câu f')
plt.grid()
plt.show()


