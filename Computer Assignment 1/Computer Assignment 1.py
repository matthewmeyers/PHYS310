# Matt Meyers, PHYS 310-010

import numpy as np
import math
import matplotlib.pyplot as plt

# Part A
Number_Oscillators_A = 200
Number_Oscillators_B = 100
Total_Energy = 100

Q=100

data = np.zeros(shape=[101, 5])

for i in range(0, 101):
    data[i, 0] = i
    data[i, 2] = 100 - i
    data[i, 1] = round((math.factorial((data[i, 0] + Number_Oscillators_A - 1))) / \
                 ((math.factorial(data[i, 0]))*(math.factorial(Number_Oscillators_A - 1))),1)
    data[i, 3] = round((math.factorial((data[i, 2] + Number_Oscillators_B - 1))) / \
                 ((math.factorial(data[i, 2]))*(math.factorial(Number_Oscillators_B - 1))),1)
    data[i, 4] = round(data[i, 1] * data[i, 3],1)

print("q_a\t\t\t Omega_a\t\t q_b\t\t Omega_b\t\t Omega_tot")
for i in range(0,101):
    print(data[i,0],"\t\t","{:.2e}".format(data[i,1]),"\t\t",data[i,2],"\t\t","{:.2e}".format(data[i,3]),
          "\t\t","{:.2e}".format(data[i,4]),"\t\t")

for i in range(0,101):
    x = []
    x = list.append(str(data[i,0]))
    y = []
    y = list.append([data[i,4]])

#plt.plot(x,y)
#plt.show()


#entropy =
