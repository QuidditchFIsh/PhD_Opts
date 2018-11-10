
#Author: Aneirin J Baker
#Date: 15/10/2018
#Description:A short python script to calculate the freuqencies of qbits based on the equations and architecture in
#Sameti, M., Potočnik, A., Browne, D. E., Wallraff, A., & Hartmann, M. J. (2017).
#Superconducting quantum simulator for topological order and the toric code. Physical Review A, 95(4), 1–20.
#https://doi.org/10.1103/PhysRevA.95.042330

import math
import seaborn as sns
import matplotlib.pylab as plt
import numpy as np
############################# Define the Constants/Variables #############################

e = 1.60217662e-19
hbar = 1.054571800e-34
h = 6.626070040e-34
pi = 3.14159265359

# Now define the variables which can be
#tuned to fit the parameters we need

#Josephson Energy
Ej_bare = 5
Ej =  Ej_bare *(1e9) * h
#Inductance
L = 100e-9
#Capcatnance on qbit
C_bare = 55
C = C_bare * (1e-15)
#Quantum of flux
phi0 = (hbar)/(2 * e)
#Energy of inductors
E_L = (phi0 ** 2) / (2 * L)
#define varibales for each of the qbit frequencies
omega_1 = 0
phi_bar = 0

#Open a file to write to
file = open("Frequency_Data.txt","w")

############################# Calculations #############################

#define some lists for a heat map output
map_w = []
temp_w = []
map_phi = []
temp_phi = []

xticks = np.linspace(5,101,96)
yticks = np.linspace(50,81,31)

#Calculating useful energies
for i in range(1,100):
    for j in range(1,150):
        Ej = i * (1e9) * h
        C = j* (1e-15)
        E_cq = (e**2)/(2 * C)

        omega_1 = (1/(hbar * 2 * pi)) * math.sqrt(8 * E_cq *(Ej + (8*E_L))) * (1e-9)
        phi_bar = ((2*E_cq)/(Ej + (8 * E_L)))**0.25

        if(omega_1 > 2 and omega_1 < 30):
            temp_w.append(omega_1)
            temp_phi.append(phi_bar)
            file.write(str(i) + " " + str(j) + " " + str(omega_1) + " " + str(phi_bar) + "\n")
file.close()

############################# Heat map of results #############################


#ax = sns.heatmap(map_w)
#plt.title("Frequencies of Qbit in a 4 way configuration")
#plt.ylabel("E_J/h: Joesphson Energy/h (GHz)")
#plt.xlabel("C_q: Capitance of each Qbit (fF)")
#plt.show()


############################# Print out Results to file #############################

print("Cq: " + str(C * (1e15)) + " fF\n" +
      "L: " + str(L * (1e9)) + " nH\n" +
      "E_J: " + str((Ej/h) * 1e-9) + " GHz\n" +
      "Omega_1: " + str(omega_1) + " GHz")




