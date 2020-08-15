import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from matplotlib import cm
from flask import session
import numpy as np
import cmath
from Modules.CompareModule.compareSimulation import Simulation
from Modules.CompareModule.compareVisualization import CreateFigure


isBusy = False

simulationData = None

def SaveData():
    if(simulationData != None):
        np.savetxt('compare.txt',(simulationData[1][0],simulationData[1][1], simulationData[1][2]))

def GetFigure(_valuesChanged):

    global simulationData

    formation = session['formation_C']
    isotropic = session['isotropic_C']
    randomSeed = session['randomSeed_C']
    receiverNumber =  session['numberReceiver_C']
    senderNumber =  session['numberSender_C']
    receiverOrigin = (session['receiverOrigin_C'][0], session['receiverOrigin_C'][1], session['receiverOrigin_C'][2])
    radius = session['radius_C']
    wavelength = session['wavelength_C']
    pathLoss = session['pathLoss_C']
    bValue = session['bValue_C']
    minReceivedValue = session['minReceivedValue_C']
    signalType = session['signalType_C']
    originRadius = session['originRadius_C']
    plotRange = session['plotRange_C']

    isBusy = True

    plt.close('all')

    if(_valuesChanged or simulationData == None):
        simulationData = Simulation(receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                                                pathLoss, bValue, randomSeed, formation, isotropic)
        
                             
    algorithm, data, energie, distanceToOrigin = simulationData
    
    figure = CreateFigure(algorithm, data, energie, signalType, minReceivedValue, plotRange, originRadius, distanceToOrigin)


    isBusy = False

    return figure


