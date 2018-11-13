from matplotlib import pyplot as plt
import numpy as np

F1 = 12.67
F2 = 13.72
F3 = 3.17
F4 = 4.22


two_body = []
four_body = []
three_body = []

two_body.append(abs(float(F1 - F2)))
two_body.append(abs(float(F1 - F3)))
two_body.append(abs(float(F1 - F4)))
two_body.append(abs(float(F2 - F3)))
two_body.append(abs(float(F2 - F4)))
two_body.append(abs(float(F3 - F4)))

two_body.append(abs(float(F1 + F2)))
two_body.append(abs(float(F1 + F3)))
two_body.append(abs(float(F1 + F4)))
two_body.append(abs(float(F2 + F3)))
two_body.append(abs(float(F2 + F4)))
two_body.append(abs(float(F3 + F4)))

three_body.append(abs(float(F1 + F2 + F4)))
three_body.append(abs(float(F1 + F2 - F4)))
three_body.append(abs(float(F1 - F2 + F4)))
three_body.append(abs(float(F1 - F2 - F4)))

three_body.append(abs(float(F4 + F2 + F3)))
three_body.append(abs(float(F4 + F2 - F3)))
three_body.append(abs(float(F4 - F2 + F3)))
three_body.append(abs(float(F4 - F2 - F3)))

three_body.append(abs(float(F1 + F4 + F3)))
three_body.append(abs(float(F1 + F4 - F3)))
three_body.append(abs(float(F1 - F4 + F3)))
three_body.append(abs(float(F1 - F4 - F3)))

four_body.append(abs(float(F1 + F2 + F3 + F4)))
four_body.append(abs(float(F1 + F2 - F3 - F4)))
four_body.append(abs(float(F1 - F2 + F3 - F4)))
four_body.append(abs(float(F1 - F2 - F3 + F4)))
four_body.append(abs(float(F1 + F2 + F3 - F4)))
four_body.append(abs(float(F1 + F2 - F3 + F4)))
four_body.append(abs(float(F1 - F2 + F3 + F4)))
four_body.append(abs(float(F1 - F2 - F3 - F4)))

print(two_body)
print(four_body)

test1= []
test2 = []
for i in two_body:
    test1.append(1)
for i in three_body:
    test2.append(1.1)

fig,ax = plt.subplots()
ax.scatter(test1,two_body)
ax.scatter(test2,three_body)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='major',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
plt.show()
'''

Geb_b30 = [11, 10, 12, 14, 16, 19, 17, 14, 18, 17]
years_b30 = range(2008,2018)
Geb_a30 = [12, 10, 13, 14, 12, 13, 18, 16]
years_a30 = range(2010,2018)

fig, ax = plt.subplots()
ax.plot(years_b30, Geb_b30, label='Prices 2008-2018', color='blue')
ax.plot(years_a30, Geb_a30, label='Prices 2010-2018', color = 'red')
legend = ax.legend(loc='center right', fontsize='x-large')
plt.xlabel('years')
plt.ylabel('prices')
plt.title('Comparison of the different prices')
plt.show()

'''