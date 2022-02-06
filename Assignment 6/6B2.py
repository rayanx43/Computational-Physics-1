#Kuranage R R Ranasinghe
#Logistic Map

import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_pdf import PdfPages
from copy import deepcopy
import random


N = 201

def sin_func(x0, r):
    
    x = [0]*N
    x[0] = x0
    #Equation for the sine function
    for n in range (N-1):
        x[n+1] = r*np.sin(np.pi*x[n])

    return x    

with PdfPages('6B2.pdf') as pdf:
    a = sin_func(0.8,0.2)
    x = np.linspace(0,N-1,N)
    plt.plot(x,a,color="blue")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.8 and r=0.2')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    b = sin_func(0.8,0.4)
    x = np.linspace(0,N-1,N)
    plt.plot(x,b,color="red")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.8 and r=0.4')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    c = sin_func(0.1,0.73)
    x = np.linspace(0,N-1,N)
    plt.plot(x,c,color="green")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.1 and r=0.73')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    d = sin_func(0.09,0.88)
    x = np.linspace(0,N-1,N)
    plt.plot(x,d,color="violet")
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('x0=0.09 and r=0.88')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

