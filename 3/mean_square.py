import matplotlib.pyplot as plt
import numpy as np
import math

k = 10
c1 =10
c2 = 10

x = np.linspace(0, 20, 10000000)

y = (c2*np.sin(k*x) + c1*np.cos(k*x) - c1)**2

plt.plot(x, y, color = "red")

plt.show()