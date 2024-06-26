import matplotlib.pyplot as plt
import numpy as np

def rotate180From(P):
    
    transP = [P[0], P[1]]
            
    """
    the rotation matrix is as follows:
    -1          0
    0           -1
    """
    for i in range(len(transP)):
        transP[i] = transP[i] * (-1)
    
    #and then we return to the original position
    finalP = [transP[0], transP[1], -P[2]]


    return finalP

def rotate90From(tempOrigin, P):

    """
    the rotation matrix is as follows:
    0     -1
    1     0
    """
    transP = [-(P[1] - tempOrigin[1]), (P[0] - tempOrigin[0])]
    #and then we return to the original position
    finalP = [transP[0] + tempOrigin[0], transP[1] + tempOrigin[1], P[2]]

    return finalP



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
         
    return [x,y]

def HermiteList(points):
    x = []
    y = []
    for i in range(len(points)):
        
        """
            flippedEnd = rotate180From(points[i])
            flippedStart = rotate180From(points[i-1])

            xy = Hermite([flippedStart, flippedEnd])

            for j in range(len(xy)):
                xy[j] = rotate180From(xy[j])  
        """
       
        if(points[i][0]<points[i-1][0]):
            # On retourne en arrière, faut faire une rotation
            # On inverse leurs dérivées
            a = [points[i-1][0], points[i-1][1], -points[i-1][2]]
            b = [points[i][0], points[i][1], -points[i][2]]
            xy = Hermite([a, b])
            
        else:
            xy = Hermite([points[i-1], points[i]])

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

def Display(x,y,Lx,Ly):
    plt.grid(True)
    plt.axis('equal')
    plt.plot(x, y)
    plt.scatter(Lx, Ly, marker="o") # Display points
    plt.show()

# A : point entre les angles
#A = HermiteList([[1.8,5.8,2], [4,7,-0.2], [4.6,8.4, -1], [6, 9.5,-0.2], [8,7,-0.8], [8.2, 4.6, 0], [9.6, 4.4, 1], [7,3.2, 0], [5, 1.2, 0]])
#Display(A[0], A[1])

# B : point sur les angles (9 points)
#B = HermiteList([[2, 6, 1],[6, 6, 1],[3.6, 8.5, 0],[8.6, 7.5, -1],[7.8, 4.8, -1],[9.4, 5.4, 0],[6, 3, -2],[5.8, 1.4, -0.6],[2.2, 2.4, 1.1]])
#Display(B[0],B[1])

# C : point sur les angles (10 points)
list = [[2, 6, 1],[6, 6, 1],[3.6, 8.5, 0],[8.6, 7.5, -1],[7.8, 4.8, -1],[9.4, 5.4, 0],[9, 3.3, -2],[6, 3, -2],[5.8, 1.4, -0.6],[2.2, 2.4, 1.1]]
C = HermiteList(list)

#making lists to show points 
Lx , Ly = [] , []

for i in range(len(list)):
    Lx.append(list[i][0]) 
    Ly.append(list[i][1])  
    
Display(C[0],C[1], Lx, Ly)