import matplotlib.pyplot as plt
import numpy as np
import math

H = 9
k = 5
m = 4

x = np.linspace(-1*math.sqrt(10), math.sqrt(10), 10000000)


p = np.sqrt(m*(H - k*(x**2)))
p1 = -1*np.sqrt(m*(H - k*(x**2)))

plt.plot(x, p, color = "red")
plt.plot(x, p1 , color = "red")

plt.show()