import matplotlib.pyplot as plt
import numpy as np
from math import *

import matplotlib as mpl

def ex2(x):
    return(x*x+1)

def generate(f,start, end, step, rotation = 0):
    list = []
    i = 0.0
    while(i < (end-start+step)):
        list.append([i+start, f(i+start)])    
        i += step

    if(rotation != 0):
        list = rotate_list(list, rotation)

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x, y = zip(*list)
    ax.plot(x,y)  # Plot some data on the axes.
    plt.show()

def rotate_list(list, angle):
    angleRad = angle * pi/180
    result = []
    for i in list:
        result.append([cos(angleRad) * i[0] - sin(angleRad) * i[1],sin(angleRad) * i[0] + cos(angleRad) * i[1]])

    return result

def Lagrange(list,x):
    a = []
    b = []
    L = []

    # polynome outil
    for i in list:
        xK = list[i][0]
        for j in L:
            if (j != i):
                L[i]=(x-list[j][0])/(xK - list[j][0])
        L[i] = a/b

    PL = 0
    for k in L:
        PL += (L[k]*list[k][1])


def Lagrange2(x):
    L = [[0,2],[1,4],[2,-2],[3,-1]]
    P = 0
    for i in range(len(L)):
        l = 1
        for j in range(len(L)):
            if(i != i):
                l = l*(x-L[j][0]) / (L[i][0] - L[j][0])
                P = P + l * L[i][1]
    print(P)
    return P

#generate(ex2,-1,1,0.1)

#generate(ex2,-1,1,0.01, 90) #ex3

#generate(Lagrange([[0,2],[1,4],[2,-2],[3,-1]]),-1,4,0.1)

generate(Lagrange2,-1,4,0.1)
