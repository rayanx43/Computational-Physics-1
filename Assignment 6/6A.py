#Kuranage R R Ranasinghe
#Logistic Map

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
from copy import deepcopy
import random


N = 201

def logistic_map(x0, r):
    
    x = [0]*N
    x[0] = x0
    #Equation for the logistic map
    for n in range (N-1):
        x[n+1] = 4*r*x[n]*(1-x[n])

    return x    

#For plotting the logistic maps with different conditions
with PdfPages('6A.pdf') as pdf:

    """
    The function was called for specific
    conditions and the results were
    plotted against n.      
    """

    a = logistic_map(0.8,0.2)
    x = np.linspace(0,N-1,N)
    plt.plot(x,a,color="blue")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.8 and r=0.2')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    b = logistic_map(0.8,0.4)
    x = np.linspace(0,N-1,N)
    plt.plot(x,b,color="red")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.8 and r=0.4')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    c = logistic_map(0.1,0.73)
    x = np.linspace(0,N-1,N)
    plt.plot(x,c,color="green")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.1 and r=0.73')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    d = logistic_map(0.09,0.88)
    x = np.linspace(0,N-1,N)
    plt.plot(x,d,color="violet")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.09 and r=0.88')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

