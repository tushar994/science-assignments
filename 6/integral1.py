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

# Plot I vs Number of pointes (N)
# x = []
# points = []
# while(len(points)<N):
#     i = random.uniform(0,1)
#     if(not i in points):
#         points.append(i)
#         points_ans = np.array(np.array(points))
#         points_ans = 3*np.square((points_ans))

#         x.append(V*np.average(points_ans))

# plt.plot(x)
# plt.show()


# Fix N=20; 100 trials; Plot I vs trials; calculate std deviation.
# x = []
# for i in range(1,100):
#     points = np.random.uniform(0,1,20)
#     points = 3*np.square((points))
#     x.append(V*np.average(points))

# # standard deviation
# print(math.sqrt(np.var(x)))
# plt.plot(x)
# plt.show()
# x = np.array(x)



# Fix N=1000; 100 trials; Plot I vs trials; calculate std deviation.
# x = []
# for i in range(1,100):
#     points = np.random.uniform(0,1,1000)
#     points = 3*np.square((points))
#     x.append(V*np.average(points))

# # standard deviation
# print(math.sqrt(np.var(x)))
# plt.plot(x)
# plt.show()
# x = np.array(x)


# standard deviation for fixed number number of trials vs N
trials = 100
n = 1000
x = []
for i in range(1,n+1):
    I = []
    for j in range(trials):
        points = np.random.uniform(0,1,i)
        points = 3*np.square((points))
        I.append(V*np.average(points))
    I = np.array(I)
    x.append(math.sqrt(np.var(I)))

plt.plot(x)
plt.show()


