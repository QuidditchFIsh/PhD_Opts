'''
Author: Aneirin John Baker
Date:14/11/18
Description:Optimiation procudure to find the optimal frequencies and hence parameters to use
in the simulation. Using Scipy optimization packages.
Will optimise against the 10 frequencies within the register along with the rest of the frequencies making
sure that they are sufficently detuned from the other parameters (by measure of the perturbations).
Will then look to compose a list of paraterers which will produce these frequencis by a list search method.
'''

import numpy as np
from scipy.optimize import minimize

########################################Variables########################################
opt_freq = []
frequencies = []
Capaticance = []
Josephson_Energy = []
Strength = []

opt_str = []
temp = []

full_opt_freq = []

x0 = [3,3,3,3]

########################################Contraint Functions########################################
def constraint1(x):
#Constraint to check that the frequecnies are sufficently detuned from one another.
    x1 = abs(x[0]-x[1])
    x2 = abs(x[0]-x[2])
    x3 = abs(x[0]-x[3])
    x4 = abs(x[1]-x[2])
    x5 = abs(x[1]-x[3])
    x6 = abs(x[2]-x[3])
    return min(x1,x2,x3,x4,x5,x6) - 0.7

def constraint2(x):
    two_min = min(two_body_opt(x))
    three_min = min(three_body_opt(x))
    
    if two_min>three_min:
        return three_min - 1
    else:
        return two_min - 1

########################################Optimization Functions########################################
def two_body_opt(x):
    two_bdy = []

    two_bdy.append(abs(x[1] - x[2]))
    two_bdy.append(abs(x[1] - x[2]))

    two_bdy.append(abs(x[0] - x[2]))
    two_bdy.append(abs(x[0] - x[2]))

    two_bdy.append(abs(x[0] - x[1]))
    two_bdy.append(abs(x[0] - x[1]))

    return two_bdy
def three_body_opt(x):
    three_bdy = []

    three_bdy.append(abs(x[0] + x[1] + x[2]))
    three_bdy.append(abs(x[0] + x[1] - x[2]))
    three_bdy.append(abs(x[0] - x[1] + x[2]))
    three_bdy.append(abs(x[0] - x[1] - x[2]))

    return three_bdy

# Define function to be optimized
def Opt_fun(x):

    two = two_body_opt(x)
    three = three_body_opt(x)

    min = 1000
    for i in two:
        for j in three:
            if(abs(i-j) < min):
                min = abs(i-j)

    return  min * -1

def full_difference(x0):

    two_body = []
    three_body = []

    F1 = x0[0]
    F2 = x0[1]
    F3 = x0[2]
    F4 = x0[3]

    two_body.append(float(F1-F2))
    two_body.append(float(F1-F3))
    two_body.append(float(F1-F4))
    two_body.append(float(F2-F3))
    two_body.append(float(F2-F4))
    two_body.append(float(F3-F4))

    two_body.append(float(F1+F2))
    two_body.append(float(F1+F3))
    two_body.append(float(F1+F4))
    two_body.append(float(F2+F3))
    two_body.append(float(F2+F4))
    two_body.append(float(F3+F4))

    three_body.append(float(F1 + F2 + F3))
    three_body.append(float(F1 + F2 - F3))
    three_body.append(float(F1 - F2 + F3))
    three_body.append(float(F1 - F2 - F3))

    three_body.append(float(F1 + F2 + F4))
    three_body.append(float(F1 + F2 - F4))
    three_body.append(float(F1 - F2 + F4))
    three_body.append(float(F1 - F2 - F4))

    three_body.append(float(F4 + F2 + F3))
    three_body.append(float(F4 + F2 - F3))
    three_body.append(float(F4 - F2 + F3))
    three_body.append(float(F4 - F2 - F3))

    three_body.append(float(F1 + F4 + F3))
    three_body.append(float(F1 + F4 - F3))
    three_body.append(float(F1 - F4 + F3))
    three_body.append(float(F1 - F4 - F3))

    min = 1000

    for i in two_body:
        for j in three_body:
            if(abs(i-j) < min):
                min = abs(i-j)
    return min

#Define the parameters whcih will be used

bnd = [3,28]
bounds = [bnd,bnd,bnd,bnd]

con1 = {'type' : 'ineq' , 'fun' : constraint1}
con2 = {'type' : 'ineq' , 'fun' : constraint2}

cons = [con1,con2]

for i in range(0,7):
    for j in range(0,7):
        for k in range(0,7):
            for l in range(0,7):
                x = [x0[0] + i,x0[1] + j , x0[2] + k,x0[3] + l]
                if(x[1] != x[0] and x[2] != x[3]):
                    sol = minimize(Opt_fun,x,method='SLSQP',bounds=bounds,constraints = cons)
                    opt_freq.append(sol.x)

'''
Now we have the optimized frequencies we can now find which one of these will give the best distance between the freq

will now need to optmize for the full frequencies 
then will need to work out some way of presenting this data you could graph the different frequencies with the important freq as a different colour
which would highlight how they difer from the other freq. Howere it would be good to come up with some metric for this so that we can have a measure 
of what the best solution to this is. Potentially we could include the strengths of the ints.
'''


########################################Printing out the data########################################
with open('Frequency_Data.txt') as f:
    for line in f:
        line = line.strip().split()
        frequencies.append(float(line[2]))
        Capaticance.append(float(line[1]))
        Josephson_Energy.append(float(line[0]))
        Strength.append(float(line[3]))

for i in opt_freq:
    Index0 = [k for k, _ in enumerate(frequencies) if np.isclose(_, i[0], 0.001)]
    Index1 = [k for k, _ in enumerate(frequencies) if np.isclose(_, i[1], 0.001)]
    Index2 = [k for k, _ in enumerate(frequencies) if np.isclose(_, i[2], 0.001)]
    Index3 = [k for k, _ in enumerate(frequencies) if np.isclose(_, i[3], 0.001)]
    filename = "Freq_out/Frequencies " + str(round(i[0],3)) + "," + str(round(i[1],3)) + "," + str(round(i[2],3)) + "," \
               + str(round(i[3],3)) + ".dat"
    with open(filename, "w") as f:
        f.write("[" + str(round(i[0],4)) + "," + str(round(i[1],4)) + "," + str(round(i[2],4)) + "," + str(round(i[3],4)) + "]\n")
        f.write(str(i[0]) + "\n")
        for j in range(0,len(Index0)):
            f.write("\t" + str(Capaticance[Index0[j]]) + " "
                    + str(Josephson_Energy[Index0[j]]) + " " + str(frequencies[Index0[j]]) + " " + str(Strength[Index0[j]]) + "\n")
        f.write(str(i[1]) + "\n")
        for j in range(0,len(Index1)):
            f.write("\t" + str(Capaticance[Index1[j]]) + " "
                    + str(Josephson_Energy[Index1[j]]) + " " + str(frequencies[Index1[j]]) + " " + str(Strength[Index1[j]]) + "\n")
        f.write(str(i[2]) + "\n")
        for j in range(0,len(Index2)):
            f.write("\t" + str(Capaticance[Index2[j]]) + " "
                    + str(Josephson_Energy[Index2[j]]) + " " + str(frequencies[Index2[j]])+ " " + str(Strength[Index2[j]]) + "\n")
        f.write(str(i[3]) + "\n")
        for j in range(0,len(Index3)):
            f.write("\t" + str(Capaticance[Index3[j]]) + " "
                    + str(Josephson_Energy[Index3[j]]) + " " + str(frequencies[Index3[j]])+ " " + str(Strength[Index3[j]]) + "\n")
