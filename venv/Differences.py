'''
Quick script to find if any of the combinations of frequencies coincide with each other
'''

e = 1.60217662e-19
hbar = 1.054571800e-34
h = 6.626070040e-34
pi = 3.14159265359
L = 100e-9
phi0 = (hbar)/(2 * e)
#Energy of inductors
E_L = (phi0 ** 2) / (2 * L)

F1 = 13.8 #34Ghz 30C
F2 = 13.1 #31Ghz 31C
F3 = 3.45 #5Ghz 99C
F4 = 4.15 #5Ghz 73C

parameters = [[34,30],[31,31],[5,99],[5,73]]

three_body_combinations = [[1,2,3],[1,2,4],[2,3,4],[1,3,4]]
two_body_combinations = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

four_bdy = []
three_body1 = []
three_body2 = []
three_body3 = []
three_body4 = []

freq2 = []
freq3 = []
freq4 = []

for i in range(0,2):
    if(i == 0):
        sum1 = F1
    if(i == 1):
        sum1 = -F1
    for j in range(0,2):
        if (j == 0):
            sum2 = F2
        if (j == 1):
            sum2 = -F2
        for k in range(0,2):
            if (k == 0):
                sum3 = F3
            else:
                sum3 = -F3
            for l in range(0,2):
                if (l == 0):
                    sum4 = F4
                else:
                    sum4 = -F4

                temp = str(abs(sum1 + sum2 + sum3 + sum4))
                if any(temp in s for s in four_bdy):
                    print(" ")
                else:
                    four_bdy.append(str(abs(sum1 + sum2 + sum3 + sum4)))

                temp = str(abs(sum1 + sum2 + sum3))
                if any(temp in s for s in three_body1):
                    print(" ")
                else:
                    three_body1.append(str(abs(sum1 + sum2 + sum3)))

                temp = str(abs(sum1 + sum2 + sum4))
                if any(temp in s for s in three_body2):
                    print(" ")
                else:
                    three_body2.append(str(abs(sum1 + sum2 + sum4)))

                temp = str(abs(sum2 + sum3 + sum4))
                if any(temp in s for s in three_body3):
                    print(" ")
                else:
                    three_body3.append(str(abs(sum2 + sum3 + sum4)))

                temp = str(abs(sum1 + sum3 + sum4))
                if any(temp in s for s in three_body4):
                    print(" ")
                else:
                    three_body4.append(str(abs(sum1 + sum3 + sum4)))

file4 = open("data4.txt","w")
file3 = open("data3.txt","w")

for i in four_bdy:
    file4.write(i+ "\n")
    freq4.append(float(i))
for i in three_body1:
    file3.write(i + "\n")
    freq3.append(float(i))
for i in three_body2:
    file3.write(i+ "\n")
    freq3.append(float(i))
for i in three_body3:
    file3.write(i+ "\n")
    freq3.append(float(i))
for i in three_body4:
    file3.write(i+ "\n")
    freq3.append(float(i))

'''
phi_bar=[]
for i in parameters:
    Ej = i[0] * (1e9) * h
    C = i[1] * (1e-15)
    E_cq = (e ** 2) / (2 * C)
    phi_bar.append(((2 * E_cq) / (Ej + (8 * E_L))) ** 0.25)

print(phi_bar)
'''


file2 = open("data2.txt","w")
sum_plus  = 0
sum_minus = 0
two_body = []
for i in two_body_combinations:
    if(i[0] == 1):
        sum_minus += F1
        sum_plus  += F1
    if(i[0] == 2):
        sum_minus += F2
        sum_plus  += F2
    if(i[0] == 3):
        sum_minus += F3
        sum_plus  += F3
    if(i[0] == 4):
        sum_minus += F4
        sum_plus  += F4

    if(i[1] == 1):
        sum_minus -= F1
        sum_plus  += F1
    if(i[1] == 2):
        sum_minus -= F2
        sum_plus  += F2
    if(i[1] == 3):
        sum_minus -= F3
        sum_plus  += F3
    if(i[1] == 4):
        sum_minus -= F4
        sum_plus  += F4
    file2.write(str(sum_plus) + "\n" + str(sum_minus) + "\n")
    freq2.append(float(sum_plus))
    freq2.append(float(sum_minus))
    sum_minus = 0
    sum_plus  = 0

file = open("output.txt","w")

output2 = []
output3 = []
output4 = []

for i in freq2:
    for j in freq3:
        file.write(str(abs(i-j)) + "\n")
        output2.append(abs(i-j))
    for j in freq4:
        file.write(str(abs(i-j)) + "\n")
        output2.append(abs(i-j))
for i in freq3:
    for j in freq4:
        file.write(str(abs(i-j)) + "\n")
        output3.append(abs(i-j))
for i in freq4:
    for j in freq3:
        file.write(str(abs(i-j)) + "\n")
        output4.append(abs(i-j))

print("Min 2 Body Difference:" + str(min(output2)))
print("Min 3 Body Difference:" + str(min(output3)))
print("Min 4 Body Difference:" + str(min(output4)))










