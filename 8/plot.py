import numpy as np
import matplotlib.pyplot as plt

def solver(R0, F0, gamma, c, alpha, beta, K, t):


    R = np.zeros(len(t)) 
    F = np.zeros(len(t)) 

    R[0] = R0
    F[0] = F0

    for n in range(0,len(t)-1):
        dt = t[n+1] - t[n]
        R[n+1] = R[n]*(1 + gamma*dt - (gamma*dt*R[n])/K - alpha*dt*F[n])
        F[n+1] = F[n]*(1 - c*dt + beta*dt*R[n])
    return R,F
 
def main():

    var = 15
    t = np.linspace(0,var,var*1000) 

    gamma = 0.6
    c = 0.4
    alpha = 0.8
    beta = 0.1
    K = 50
    R0, F0 = 4, 6

    # Actually solve the problem
    R, F = solver(R0, F0, gamma, c, alpha, beta, K, t)

    # Plot the solution
    plt.plot(t,R,t,F)
    plt.legend(['Prey','Predator'])
    plt.grid(True)
    plt.title("Solution of Lotka-Volterra system using explicit Euler") 
    plt.show()

main()