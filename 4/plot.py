import matplotlib.pyplot as plt
import numpy as np
import math


w = 10
h = 10

dx = 0.1
dy=0.1

Dx = 4
Dy = 4
dt = 0.1

p = np.zeros((int(w/dx),int(h/dy)))


p[int(len(p)/2)][int(len(p)/2)] = 1
print(p)

def return_p(p,i,j):
    if(i>=len(p)):
        return 0
    elif(j>=len(p)):
        return 0
    elif((i-int(len(p)/2))**2 + (j-int(len(p)/2))**2 >= int(len(p)/2)):
        return 0
    else:
        return p[i][j]


for k in range(0,1000):
    p_temp = np.zeros((int(w/dx) ,int(h/dy)))
    for i,value1 in enumerate(p):
        for j,value2 in enumerate(value1):
            uxx = (return_p(p,i+1,j) - 2*return_p(p,i,j) + return_p(p,i-1,j)) / (dx*dx)
            uyy = (return_p(p,i,j+1) - 2*return_p(p,i,j) + return_p(p,i,j-1)) / (dy*dy)
            p_temp[i][j] = p[i][j] + Dx*dt*uxx + Dy*dt*uyy
    p = p_temp
print(p)

