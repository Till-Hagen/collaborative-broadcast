import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from matplotlib import cm
from flask import session
from Modules.ReceiverSphere.receiversphereSimulation import Simulate
from Modules.ReceiverSphere.receiverSphereVisualization import CreateFigure
import numpy as np
import cmath

isBusy = False

simulationData = None

def SaveData():
    if(simulationData != None):
        np.savetxt('receiverSphere.txt',(simulationData[0],simulationData[1],simulationData[2],simulationData[3]))

def GetFigure(_valuesChange, _debug = False):
    global isBusy

    global simulationData

    if isBusy:
        return

    isBusy = True

    receiverNumber =  session['receiverNumber_RS']
    senderNumber =  session['senderNumber_RS']
    receiverOrigin =  session['receiverOrigin_RS']
    radius =  session['radius_RS']
    wavelength =  session['wavelength_RS']
    pathLoss =  session['pathLoss_RS']
    b =  session['bValue_RS']
    algorithm =  session['algorithm_RS']
    randomSeed =  session['randomSeed_RS']
    isotropic =  session['isotropic_RS']

    plt.close('all')

    if(_valuesChange):
        if _debug:
            print("values changed so calculate new")
        simulationData = Simulate(receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                pathLoss, b, algorithm, randomSeed, isotropic, _debug)      
    else:
        if _debug:
            print("values not changed so dont calculate new")
        if simulationData == None:
            if _debug:
                print("But MimoFigure == None so calculate new")
            simulationData = Simulate(receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                pathLoss, b, algorithm, randomSeed, isotropic, _debug)

    figure = CreateFigure(simulationData)

    isBusy = False

    return figure


