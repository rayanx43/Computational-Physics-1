#Kuranage R R Ranasinghe
#Falling Body

import numpy as np
import matplotlib.pyplot as mp
import scipy as sp
from matplotlib.backends.backend_pdf import PdfPages

#initializing variables
mass = 50
k = 10**(-4)        #drag constant
height = -5000      #initial height
g = 9.81            #gravitational constant
step = 0.00001      #time step

#building an array
t = np.linspace(0,35,int(35/step))

y = [0]*len(t)          #initializing arrays
v_list=[]
a_list=[]
v = 0                   #initial velocity at 5000m 
temp_y = height        #initial height is negative
i=0
j=0

for x in t:
    #positive acceleration is assumed to act downwards
    a = g - ((k*v**(2))/mass)    #equation for acceleration
    v =  v + (step*a)            #Euler method for velocity
    temp_y = temp_y + (step*v)   #Euler method for height
    if temp_y >= 0:
        v = 0
    y[i] = -temp_y
    i = i + 1
    v_list.append(v)
    a_list.append(a)


with PdfPages('1A.pdf') as pdf:
    mp.plot(t,y, color='blue', label='Numerical solution')
    mp.xlabel('Time')
    mp.ylabel('Height')
    mp.title('Height')
    mp.legend()
    #mp.show()
    pdf.savefig()  # saves the current figure into a pdf page
    mp.close()

    mp.plot(t,v_list, color='blue', label='Second Line')
    mp.xlabel('Time')
    mp.ylabel('Velocity')
    mp.title('Velocity')
    mp.legend()
    pdf.savefig()
    mp.close()

    mp.plot(t,a_list, color='blue', label='Third Line')
    mp.xlabel('Time')
    mp.ylabel('Acceleration')
    mp.title('Acceleration')
    mp.legend()
    pdf.savefig()
    mp.close()

