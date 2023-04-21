import math
sum = float(0)
for x in range(1, 99+1, 1):
    sum = ( sum + ( x / (x + 1) ) )
    if (x >= 100):
        break
print("ket qua cua M la:",'%.4f'%(sum))
y = '%.4f'%(sum)
print("ket qua cua M la:",y)