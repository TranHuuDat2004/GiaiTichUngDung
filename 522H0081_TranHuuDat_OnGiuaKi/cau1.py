import math

a = math.sqrt(1234) + 1234**(1/3) + math.log(1234, 5) + math.sin(1234)
print('cau a:', '%.4f'%(a))

b = 0
for x in range (1, 1001, 1):
    b = x + b
print('cau b:', b)
