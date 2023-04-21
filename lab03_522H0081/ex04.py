import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.arange(-5, 5.1, 0.1)
y1 = np.array(list(map(lambda t: -t**3, x1)))

plt.plot(x1, y1, color = 'red')
plt.title('câu 4i')
plt.show()



x2 = np.arange(-5, 5.5, 0.5)
y2 = np.array(list(map(lambda t: -1 / t**2, x2)))

plt.plot(x2, y2, color = 'blue')
plt.title('câu 4j')
plt.show()



x3 = np.arange(-5, 5.25, 0.25)
y3 = np.array(list(map(lambda t: -1 / t, x3)))

plt.plot(x3, y3, color = 'purple')
plt.title('câu 4k')
plt.show()



x4 = np.arange(-6, 7.5, 0.5)
y4 = np.array(list(map(lambda t: 1 / abs(t) , x4)))

plt.plot(x4, y4, color = 'green')
plt.title('câu 4l')
plt.show()



x5 = np.arange(-2, 2.1, 0.1)
y5 = np.array(list(map(lambda t: math.sqrt((abs(t))) , x5)))

plt.plot(x5, y5, color = 'brown')
plt.title('câu 4m')
plt.show()



x6 = np.arange(-2, 6.25, 0.25)
y6 = np.array(list(map(lambda t: math.sqrt((abs(-t))) , x6)))

plt.plot(x6, y6, color = 'black')
plt.title('câu 4n')
plt.show()
