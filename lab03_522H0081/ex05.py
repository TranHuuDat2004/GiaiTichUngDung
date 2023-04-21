import matplotlib.pyplot as plt
import numpy as np



f1 = lambda t : (1-(abs(t)-1)**2)**1/2
x1 = np.arange(-2, 2.1, 0.1) 
y1 = list( map(f1, x1) )

plt.plot(x1, y1, color = 'magenta' )
plt.title('câu 5a')
plt.show()



f2 =  lambda t : (-3)*((1-(abs(t)/2)**1/2)**1/2)
x2 = np.arange(-2, 2.1, 0.1)
y2 = list( map(f2, x2) )
        
plt.plot(x2, y2, color = 'red' )
plt.title('câu 5b')
plt.show()

