import matplotlib.pyplot as plt
import numpy as np


def fa():
    fa = lambda x: x ** 3 - x / 2

    x_array = np.arange(-10, 10 + 0.1, 0.1)
    ya_array = np.array( list( map(fa, x_array) ) )

    valuesX = []
    valuesY = []

    for xi in x_array:
        valuesX.append(xi)
    for yi in ya_array:
        valuesY.append(yi)

    sortedX = sorted(valuesX)
    sortedY = sorted(valuesY)
    RevSortedY = sorted(valuesY, reverse = True)
    if (valuesX == sortedX ):
        if (valuesY == sortedY or valuesY == RevSortedY):
            print('fa: x ** 3 - x / 2 is one-to-one function')
        else:
            print('fa: x ** 3 - x / 2 is not one-to-one function')

    plt.plot(x_array, ya_array, color = "red")
    plt.title("Câu 7a")
    plt.grid()
    plt.show()

fa()


def fb():
    fb = lambda x: x ** 2 + x / 2

    x_array = np.arange(-10, 10 + 0.1, 0.1)
    yb_array = list( map(fb, x_array))

    valuesX = []
    valuesY = []

    for xi in x_array:
        valuesX.append(xi)
    for yi in yb_array:
        valuesY.append(yi)

    sortedX = sorted(valuesX)
    sortedY = sorted(valuesY)
    RevSortedY = sorted(valuesY, reverse = True)

    if (valuesX == sortedX ):
        if (valuesY == sortedY or valuesY == RevSortedY):
            print('fb: x ** 2 + x / 2 is one-to-one function')
        else:
            print('fb: x ** 2 + x / 2 is not one-to-one function')

    plt.plot(x_array, yb_array, color = "green")
    plt.title("Câu 7b")
    plt.grid()
    plt.show()

fb()