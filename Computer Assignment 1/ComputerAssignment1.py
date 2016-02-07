# Matt Meyers, PHYS 309-010

import numpy as np
import matplotlib.pyplot as plt
import math

# Assigning constants for number of oscillators and total energy
N_A = 200
N_B = 100
Q = 100

# Putting macrostates for a and b into lists
q_a = np.arange(0, Q + 1)
q_b = Q - q_a

# Calculating omega for a and b and assigning these values to lists
omegaA = np.empty(shape=[Q + 1])
for i in range(0, Q + 1):
    omegaA[i] = (math.factorial(q_a[i] + N_A - 1)) / (math.factorial(q_a[i]) * math.factorial(N_A - 1))

omegaB = np.empty(shape=[Q + 1])
for i in range(0, Q + 1):
    omegaB[i] = (math.factorial(q_b[i] + N_B - 1)) / (math.factorial(q_b[i]) * math.factorial(N_B - 1))

# Omega total is the product of omega_a and omega_b
omegaTot = omegaA * omegaB

#Printing table for testing
for i in range(0,Q +1):
    print(q_a[i],"\t","{:.2e}".format(omegaA[i]),"\t",q_b[i],"\t",
          "{:.2e}".format(omegaB[i]),"\t","{:.2e}".format(omegaTot[i]))

# Plotting Omega_total versus number of macrostates for a
plt.plot(q_a, omegaTot)
plt.rc('text', usetex=True)
plt.xlabel(r"$q_A$")
plt.ylabel(r"$\Omega_{total}$")
plt.savefig("MicrostatesPlot.png")
plt.show()

# The most probable macrostate would be q_a = 67.  The probability of this would be the following.
mostProbable = omegaTot[67] / sum(omegaTot)
print("{:.2e}".format(mostProbable))

# The least probable macrostate would be q_a = 0.  The probability of this would be the following.
leastProbable = omegaTot[0] / sum(omegaTot)
print("{:.2e}".format(leastProbable))

# Calculating entropy for a and b.  Then saving these values to lists  in terms of Boltzmann's constant, the entropy is
# the natural log of the number of microstates.
s_a = np.empty(shape=[Q + 1])
for i in range(0, Q + 1):
    s_a[i] = math.log(omegaA[i])
s_b = np.empty(shape=[Q + 1])
for i in range(0, Q + 1):
    s_b[i] = math.log(omegaB[i])
s_tot = np.empty(shape=[Q + 1])
for i in range(0, Q + 1):
    s_tot[i] = math.log(omegaTot[i])

# Plotting the entropies against the number of macrostates for a. A is the red curve, B is blue, and the total is green.
plt.plot(q_a, s_a, 'r', q_a, s_b, 'b', q_a, s_tot, 'g')
plt.rc('text', usetex=True)
plt.xlabel(r"$q_A$")
plt.ylabel(r"Entropy ($S/k$)")
plt.savefig("EntropyPlot.png")
plt.show()

# Formatting the data for omega and writing to a text file.
file = open("MicrostateTable.txt", "w")
for i in range(0,102):
    if i == 0:
        file.write("q_a\tomega_a\t\tq_b\tomega_b\t\tomega_tot")
        file.write("\n")
    else:
        file.write(str(q_a[i-1])+"\t"+str("{:.2e}".format(omegaA[i-1]))+"\t"+str(q_b[i-1])+"\t"+
                   str("{:.2e}".format(omegaB[i-1]))+"\t"+str("{:.2e}".format(omegaTot[i-1])))
        file.write("\n")

# Formatting the entropy data and printing to a text file.
file = open("EntropyTable.txt", "w")
for i in range(0,102):
    if i == 0:
        file.write("q_a\tomega_a\t\tS_a/k\tq_b\tomega_b\t\tS_b/k\t\tomega_tot\tS_tot/k")
        file.write("\n")
    else:
        file.write(str(q_a[i-1])+"\t"+str("{:.2e}".format(omegaA[i-1]))+"\t"+str("{:.2f}".format(s_a[i-1]))
                   +"\t"+str(q_b[i-1])+"\t"+str("{:.2e}".format(omegaB[i-1]))+"\t"+str("{:.2f}".format(s_b[i-1]))+"\t\t"
                   +str("{:.2e}".format(omegaTot[i-1]))+"\t"+str("{:.2f}".format(s_tot[i-1])))
        file.write("\n")
