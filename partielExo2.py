import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Button, TextBox

cursorRange = 0.25
#create the global variable for selecting a point
pointSelect = 0

# C : point sur les angles (10 points)
pointList = [[2, 6, 1],[6, 6, 1],[3.6, 8.5, 0],[8.6, 7.5, -1],[7.8, 4.8, -1],[9.4, 5.4, 0],[9, 3.3, -2],[6, 3, -2],[5.8, 1.4, -0.6],[2.2, 2.4, 1.1]]


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
        bornes[0][1] * PhiOne(phiX)
        + bornes[1][1] * PhiTwo(phiX)
        + (bornes[1][0]  - bornes[0][0]) * bornes[0][2] * PhiThree(phiX)
        + (bornes[1][0]  - bornes[0][0]) * bornes[1][2] * PhiFour(phiX)
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
def PhiOne(x):
    return (((x - 1)**2) * (2 * x + 1))

def PhiTwo(x):
    return (x**2 * (-2 * x + 3))

def PhiThree(x): 
    return ((x - 1)**2 * x)

def PhiFour(x):
    return (x**2 * (x - 1))

def Display():
    global pointList

    x,y = HermiteList(pointList)[0] , HermiteList(pointList)[1]
    
    #making lists to show points 
    Lx , Ly = [] , []
    for i in range(len(pointList)):
        Lx.append(pointList[i][0]) 
        Ly.append(pointList[i][1])  
        
    ax.cla()
    ax.grid(True)
    ax.axis('equal')
    ax.plot(x, y)
    ax.scatter(Lx, Ly, marker="o") # Display points
    plt.show()

# User Interface
# Textboxes to change point coordinates
axbox = fig.add_axes([0.15, 0.05, 0.1, 0.075])
text_boxX = TextBox(axbox, "X", textalignment="center")
aybox = fig.add_axes([0.35, 0.05, 0.1, 0.075])
text_boxY = TextBox(aybox, "Y", textalignment="center")
adbox = fig.add_axes([0.55, 0.05, 0.1, 0.075])
text_boxD = TextBox(adbox, "F'(X)", textalignment="center")

# Point selection with left click
def On_click(event):
    if event.button is MouseButton.LEFT:
        mousex = event.xdata
        mousey = event.ydata
        # Check if point nearby
        for i in range(len(pointList)):
            #check if mouse is in thefigure box
            if(mousex is not None and mousey is not None):
                #horizontal check
                if(mousex > pointList[i][0] and mousex < pointList[i][0] + cursorRange or pointList[i][0] > mousex and pointList[i][0] < mousex + cursorRange):
                    #vertical check
                    if(mousey > pointList[i][1] and mousey < pointList[i][1] + cursorRange or pointList[i][1] > mousey and pointList[i][1] < mousey + cursorRange):
                        
                        Display()
                        
                        
                        ax.text(pointList[i][0] - 0.09 ,pointList[i][1] + 0.15,"V")

                        global pointSelect
                        pointSelect = i

                        # Fill textboxes with point info
                        text_boxX.set_val(pointList[pointSelect][0])
                        text_boxY.set_val(pointList[pointSelect][1])
                        text_boxD.set_val(pointList[pointSelect][2])

                        #box.TextArea.
                        plt.show()

def Submit(event):
    global pointList
    # Get data from textboxes
    if(text_boxX.text != ""):
        pointList[pointSelect][0] = float(text_boxX.text)
    if(text_boxY.text != ""):
        pointList[pointSelect][1] = float(text_boxY.text)
    if(text_boxD.text != ""):
        pointList[pointSelect][2] = float(text_boxD.text)
    Display()

plt.connect('button_press_event', On_click)

# Submit button
bbox = fig.add_axes([0.8, 0.05, 0.1, 0.075])
bsubmit = Button(bbox,"Submit")
bsubmit.on_clicked(Submit)


Display()