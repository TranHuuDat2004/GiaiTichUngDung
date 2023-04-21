import sympy as sp
import math

n = sp.symbols('n')

print('Câu a')
fa = sp.Sum(4**n, (n, 1, sp.oo))  # 4**n = 4 +16 +64 +256 +...
print(fa)
converged = fa.is_convergent()  # kiểm tra có tính hội tụ 
print(converged)

print('Câu b')
fb = sp.Sum((5/2**n), (n, 1, sp.oo))  # 5/2**n = 5/2 + 5/4 + 5/8
print(fb)
converged = fb.is_convergent()  # kiểm tra có tính hội tụ 
print(converged)

