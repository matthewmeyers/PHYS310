# Matt Meyers PHYS 310-010 Computer Assignment 3

import random
import math
import matplotlib.pyplot as plt
import copy
import time

SIZE = 25
T = 2.5

def initialize(s):
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if random.random() < .5:
                s[i][j] = 1
            else:
                s[i][j] = -1
    return s

def deltaU(i, j, s):
    if i == 0:
        top = s[SIZE-1][j]
    else:
        top = s[i-1][j]
    if i == SIZE-1:
        bottom = s[0][j]
    else:
        bottom = s[i+1][j]
    if j == 0:
        left = s[i][SIZE-1]
    else:
        left = s[i][j-1]
    if j == SIZE-1:
        right = s[i][0]
    else:
        right = s[i][j+1]
    return 2 * s[i][j] * (top + bottom + left + right)

def main():
    s = [[0 for x in range(SIZE)] for x in range(SIZE)]
    s = initialize(s)

    p = copy.deepcopy(s)
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if p[i][j] == 1:
                p[i][j] = 0
            else:
                p[i][j] = -p[i][j]
    plt.matshow(p, cmap=plt.cm.gray)
    plt.show(block=False)
    plt.savefig("Initial_S"+str(SIZE)+"_T"+str(T)+".png")
    plt.hold(False)
    time.sleep(1)

    for iteration in range(100*(SIZE**2)):
        i = random.randint(0, SIZE-1)
        j = random.randint(0, SIZE-1)
        Ediff = deltaU(i, j, s)
        if Ediff <= 0:
            s[i][j] = -s[i][j]
        else:
            if random.random() < math.exp(-Ediff/T):
                s[i][j] = -s[i][j]

        # This code animates the graph. Remove #s to see animation. Otherwise leave commented to see initial and final.
        r = copy.deepcopy(s)
        for i in range(0, SIZE):
            for j in range(0, SIZE):
                if r[i][j] == 1:
                    r[i][j] = 0
                else:
                    r[i][j] = -r[i][j]
        plt.matshow(r, fignum=False, cmap=plt.cm.gray)
        plt.draw()
        plt.hold(False)

    r = copy.deepcopy(s)
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if r[i][j] == 1:
                r[i][j] = 0
            else:
                r[i][j] = -r[i][j]
    plt.matshow(r, fignum=False, cmap=plt.cm.gray)
    plt.savefig("Final_S"+str(SIZE)+"_T"+str(T)+".png")
    plt.show(block=True)
    
main()