import numpy as np
import matplotlib.pyplot as plt


w = h = 5.

dx = dy = 0.1

Dx = 4.
Dy = 9.

Tcool, Thot = 0, 100000000000000

nx, ny = int(w/dx), int(h/dy)

dx2, dy2 = dx*dx, dy*dy
dt = dx2 * dy2 / ((Dx+Dy) * (dx2 + dy2))

u0 = Tcool * np.zeros((nx, ny))
u = u0.copy()


r, cx, cy = 0.3, w/2, h/2
r2 = r**2
for i in range(nx):
    for j in range(ny):
        p2 = (i*dx-cx)**2 + (j*dy-cy)**2
        if p2 < r2:
            u0[i,j] = Thot

def do_timestep(u0, u):

    u[1:-1, 1:-1] = u0[1:-1, 1:-1] + Dx * dt * ((u0[2:, 1:-1] - 2*u0[1:-1, 1:-1] + u0[:-2, 1:-1])/dx2) + Dy * dt *((u0[1:-1, 2:] - 2*u0[1:-1, 1:-1] + u0[1:-1, :-2])/dy2 )

    u0 = u.copy()
    return u0, u


nsteps = 10001

mfig = [10,100,1000, 10000]
fignum = 0
fig = plt.figure()
for m in range(nsteps):
    u0, u = do_timestep(u0, u)
    if m in mfig:
        fignum += 1
        print(m, fignum)
        ax = fig.add_subplot(220 + fignum)
        im = ax.imshow(u.copy(), cmap=plt.get_cmap('PuBu_r'), vmin=Tcool,vmax=Thot)
        ax.set_axis_off()
        ax.set_title('{:0.0f} timesteps'.format(m))
fig.subplots_adjust(right=0.85)
# PuBu_r
plt.show()