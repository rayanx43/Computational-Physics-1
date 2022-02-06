#Kuranage R R Ranasinghe
#Burgers’ equation

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
from copy import deepcopy
import random

#Declaration of initial variables 
N = 100   
c = 1.
dx = 1./N 
beta = 0.8
#beta = c*dt/dx
dt = beta*dx/c 
print(dt)
T_final = 0.1
n = int(T_final/dt)
print(n)

#Defining arrays for initial data and solution
u0 = [] 
xx = [] 
u = np.zeros((N+1),float)
plt.figure(0)

#Plotting the initial solution
def plotIniExac():
    for i in range(0, N):
        x = i*dx
        xx.append(x)
        #Sinusiodal initial data with given parameters
        u0.append(3*np.sin(3.2*(x)))  
    plt.plot(xx, u0, 'b')
plotIniExac()

#Lax Wendroff solution
def numerical():                  
    for j in range (0, n):        #loop for time
        for i in range (0, N-2):  #Loop for x

            #Equation for Lax Wendroff method
            u[i+1] = u0[i+1] - ((beta/4)*(((u0[i+2])**2)-((u0[i])**2))) + (beta**2/8)*(u0[i+2] - u0[i+1])*(((u0[i+2])**2)-((u0[i])**2)) - (beta**2/8)*(u0[i+1] - u0[i])*(((u0[i+1])**2)-((u0[i])**2))

            #Boundary conditions incorporated
            u[0] = 0.
            u[N-1] = 0.
            u0[i] = u[i]
        plt.plot(xx, u[:-1], 'g')
numerical()

plt.title('Initial wave in blue, numerical solution in green')
plt.xlabel('x')
plt.show()