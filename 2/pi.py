import random
import matplotlib.pyplot as plt

# Importing datetime.
from datetime import datetime

import math
# Creating a datetime object so we can test.
a = datetime.now()

# Converting a to string in the desired format (YYYYMMDD) using strftime
# and then to int.
a = int(a.strftime('%Y%m%d%s'))
# print(a)
random.seed(a)

inside=0
tot=0
x = random.uniform(0,1)
y = random.uniform(0,1)

pi_values = []

# print(x,y)
for i in range(0,1000000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    # print("x is",x*x)
    # print("y is",y*y)
    if ((x*x) + (y*y)) <= 1:
        inside+=1
    tot +=1
    pi_values.append((inside*4)/tot)

# print(inside)

pi = ((inside*4)/tot)

plt.plot(pi_values)
plt.plot([math.pi for i in range(0,1000000)])
plt.xlabel("n")
plt.ylabel("predicted value of pi")
plt.show()
print(pi)