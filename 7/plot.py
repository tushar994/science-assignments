import numpy as np
import matplotlib.pyplot as plt
import random
import time
import math

random.seed(time.time())


J = 1

def Find_energy(model):
    E = 0
    for i in range(len(model)):
        E -= J*model[i]*model[(i+1)%len(model)]
    return E

size = 1000
steps = 100
journey = 1000
dT = 1
T = np.linspace(0,journey,int(journey/dT))

energy = []
magnet = []

for temp in T:
    model = [random.choice([-1, 1]) for i in range(size)]
    E = Find_energy(model)

    for i in range(steps):
        change_site = random.randint(0,size-1)
        model2 = [i for i in model]
        model2[change_site] *=-1
        E2 = Find_energy(model2)
        if(E2<E):
            model = model2
            E = E2
        else:
            rand_num = random.uniform(0,1)
            if rand_num < math.exp(-(E2-E)/((temp+dT))):
                model = model2
                E = E2
    energy.append(E)
    magnet.append(sum(model))


plt.xlabel('Temperature')
plt.ylabel("Energy")
plt.plot(T, energy)
plt.show()

plt.xlabel('Temperature')
plt.ylabel("Magnetisation")
plt.plot(T, magnet)
plt.show()


