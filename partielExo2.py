import matplotlib.pyplot as plt
import numpy as np
import matplotlib.offsetbox as box
#from matplotlib import offsetbox
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Slider, TextBox


cursorRange = 0.25

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

def Hermite(bornes):

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
    ax.cla()
    ax.grid(True)
    ax.axis('equal')
    ax.plot(x, y)
    ax.scatter(Lx, Ly, marker="o") # Display points
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


# User Interface

# On textbox enter
def submitX(expression):
    # Update point coordinates
    print(expression)

def submitY(expression):
    # Update point coordinates
    print(expression)

# Textboxes to change point coordinates
axbox = fig.add_axes([0.1, 0.05, 0.3, 0.075])
text_boxX = TextBox(axbox, "X", textalignment="center")
#text_boxX.on_submit(submitX)
aybox = fig.add_axes([0.5, 0.05, 0.3, 0.075])
text_boxY = TextBox(aybox, "Y", textalignment="center")
#text_boxY.on_submit(submitY)

# Point selection with left click
def on_click(event):
    if event.button is MouseButton.LEFT:
        mousex = event.xdata
        mousey = event.ydata
        # Check if point nearby
        for point in list:
            #horizontal check
            if(mousex > point[0] and mousex < point[0] + cursorRange or point[0] > mousex and point[0] < mousex + cursorRange):
                #vertical check
                if(mousey > point[1] and mousey < point[1] + cursorRange or point[1] > mousey and point[1] < mousey + cursorRange):
                    print(point[2])
                    Display(C[0],C[1], Lx, Ly)

                    # Text overlay on top of selected point
                    ax.text(point[0] - 0.2 ,point[1] + 0.5,point[2])

                    #box.TextArea.
                    plt.show()

plt.connect('button_press_event', on_click)

Display(C[0],C[1], Lx, Ly)