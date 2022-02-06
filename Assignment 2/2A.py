#Kuranage R R Ranasinghe
#Solar System (Earth was chosen as the planet)

import numpy as np
import matplotlib.pyplot as mp
import scipy as sp
from matplotlib.backends.backend_pdf import PdfPages

#initializing variables
mass = 1.989 * 10**30            #mass of sun
mass2 = 6.01 * 10**24            #mass of Earth
G = 6.67 * 10**-11               #Gravitational constant
r = 1.469 * 10**11               #distance from Earth to sun
vy_int = np.sqrt((G*mass)/r)  
vx_int = 0        
x_int = r           
y_int = 0
KE_int = 0.5*mass2*(vx_int**2+vy_int**2)
PE_int = (-G * mass * mass2)/(np.sqrt(x_int**2+y_int**2))
TE_int = KE_int + PE_int
t_min = 0
t_max = 1*365*24*60*60           #1 year (for earth)

step = 60                        #time step of one minitue
t = np.linspace(t_min,t_max,int((t_max-t_min)/step))
#initializing arrays
x_list = []
y_list = []
vx_list = []
vy_list = []
vx = vx_int
vy = vy_int
x = x_int
y = y_int
KE_list =[]
PE_list =[]
TE_list = []
KE = KE_int
PE = PE_int
TE = TE_int



for i in t:
    r = np.sqrt(x**2+y**2)         #distance between earth and sun
    F = - ((G*mass*mass2)/r**2)    #calculating force between earth and sun
    a = F/mass2 
    #calculation of acceleration components
    ax = a * x/r                   
    ay = a * y/r
    #Euler integrations
    vx = vx + step*ax
    vy = vy + step*ay

    #calculating kinetic energy (KE)
    KE = 0.5 * mass2 * (vx**2 + vy**2)

    x = x + (step*vx)
    y = y + (step*vy)

    #calculating potential energy (PE)
    PE = (-G * mass *mass2) / (np.sqrt(x**2+y**2)) 

    #calculating total energy (TE)
    TE = KE + PE

    #filling up our arrays
    vx_list.append(vx)
    vy_list.append(vy)
    x_list.append(x)
    y_list.append(y)
    KE_list.append(KE)
    PE_list.append(PE)
    TE_list.append(TE)
    
    
with PdfPages('2A.pdf') as pdf:
    mp.plot(t,vx_list, color="blue", label='X-Velocity')
    mp.plot(t,vy_list, color="red", label='Y-Velocity')
    mp.xlabel('Time(s)')
    mp.ylabel('Velocity(m/s)')
    mp.title('Velocity of the Earth')
    mp.legend()
    #mp.show()
    pdf.savefig()  # saves the current figure into a pdf page
    mp.close()

    mp.plot(t,x_list, color="blue", label='X-Displacement')
    mp.plot(t,y_list, color="red", label='Y-Displacement')
    mp.xlabel('Time(s)')
    mp.ylabel('Displacement(m)')
    mp.title('Position of the Earth')
    mp.legend()
    #mp.show()
    pdf.savefig()  # saves the current figure into a pdf page
    mp.close()

    mp.plot(x_list,y_list, color="green", label='Trajectory')
    mp.xlabel('x-displacement')
    mp.ylabel('y-displacement')
    mp.title('Trajectory of Earth aorund Sun for 365 days in 2 Dimensions')
    mp.legend()
    #mp.show()
    pdf.savefig()  # saves the current figure into a pdf page
    mp.close()

    mp.plot(t,KE_list, color="red", label='Kinetic Energy')
    mp.plot(t,PE_list, color="blue", label='Potential Energy')
    mp.plot(t,TE_list, color="black", label='Total Energy')
    mp.xlabel('Time(s)')
    mp.ylabel('Energy(J)')
    mp.title('Energy Plot')
    mp.legend()
    #mp.show()
    pdf.savefig()  # saves the current figure into a pdf page
    mp.close()


    
