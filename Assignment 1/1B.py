#Kuranage R R Ranasinghe
#Harmonic Oscillator

import numpy as np
import matplotlib.pyplot as mp
from matplotlib.backends.backend_pdf import PdfPages

#initializing variables and arrays
mass = 1
k = 1               #spring constant
v_int = 0           #initial velocity
x_int = 5           #initial position
g = 9.81            #gravitational constant
step = 0.5          #time step
t = np.linspace(0,100,int(100/step))
y = [0]*len(t)
v_list = []
a_list = [] 
v = 0
x = x_int
j = 0

for i in t:
    #positive acceleration is assumed to act downwards
    a = - ((k*x)/mass)           #equation for acceleration
    v =  v + (step*a)            #Euler method for velocity
    x  = x + (step*v)            #Euler method for height
    y[j] = x
    j = j + 1
    v_list.append(v)
    a_list.append(a)

anal_solution = x_int*np.cos(k/mass * t)   

error = anal_solution - y

with PdfPages('1B.pdf') as pdf:
    mp.plot(t,y, color="blue", label='Numerical Solution')
    mp.plot(t,anal_solution, color="red", label='Analytical solution')
    mp.xlabel('Time')
    mp.ylabel('Height')
    mp.title('Height')
    mp.legend()
    #mp.show()
    pdf.savefig()  # saves the current figure into a pdf page
    mp.close()

    mp.plot(t,v_list,label='Second Line')
    mp.xlabel('Time')
    mp.ylabel('Velocity')
    mp.title('Velocity')
    mp.legend()
    pdf.savefig()
    mp.close()

    mp.plot(t,a_list,label='Third Line')
    mp.xlabel('Time')
    mp.ylabel('Acceleration')
    mp.title('Acceleration')
    mp.legend()
    pdf.savefig()
    mp.close()

    mp.plot(t,error,label='Fourth Line')
    mp.xlabel('Time')
    mp.ylabel('Error')
    mp.title('Numerical Error')
    mp.legend()
    pdf.savefig()
    mp.close()
