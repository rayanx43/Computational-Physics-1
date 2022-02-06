#Kuranage R R Ranasinghe
#One-dimensional cellular automata 

import numpy as np
import matplotlib.pyplot as mp
import math
from matplotlib.backends.backend_pdf import PdfPages
from copy import deepcopy
import random

#N = input("Enter the number of sites: ")

Ans = "P"

cycles = input("Enter number of cycles: ")

N = 100

#creating an array filled with 0s
data = [0]*100

#creating an array of size 12, filled with
#random numbers from 6 to 99, which will
#later correspond to the positions in the
#data array, where we will have 1s
r = random.sample(range(6,99), 48)
for i in range (48):
    data[r[i]] = 1
print("random position where we have 1s:", r)

#filling the first 6 positions of data with 1s
for i in range (6):
        data[i] = 1

print("original random data:", data)

#getting inputs considering neighbours
s = [0]*8
for i in range(8):
    s[i] = np.binary_repr(i, 3)
print("combinations possible for input: ", s)

 
rule_number = 184
rule_string = np.binary_repr(rule_number, 8)
rule = np.array([int(bit) for bit in rule_string])
print("rule applied to each combination in order: ", rule)

#new arrays to store output
a = np.empty(int(N), dtype=int)
b = np.empty(int(N), dtype=int)

#Iterating through array and updating
#x is the decimal number which is the
#result of a binary combnation
#x gives the position in the rule array

cycles = int(cycles)

if Ans == "F":
    print("generated array with finite bound: ")
    
    while cycles>0:
        for i in range (int(N)):
            if i==0:
                x = data[i]*2 + data[i+1]
            elif i==int(N)-1:
                x = data[i-1]*4 + data[i]*2
            else:
                x = data[i-1]*4 + data[i]*2 + data[i+1]
            a[i] = rule[x]

        print(a)

        for i in range (int(N)):
            data[i] = a[i]
        
        cycles = cycles - 1
    

elif Ans == "P": 
    data2 = np.empty(int(N)+2, dtype=int)

    print("generated array with periodic bound")

    for i in range(int(N)+2):
            if i == 0:
                data2[i] = data[int(N)-1]
            elif i == int(N)+1:
                data2[i] = data[0]
            else:
                data2[i] = data[i-1]

    while cycles>0:
        for i in range (1,int(N)+1):
            x = data2[i-1]*4 + data2[i]*2 + data2[i+1]
            b[i-1] = rule[x]

        print(b)

        for i in range (int(N)+2):
            if i == 0:
                data2[i] = b[int(N)-1]
            elif i == int(N)+1:
                data2[i] = b[0]
            else:
                data2[i] = b[i-1]

        cycles = cycles - 1
