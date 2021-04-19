import random
import matplotlib.pyplot as plt

# Importing datetime.
from datetime import datetime

# Creating a datetime object so we can test.
a = datetime.now()

def factorial(n):
    ans=1
    while(n>0):
        ans*=n
        n-=1
    return ans

def power(n,i):
    ans = 1
    while(i>0):
        ans*=n
        i-=1
    return ans

# Converting a to string in the desired format (YYYYMMDD) using strftime
# and then to int.
a = int(a.strftime('%Y%m%d%s'))
print(a)
random.seed(a)

n=100

print("1")
meet_count = []
displacement_list = []
square_displacement_list = []
origin_count = []

for j in range(1,n+1):
    meet_count.append(0)
    origin_count.append(0)
    displacement_list.append([])
    square_displacement_list.append([])


total = 0
iterations = 100000
for i in range(1,iterations):
    pos1 = 0
    pos2 = 0
    total+=1
    for j in range(0,n):
        a = random.randint(0,1)
        if a==0:
            pos1+=1
        else:
            pos1-=1
        a = random.randint(0,1)
        if a==0:
            pos2+=1
        else:
            pos2-=1
        # if they meet then increment the number of times  they meet after j steps
        if pos1==pos2:
            meet_count[j] += 1
        # if the first guy is at 0, then increment the number of times of that
        if pos1==0:
            origin_count[j] += 1
        # # if the second guy is at 0, then increment the number of times of that
        if pos2==0:
            origin_count[j] += 1
        # # update displacement after j steps
        displacement_list[j].append(pos1)
        displacement_list[j].append(pos2)
        # # update square displacement after j steps
        square_displacement_list[j].append(pos1*pos1)
        square_displacement_list[j].append(pos2*pos2)


mean_displacement = []
square_mean_displacement = []

for j in range(0,n):
    meet_count[j] = meet_count[j]/total
    origin_count[j] = origin_count[j]/(2*total)
    sum2 =0 
    total2 = 0
    for num in displacement_list[j]:
        total2+=1
        sum2+=num
    mean_displacement.append(sum2/total2)
    sum2 =0 
    total2 = 0
    for num in square_displacement_list[j]:
        total2+=1
        sum2+=num
    square_mean_displacement.append(sum2/total2)


            



print("2")
## calculating actual value of the drfunks ending at same position
math = []
for j in range(1,n+1):
    math.append( (factorial(2*j) / (factorial(j)*factorial(j) ))  *  (power(0.5,2*j))  )
print("3")

## calculating actual value of drunks ending at orgin
origin_prob = []
for j in range (1,n+1):
    if j%2==1:
        origin_prob.append(0)
    else:
        origin_prob.append ( (power(0.5,j) * ( (factorial(j) )/( factorial(j/2) * factorial(j/2) ) )) )
        
## calculating mean displacement
mean_displacement_calc = [0 for j in range (1,n+1)]

square_mean_displacement_calc = [j for j in range (1,n+1)]

## plotting number of times they meet
plt.plot(meet_count)
plt.plot(math)
plt.ylabel("Probability of them meeting vs predicted value of the same")
plt.xlabel("n")
plt.show()

# plt.plot(meet_count)
# plt.show()

## plotting probability of him being at the origin
plt.plot(origin_count)
plt.plot(origin_prob)
plt.xlabel("n")
plt.ylabel("Probability of drunk ending at origin vs predicted value of the same")
plt.show()

## plotting mean displacement
plt.plot(mean_displacement_calc , color="orange")
plt.plot(mean_displacement, color="blue")
plt.xlabel("n")
plt.ylabel("mean displacement")
plt.show()

## plotting mean squared displacement
plt.plot(square_mean_displacement_calc , color="orange")
plt.plot(square_mean_displacement , color="blue")
plt.xlabel("n")
plt.ylabel("mean square displacement")
plt.show()