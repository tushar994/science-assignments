import math
import pandas as pd
particles = pd.read_csv("./info.csv")
particles = particles.to_numpy()
# print(particles)

class Molecule:
    def __init__(self, h1x, h1y, h1z, h2x, h2y, h2z, ox, oy, oz):
        self.h1x = h1x
        self.h1y = h1y
        self.h1z = h1z
        self.h2x = h2x
        self.h2y = h2y
        self.h2z = h2z
        self.ox = ox
        self.oy = oy
        self.oz = oz


A = 582*(10**3)
B = 595
k = 332.1
O_charge = -0.834
H_charge = 0.417
qo = -0.834
qh = 0.417
lx = 23.623
ly = 22.406
lz = 27.1759

def get_pot(m1,m2):
    potential_energy = 0.0
    # potential_energy += k*(H_charge*H_charge)/distance( m1.h1x, m1.h1y, m1.h1z, m2.h1x, m2.h1y, m2.h1z)
    # potential_energy += k*(H_charge*H_charge)/distance( m1.h1x, m1.h1y, m1.h1z, m2.h2x, m2.h2y, m2.h2z)
    # potential_energy += k*(H_charge*O_charge)/distance(m1.h1x, m1.h1y, m1.h1z, m2.ox, m2.oy, m2.oz)


    # potential_energy += k*(H_charge*H_charge)/distance(m1.h2x, m1.h2y, m1.h2z, m2.h1x, m2.h1y, m2.h1z)
    # potential_energy += k*(H_charge*H_charge)/distance( m1.h2x, m1.h2y, m1.h2z, m2.h2x, m2.h2y, m2.h2z)
    # potential_energy += k*(H_charge*O_charge)/distance( m1.h2x, m1.h2y, m1.h2z, m2.ox, m2.oy, m2.oz)

    # potential_energy += k*(H_charge*O_charge)/distance( m1.ox, m1.oy, m1.oz, m2.h1x, m2.h1y, m2.h1z)
    # potential_energy += k*(H_charge*O_charge)/distance( m1.ox, m1.oy, m1.oz, m2.h2x, m2.h2y, m2.h2z)
    # potential_energy += k*(O_charge*O_charge)/distance( m1.ox, m1.oy, m1.oz, m2.ox, m2.oy, m2.oz)
    
    
    potential_energy += k*(H_charge*H_charge)/three_coor( m1.h1x, m1.h1y, m1.h1z, m2.h1x, m2.h1y, m2.h1z)
    potential_energy += k*(H_charge*H_charge)/three_coor( m1.h1x, m1.h1y, m1.h1z, m2.h2x, m2.h2y, m2.h2z)
    potential_energy += k*(H_charge*O_charge)/three_coor( m1.h1x, m1.h1y, m1.h1z, m2.ox, m2.oy, m2.oz)

    # print(potential_energy)

    potential_energy += k*(H_charge*H_charge)/three_coor( m1.h2x, m1.h2y, m1.h2z, m2.h1x, m2.h1y, m2.h1z)
    potential_energy += k*(H_charge*H_charge)/three_coor( m1.h2x, m1.h2y, m1.h2z, m2.h2x, m2.h2y, m2.h2z)
    potential_energy += k*(H_charge*O_charge)/three_coor( m1.h2x, m1.h2y, m1.h2z, m2.ox, m2.oy, m2.oz)

    potential_energy += k*(H_charge*O_charge)/three_coor( m1.ox, m1.oy, m1.oz, m2.h1x, m2.h1y, m2.h1z)
    potential_energy += k*(H_charge*O_charge)/three_coor( m1.ox, m1.oy, m1.oz, m2.h2x, m2.h2y, m2.h2z)
    potential_energy += k*(O_charge*O_charge)/three_coor( m1.ox, m1.oy, m1.oz, m2.ox, m2.oy, m2.oz)



    potential_energy += A/(three_coor(m1.ox, m1.oy, m1.oz, m2.ox, m2.oy, m2.oz)**6)
    potential_energy -= B/(three_coor(m1.ox, m1.oy, m1.oz, m2.ox, m2.oy, m2.oz)**3)

    # potential_energy += A/(distance(m1.ox, m1.oy, m1.oz, m2.ox, m2.oy, m2.oz)**6)
    # potential_energy -= B/(distance(m1.ox, m1.oy, m1.oz, m2.ox, m2.oy, m2.oz)**3)
    return potential_energy

def distance(x1,y1,z1,x2,y2,z2):
    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def get_pot2(m1,m2):
    potential_energy = 0
    potential_energy += k*(H_charge*H_charge)/distance( m1.h1x, m1.h1y, m1.h1z, m2.h2x, m2.h2y, m2.h2z)
    potential_energy += k*(H_charge*O_charge)/distance( m1.h1x, m1.h1y, m1.h1z, m2.ox, m2.oy, m2.oz)
    potential_energy += k*(H_charge*O_charge)/distance( m1.h2x, m1.h2y, m1.h2z, m2.ox, m2.oy, m2.oz)
    return potential_energy


def three_coor(x1,y1,z1,x2,y2,z2):
    x_dif = abs(x1-x2)
    x_fin = x_dif - lx*round(x_dif/lx)
    # x_fin = min(x_dif,x_dif - lx, x_dif + lx)

    y_dif = abs(y1-y2)
    y_fin = y_dif - ly*round(y_dif/ly)
    # y_fin = min(y_dif,y_dif - ly, y_dif + ly)
    
    z_dif = abs(z1-z2)
    z_fin = z_dif - lz*round(z_dif/lz)
    # z_fin = min(z_dif,z_dif - lz, z_dif + lz)

    return ((z_fin**2) + (y_fin**2) + (x_fin**2))


def get_r2(m1, m2):
    # m1 h1 with m2 h2
    e = 0

    rx = m1.h1x-m2.h2x   
    rxm = rx - lx*round(rx/lx)
    ry = m1.h1y-m2.h2y  
    rym = ry - ly*round(ry/ly)
    rz = m1.h1z-m2.h2z 
    rzm = rz - lz*round(rz/lz)
    rm1h1m2h2 = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qh)/rm1h1m2h2

    # m1 h1 with m2 h1
    rx = m1.h1x-m2.h1x   
    rxm = rx - lx*round(rx/lx)
    ry = m1.h1y-m2.h1y  
    rym = ry - ly*round(ry/ly)
    rz = m1.h1z-m2.h1z 
    rzm = rz - lz*round(rz/lz)
    rm1h1m2h1 = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qh)/rm1h1m2h1

    # m1 h1 with m2 0
    rx = m1.h1x-m2.ox   
    rxm = rx - lx*round(rx/lx)
    ry = m1.h1y-m2.oy  
    rym = ry - ly*round(ry/ly)
    rz = m1.h1z-m2.oz 
    rzm = rz - lz*round(rz/lz)
    rm1h1m2o = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qo)/rm1h1m2o

    # m1 h2 with m2 h2
    rx = m1.h2x-m2.h2x   
    rxm = rx - lx*round(rx/lx)
    ry = m1.h2y-m2.h2y  
    rym = ry - ly*round(ry/ly)
    rz = m1.h2z-m2.h2z 
    rzm = rz - lz*round(rz/lz)
    rm1h2m2h2 = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qh)/rm1h2m2h2

    # m1 h2 with m2 h1
    rx = m1.h2x-m2.h1x   
    rxm = rx - lx*round(rx/lx)
    ry = m1.h2y-m2.h1y  
    rym = ry - ly*round(ry/ly)
    rz = m1.h2z-m2.h1z 
    rzm = rz - lz*round(rz/lz)
    rm1h2m2h1 = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qh)/rm1h2m2h1

    # m1 h2 with m2 o
    rx = m1.h2x-m2.ox   
    rxm = rx - lx*round(rx/lx)
    ry = m1.h2y-m2.oy  
    rym = ry - ly*round(ry/ly)
    rz = m1.h2z-m2.oz 
    rzm = rz - lz*round(rz/lz)
    rm1h2m2o = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qo)/rm1h2m2o

    # m1 o with m2 h2
    rx = m1.ox-m2.h2x   
    rxm = rx - lx*round(rx/lx)
    ry = m1.oy-m2.h2y  
    rym = ry - ly*round(ry/ly)
    rz = m1.oz-m2.h2z 
    rzm = rz - lz*round(rz/lz)
    rm1om2h2 = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qo)/rm1om2h2

    # m1 o with m2 h1
    rx = m1.ox-m2.h1x   
    rxm = rx - lx*round(rx/lx)
    ry = m1.oy-m2.h1y  
    rym = ry - ly*round(ry/ly)
    rz = m1.oz-m2.h1z 
    rzm = rz - lz*round(rz/lz)
    rm1om2h1 = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qh*qo)/rm1om2h1

    # m1 o with m2 0
    rx = m1.ox-m2.ox   
    rxm = rx - lx*round(rx/lx)
    ry = m1.oy-m2.oy  
    rym = ry - ly*round(ry/ly)
    rz = m1.oz-m2.oz 
    rzm = rz - lz*round(rz/lz)
    rm1om2o = rxm**2 + rym**2 + rzm**2     # this
    e += (k*qo*qo)/rm1om2o

    e += A/(rm1om2o**6) 
    e -= B/(rm1om2o**3)

    return e


molecule_array = []
for i in particles:
    mole = Molecule(i[6],i[7],i[8],i[3],i[4],i[5],i[0],i[1],i[2])
    molecule_array.append(mole)
# print(len(molecule_array))

final_ans = 0
for index,val in enumerate(molecule_array):
    for index2 in range(index+1, len(molecule_array)):
        if(index2!=index):
            final_ans +=get_r2(val,molecule_array[index2])
        
print(final_ans)
