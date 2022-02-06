#Kuranage R R Ranasinghe
#Potential within a rectangular region: the Jacobi with a grid size = 0.5

import numpy as np
import matplotlib.pyplot as mp
import math
import scipy as sp
from matplotlib.backends.backend_pdf import PdfPages
from copy import deepcopy

#declaring variables
Lx = 11
Ly = 21
x = (2*Lx) + (2)
y = (2*Ly) + (2)

#setting up matrices with boundary conditions
V = np.full((x,y),2.00)

V[1:-1,1:-1] = 0.00 # naive guess which gives 1875 iterations
#1.80 gives us 1492 iterations
#1.90 gives us 1377 iterations

R = deepcopy(V) #copying

#V is our old matrix with a guess
#R is the new matrix which is initially a copy of V

#declaring variables for convergence
sumv = sumr = 0.00
count = 0
converge = False

while converge == False:
    #incrementing to find iterations
    count = count + 1

    for i in range(1,x-1):
        for j in range(1,y-1):
            #implementing Jacobi
            R[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

    #computing new sum for testing convergence        
    for i in range(1,x-1):
        for j in range(1,y-1):
            sumr = sumr + abs(R[i,j] - V[i,j]) 

    #convergence measure
    #will only become true after the appropriate precision has been achieved
    converge = math.isclose(sumr,sumv,abs_tol=1e-4)  
    #for the next comparison in the while loop
    sumv = sumr    
    #for next step of the Jacobi  
    V = deepcopy(R)

print(V)
print("number of iterations=", count)    

