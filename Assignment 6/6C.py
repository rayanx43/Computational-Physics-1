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
    
    x = np.zeros(N)
    x[0] = x0

    """
    As per usual, the original function for
    the logistic map was defined.
    """

    for n in range (N-1):
        x[n+1] = 4*r*x[n]*(1-x[n])

    return x    

with PdfPages('6C.pdf') as pdf:

    """
    First, two arrays of the same logistic map
    with the same r value but different initial
    x values were obtained.
    Next, adhering to the equation given in the
    question, an array c was obtained which
    corresponded to the logarithm of the
    absolute values of the difference between the
    two arrays divided by a constant. This array
    was then plotted against n as usual.
    """

    a = logistic_map(0.6,0.92)
    b = logistic_map(0.60001,0.92)
    c = np.log(abs((a-b)/1e-5))
    x = np.linspace(0,N-1,N)
    #plt.plot(x,a,color="blue")
    #plt.plot(x,b,color="red")
    plt.plot(x,c,color="green")
    plt.xlabel('n')
    plt.ylabel('ln|del_xn/del_x0|')
    plt.title('Difference between 2 trajectories')
    #plt.legend()
    #plt.show()
    pdf.savefig() 
    plt.close()

    