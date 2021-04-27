import random
import time
import numpy as np
import math

random.seed(time.time())


lx = 18*(10**-10)
ly = 18*(10**-10)
lz = 18*(10**-10)

eta = (0.238 * 4184) / (6.0221415*(10**23))
sigma = 3.4*(10**-10)




def normal_distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)



def box_distance(p1,p2):
    arr1 = [p1[i]-p2[i] for i in range(0,len(p1))]
    arr2 = [arr1[i] - lx*round(arr1[i]/lx) for i in range(0,len(arr1))]
    return math.sqrt(arr2[0]**2 + arr2[1]**2 + arr2[2]**2)

def find_potential(set_of_points):
    ans = 0
    for i,val in enumerate(set_of_points):
        for j in range(i+1,len(set_of_points)):
            dist = box_distance(val,set_of_points[j])
            ans += (4*eta*((sigma/dist)**12 - (sigma/dist)**6))
    return ans



def force_vector(p1,p2):
    arr1 = [p1[i]-p2[i] for i in range(0,len(p1))]
    arr2 = [arr1[i] - lx*round(arr1[i]/lx) for i in range(0,len(arr1))]
    deno =  math.sqrt(arr2[0]**2 + arr2[1]**2 + arr2[2]**2)
    return [val/deno for val in arr2]

def total_force(p1,set_of_points):
    force_tot = [0,0,0]
    for i in range(0,len(set_of_points)):
        if np.isclose(p1, set_of_points[i], atol=float(1e-21)).all():
            continue
        if set_of_points[i] != p1:
            force_dir = force_vector(p1, set_of_points[i])
            dist = box_distance(set_of_points[i],p1)
            force_mag = 4*eta*((((sigma/dist)**12)*(-12/dist)) - (((sigma/dist)**6)*(-6/dist)))
            force = [force_dir[0]*force_mag, force_dir[1]*force_mag, force_dir[2]*force_mag]
            force_tot = [force[0]+force_tot[0], force[1]+force_tot[1], force[2]+force_tot[2]]
    return force_tot




def return_force_arr(set_of_points):
    force_arr = []
    for i in set_of_points:
        force_arr.append(total_force(i,set_of_points))
    return force_arr

def return_second_state(set_of_points,force_arr):
    step = 0.0002
    next_con = []
    for i in range(0,len(set_of_points)):
        next_con.append([set_of_points[i][0]- step*force_arr[i][0], set_of_points[i][1]- step*force_arr[i][1], set_of_points[i][2]- step*force_arr[i][2]])
    return next_con

def return_boxed_config(config):
    for i in range(0,len(config)):
        for j in range(0,len(config[i])):
            if config[i][j]>lx:
                config[i][j]-=lx
            if config[i][j]<0:
                config[i][j]+=lx
    return config
            
        
        
def find_config(set_of_points):

    iterations = 0
    ini_config = set_of_points.copy()
    while(True):
        iterations+=1
        starting_energy = find_potential(ini_config)
        force_arr = return_force_arr(ini_config)
        second_state = return_second_state(ini_config,force_arr)
        second_state = return_boxed_config(second_state)
        final_energy = find_potential(second_state)
        ini_config = second_state.copy()
        print("iterations" , iterations)
        print(final_energy)
        if np.isclose(starting_energy, final_energy, atol = 10**-21):
            print("Energy of final configuration:", final_energy)
            break
    return ini_config







random.seed(time.time())
init_state = []
num = 0
while(num<108):
    flag =0 
    new_coor = [random.uniform(0,lx),random.uniform(0,lx),random.uniform(0,lx)]
    for i in init_state:
        if(normal_distance(new_coor,i)<sigma):
            flag = 1
    if(flag==0):
        init_state.append(new_coor)
        num+=1
# print(init_state)
print("initial energy of the configuration is ",find_potential(init_state))
ff = open("initial.xyz", 'w')
for i in init_state:
    print('C '+str(i[0])+' '+str(i[1])+' '+str(i[2]), file = ff)
ff.close()



init_state = find_config(init_state)
# print(len(init_state[0]))
ff = open("optimal.xyz", 'w')
for i in init_state:
    print('C '+str(i[0])+' '+str(i[1])+' '+str(i[2]), file = ff)
ff.close()




hash_map = [0,1,2]

def del_Unit(n, m, i, j):
    if i == j:
        return 0
    elif m==n and i!=j:
        return -4*eta*((168*(sigma**12)/((box_distance(init_state[i], init_state[j]))**16))-(48*(sigma**6)/(box_distance(init_state[i], init_state[j]))**10))*(init_state[i][n]-init_state[j][n])*(init_state[i][m]-init_state[j][m]) -4*eta*((6*(sigma**6)/(box_distance(init_state[i], init_state[j]))**8)-12*(sigma**12)/((box_distance(init_state[i], init_state[j]))**14))
    else:
        return -4*eta*((168*(sigma**12)/(box_distance(init_state[i], init_state[j]))**16)-(48*(sigma**6)/(box_distance(init_state[i], init_state[j]))**10))*(init_state[i][n]-init_state[j][n])*(init_state[i][m]-init_state[j][m]) 

constant_len = 3*108
    
matrix = np.zeros((constant_len, constant_len))

for i,val in enumerate(matrix):
    for j,val2 in enumerate(matrix):
        matrix[i][j] = del_Unit(hash_map[i%3],hash_map[j%3], i//3,j//3)
# print(matrix)
ff = open("hessian.txt", 'w')
np.set_printoptions(threshold=np.inf)
print(matrix, file = ff)
ff.close()

w, v = np.linalg.eig(matrix)
print("There are", len(w), "eigenvalues and corresponding vectors as follows: ")
print("")
print("List of all eigenvalues:", w)
print("")
print("List of all eigenvalues with corresponding eigenvectors: ")
print("")
for i in range(len(w)):
    print(i+1, "Eigenvalue:", w[i])
    print("Eigenvector:", v[i])
    print("")

ff = open("eigen_vector_value.txt", 'w')
np.set_printoptions(threshold=np.inf)
for i,val in enumerate(w):
    print(val , ":", v[i], file = ff)


ff.close()