initial configuration is stored in **initial.xyz**

Optimised configuration is stored in **optimal.xyz**

The potential energy obtained with each step is printed, with the step number.

The optimized potential energy is printed to screen

Hessian matrix is stored in **hessian.txt**

the eigenvalues and vectors are stored in **eigen.txt**

SI units have been used for everything.


# Report

## Question 1
Here, we generate particles at random locations, and make sure that no two particles have a distance less than 3.4A between them. WHen we have enough particles we store them in an array.

## Question 2

We find the potential energy of the system by calculating interactions between every pair of molecules, and then using the Lennard-Jones potential to find the value of the potential.

This is the formula we use
$$
U_{LJ} (r_{ij}) = 4\epsilon[(\frac\sigma{r_{ij}})^12 - (\frac\sigma{r_{ij}})^6]
$$


## Question 3

To decrease the potential of the system, we find the force acting on each particle and then step by step move the particles in the direction of the force. This results in a new configuration, to which we apply the same step. We do this until the change in potential energy we get from an iteration is very small.

The find the force on a particle, we differentiate the formula of the potential, and we use the new formula to find the force. We have to find the force on a certain particle by every other particle in the system, and sum up all these forces to find the final net force acting on that one particle.


## Question 4
For each element in the Hessian Matrix, we calculate the double derivative of the potential as described in class.  
$$
H_{ij} = \frac{\part U_{ij}}{\part{n_l}\part{m_k}}
$$
Here, n and m correspond to either x, y, or z depending on the values of i and j. l and k correspond to which atom we are referring to.

We then use `np.linalg.eig()` to get the eigenvalues and eigenvectors of the Hessian Matrix which are outputted in a separate file.

# External Libraries:

- Numpy