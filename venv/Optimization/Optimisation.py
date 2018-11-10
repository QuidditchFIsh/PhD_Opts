'''
Short script to optimise the frequencies

Turning into longer script look to maybe port to C++ if this gets slow in finding parameter space.
'''
import numpy as np
from scipy.optimize import minimize

F1 = 13.8
F2 = 13.1
F3 = 3.00
F4 = 4.15

def constraint1(x):
    return abs(x[0]- x[1] + x[2] - x[3]) - 0.1
def constraint2(x):
    return abs(x[0]- x[1] - x[2] - x[3]) - 0.1
def constraint3(x):
    x1 = abs(x[0]-x[1])
    x2 = abs(x[0]-x[2])
    x3 = abs(x[0]-x[3])
    x4 = abs(x[1]-x[2])
    x5 = abs(x[1]-x[3])
    x6 = abs(x[2]-x[3])
    return abs(min(x1,x2,x3,x4,x5,x6)) - 0.6

def difference(x0):

    two_body = []
    three_body = []
    four_body = []

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

    four_body.append(float(F1 + F2 + F3 + F4))
    four_body.append(float(F1 + F2 - F3 - F4))
    four_body.append(float(F1 - F2 + F3 - F4))
    four_body.append(float(F1 - F2 - F3 + F4))
    four_body.append(float(F1 + F2 + F3 - F4))
    four_body.append(float(F1 + F2 - F3 + F4))
    four_body.append(float(F1 - F2 + F3 + F4))
    four_body.append(float(F1 - F2 - F3 - F4))

    min = 1000

    for i in two_body:
        for j in three_body:
            if(abs(i-j) < min):
                min = abs(i-j)
        for j in four_body:
            if(abs(i-j) < min):
                min = abs(i-j)
    min1 = 1000
    for i in three_body:
        for j in four_body:
            if(abs(i-j) < min1):
                min1 = abs(i-j)
    return -1 * min
''' Setting the Bounds and Contraints '''
b1 = (10,30)
b2 = (3,5)
bnds =[b1,b1,b2,b2]

con1 = {'type': 'ineq', 'fun' : constraint1}
con2 = {'type': 'ineq', 'fun' : constraint2}
con3 = {'type': 'ineq', 'fun' : constraint3}

cons = [con1,con2,con3]

'''Opening a File for output '''
opt_out = open("Optimization_Output.dat","w")
opt_freq = []
opt_str = []

''' Initalising the loop and the inital conditions'''
x0 = [13,13,3,3]
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            for l in range(0,2):
                x = [x0[0] + i,x0[1] + j , x0[2] + k,x0[3] + l]
                if(x[1] != x[0] and x[2] != x[3]):
                    sol = minimize(difference,x,method='SLSQP',bounds=bnds,constraints=cons)
                    opt_out.write(str(round(sol.x[0],2)) + " " + str(round(sol.x[1],2)) + " " + str(round(sol.x[2],2) )
                            + " " + str(round(sol.x[3],2))+ " " + str(round(sol.fun,2) * -1) + "\n")
                    opt_freq.append([sol.x,sol.fun * -1])



