#Kuranage R R Ranasinghe
#Solar System (Earth was chosen as the planet)

import numpy as np
import matplotlib.pyplot as mp
import scipy as sp
from matplotlib.backends.backend_pdf import PdfPages

#initializing variables
mass = 1.989 * 10**30            #mass of sun
mass2 = 6.0 * 10**24             #mass of Earth
mass3 = 6.6 * 10**23             #mass of Mars (period = 1.88 Earth years)

G = 6.67 * 10**-11               #Gravitational constant
r = 1.469 * 10**11               #distance from Earth to sun
r2 = 2.4533 * 10**11             #distance from Mars to sun



#Planet Earth
vy_int = np.sqrt((G*mass)/r)  
vx_int = 0        
x_int = r           
y_int = 0
KE_int = 0.5*mass2*(vx_int**2+vy_int**2)
PE_int = (-G * mass * mass2)/(np.sqrt(x_int**2+y_int**2))
TE_int = KE_int + PE_int
t_min = 0
t_max = 2*365*24*60*60           #2 years (for earth)

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
    


#Planet Mars    
vy_intm = np.sqrt((G*mass)/r2)  
vx_intm = 0        
x_intm = r2           
y_intm = 0
KE_intm = 0.5*mass3*(vx_intm**2+vy_intm**2)
PE_intm = (-G * mass * mass3)/(np.sqrt(x_intm**2+y_intm**2))
TE_intm = KE_intm + PE_intm
t_minm = 0
t_maxm = 2*365*24*60*60           #2 years (for earth)

stepm = 60                        #time step of one minitue
tm = np.linspace(t_minm,t_maxm,int((t_maxm-t_minm)/stepm))
#initializing arrays
x_listm = []
y_listm = []
vx_listm = []
vy_listm = []
vxm = vx_intm
vym = vy_intm
xm = x_intm
ym = y_intm
KE_listm =[]
PE_listm =[]
TE_listm = []
KEm = KE_intm
PEm = PE_intm
TEm = TE_intm



for j in tm:
    r2 = np.sqrt(xm**2+ym**2)         #distance between earth and sun
    Fm = - ((G*mass*mass3)/r2**2)    #calculating force between mars and sun
    am = Fm/mass3 
    #calculation of acceleration components
    axm = am * xm/r2                   
    aym = am * ym/r2
    #Euler integrations
    vxm = vxm + stepm*axm
    vym = vym + stepm*aym

    #calculating kinetic energy (KE)
    KEm = 0.5 * mass3 * (vxm**2 + vym**2)

    xm = xm + (stepm*vxm)
    ym = ym + (stepm*vym)

    #calculating potential energy (PE)
    PEm = (-G * mass *mass3) / (np.sqrt(xm**2+ym**2)) 

    #calculating total energy (TE)
    TEm = KEm + PEm

    #filling up our arrays
    vx_listm.append(vxm)
    vy_listm.append(vym)
    x_listm.append(xm)
    y_listm.append(ym)
    KE_listm.append(KEm)
    PE_listm.append(PEm)
    TE_listm.append(TEm)

new_list = []
zip_object = zip(TE_list, TE_listm)
for TE_list_i, TE_listm_i in zip_object:
    new_list.append(TE_list_i-TE_listm_i)

with PdfPages('2B.pdf') as pdf:
    mp.plot(t,new_list, color="blue", label='Total Energy Difference')
    mp.xlabel('Time(s)')
    mp.ylabel('Total Energy Difference(J)')
    mp.title('Energy Plot')
    mp.legend()
    #mp.show()
    pdf.savefig()  # saves the current figure into a pdf page
    mp.close()

    


    
