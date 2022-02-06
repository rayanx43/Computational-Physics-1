#Kuranage R R Ranasinghe
#Logistic Map

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
from copy import deepcopy
import random

#no. of iterations
N = 201

"""
As usual, the functions for the three different maps
were defined.
"""

def logistic_map(x0, r):
    
    x = np.zeros(N)
    x[0] = x0
    #Equation for the logistic map
    for n in range (N-1):
        x[n+1] = 4*r*x[n]*(1-x[n])

    return x    

def exp_func(x0, r):
    
    x = np.zeros(N)
    x[0] = x0
    #Equation for the exponential function
    for n in range (N-1):
        x[n+1] = x[n]*np.exp(4*r*(1-x[n]))

    return x  

def sin_func(x0, r):
    
    x = np.zeros(N)
    x[0] = x0
    #Equation for the sine function
    for n in range (N-1):
        x[n+1] = r*np.sin(np.pi*x[n])

    return x       

"""
The function below first computes the derivatives
of the generated map array passed into the function
from one of the functions above.
Next, the sum of the derivaties is calculated and then
divided by the size of the derivative array to get
the Lyapunov value, which is returned.
"""

def Lyapunov(map_arr, r):
    y = 4*r*(1-(2*map_arr))
    for i in range (N-1):
        sum = 0
        sum += np.log(abs(y[i]))
    val = sum/N

    return val


with PdfPages('6D.pdf') as pdf:
    
    """
    K is the number of r values considered
    in the range of 0.4 to 1.0.
    rr is the linspace created for those
    values of r.
    m is an empty array which we will fill
    with the calculated Lyapunov's values.
    """

    K = 300
    rr = np.linspace(0.4,1,K)
    m = np.zeros(K)

    """
    Below are set of plots generated.
    The for loops calculate a Lyapunov
    value for each logistic map when r
    is incremented and stores this value
    in m.
    Then, m is plotted against rr.
    """

    for i in range (K):
        n = logistic_map(0.8,rr[i])
        m[i] = Lyapunov(n,rr[i])
    plt.plot(rr,m,color="blue")
    plt.xlabel('r')
    plt.ylabel('Lyapunov exponent (lambda)')
    plt.title('For logistic map')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    for i in range (K):
        n = exp_func(0.8,rr[i])
        m[i] = Lyapunov(n,rr[i])
    plt.plot(rr,m,color="red")
    plt.xlabel('r')
    plt.ylabel('Lyapunov exponent (lambda)')
    plt.title('For exponential function')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    for i in range (K):
        n = sin_func(0.8,rr[i])
        m[i] = Lyapunov(n,rr[i])
    plt.plot(rr,m,color="green")
    plt.xlabel('r')
    plt.ylabel('Lyapunov exponent (lambda)')
    plt.title('For sine function')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    