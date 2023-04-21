import math 
so_le = 0
so_chan = 0 
for x in range(1, 9+1, 1):
    if x % 2 == 1:
    	so_le += 1
for x in range(1, 9+1, 1):
    if x % 2 == 0:
    	so_chan += 1
print("So luong cua so le:",so_le)
print("So luong cua so chan:",so_chan)