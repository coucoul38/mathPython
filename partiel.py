import matplotlib.pyplot as plt
import numpy as np

plt.grid(True)
plt.axis('equal')

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def Hermite(bornes):

    """
    x =  np.linspace(bornes[0][0], bornes[1][0], 100)
    y = bornes[0][1] + (x - bornes[0][0]) * ((bornes[1][1] - bornes[0][1]) / (bornes[1][0] - bornes[0][0]))
    """ 

    x = []
    y = []

    ## n = nombre de point que l'on veut
    interv =  np.linspace(bornes[0][0], bornes[1][0], 50)

    for i in interv : 
        x.append(i)

        phiX = (i - bornes[0][0])/(bornes[1][0] - bornes[0][0])

        y.append(
        bornes[0][1] * phiOne(phiX)
        + bornes[1][1] * phiTwo(phiX)
        + (bornes[1][0]  - bornes[0][0]) * bornes[0][2] * phiThree(phiX)
        + (bornes[1][0]  - bornes[0][0]) * bornes[1][2] * phiFour(phiX)
        )
         
    return (x,y)

def HermiteList(points):
    x = []
    y = []
    for i in range(len(points)-1):
        if(points[i+1][0]<points[i][0]):
        #     ## On retourne en arrière, faut faire une rotation
            # On inverse leurs dérivées
            a = [points[i+1][0],points[i+1][1],- ( 100 - points[i+1][2])]
            b = [points[i][0],points[i][1],- ( 100 - points[i+1][2])]
            xy = Hermite([a, b])
        else:
            xy = Hermite([points[i], points[i+1]])
            
        for xi in xy[0]:
            x.append(xi)
        for yi in xy[1]:
            y.append(yi)

    return (x,y)


# phi functions for the Hermite calculations
def phiOne(x):
    return (((x - 1)**2) * (2 * x + 1))

def phiTwo(x):
    return (x**2 * (-2 * x + 3))

def phiThree(x): 
    return ((x - 1)**2 * x)

def phiFour(x):
    return (x**2 * (x - 1))

def Display(x,y):
    plt.plot(x, y)
    plt.show()

A = HermiteList([[1.8,5.8,2], [4,7,-0.2], [4.6,8.4, -1]])
B = HermiteList([[2,6,1],[6,6,1],[3.6,8.5,0],[8.6,7.5,- 1]])
C = HermiteList([[0,0,1],[0.1,1,-1]])
#Display(A[0], A[1])
Display(B[0],B[1])
#Display(A[0],A[1])

#[6, 9.5,-0.2], [8,7,-0.8], [8.2, 4.6, 0], [9.6, 4.4, 1], [7,3.2, 0], [5, 1.2, 0]

def rotate180From(tempOrigin, P):

    transP = [P[0] - tempOrigin[0], P[1] - tempOrigin[1]]
    """
    the rotation matrix is as follows:
    -1          0
    0           -1
    """
    transP[0] = -transP[0]
    transP[1] = -transP[1]

    #and then we return to the original position
    transP[0] = transP[0] + tempOrigin[0]
    transP[1] = transP[1] + tempOrigin[1]

    return transP

def rotate90From(tempOrigin, P):

    transP = [P[0] - tempOrigin[0], P[1] - tempOrigin[1]]
    """
    the rotation matrix is as follows:
    
    0     -1
    1     0
    """
    transP[0] = -transP[0]
    transP[1] = -transP[1]

    #and then we return to the original position
    transP[0] = transP[0] + tempOrigin[0]
    transP[1] = transP[1] + tempOrigin[1]

    return transP