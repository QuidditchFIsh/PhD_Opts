with open('data2.txt') as f:
    data2 = f.read().splitlines()
with open('data3.txt') as f:
    data3 = f.read().splitlines()
with open('data4.txt') as f:
    data4 = f.read().splitlines()

freq2 = []
freq3 = []
freq4 = []

for i in data2:
    freq2.append(float(i))
for i in data3:
    freq3.append(float(i))
for i in data4:
    freq4.append(float(i))

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

#print(output2.index(3.552713678800501e-15))
#print(output3.index(0.5999999999999979))

print("Min 2 Body Difference:" + str(min(output2)))
print("Min 3 Body Difference:" + str(min(output3)))
print("Min 4 Body Difference:" + str(min(output4)))






