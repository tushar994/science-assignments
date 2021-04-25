V = 1
N = 10000
Trials = 100
# Importing datetime.
from datetime import datetime
import random
import numpy as np
import matplotlib.pyplot as plt
import math
# Creating a datetime object so we can test.
a = datetime.now()

# Converting a to string in the desired format (YYYYMMDD) using strftime
# and then to int.
a = int(a.strftime('%Y%m%d%s'))
random.seed(a)

# Plot I vs Number of points (N)
x = []
points = []
points2 = []
while(len(points)<N):
    i = random.uniform(0,1)
    j = random.uniform(0,1)
    points.append(i)
    points2.append(j)
    points_ans = np.array(points)
    points_ans2 = np.array(points2)
    points_ans = np.square((points_ans))*points_ans2

    x.append(V*np.average(points_ans))

plt.plot(x)
plt.show()


# Fix N=20; 100 trials; Plot I vs trials; calculate std deviation.
x = []
for i in range(1,100):
    points = np.random.uniform(0,1,20)
    points2 = np.random.uniform(0,1,20)
    points = np.square((points))*points2
    x.append(V*np.average(points))

# standard deviation
x = np.array(x)
print("standard deviation for N=20: ",math.sqrt(np.var(x)))
plt.plot(x)
plt.show()



# Fix N=1000; 100 trials; Plot I vs trials; calculate std deviation.
x = []
for i in range(1,100):
    points = np.random.uniform(0,1,1000)
    points2 = np.random.uniform(0,1,1000)
    points = np.square((points))*points2
    x.append(V*np.average(points))

# standard deviation
x = np.array(x)
print("standard deviation for N=1000: ", math.sqrt(np.var(x)))
plt.plot(x)
plt.show()


# standard deviation for fixed number number of trials vs N
trials = 100
n = 1000
x = []
for i in range(1,n+1):
    I = []
    for j in range(trials):
        points = np.random.uniform(0,1,i)
        points2 = np.random.uniform(0,1,i)
        points = np.square((points))*points2
        I.append(V*np.average(points))
    I = np.array(I)
    x.append(math.sqrt(np.var(I)))

plt.plot(x)
plt.show()


