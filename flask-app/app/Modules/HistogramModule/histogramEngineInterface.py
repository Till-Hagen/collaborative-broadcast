import matplotlib.pyplot as plt
from textwrap import wrap
from flask import session
import numpy as np
from Modules.HistogramModule.histogramSimulation import Simulate
from Modules.HistogramModule.histogramVisualization import CreateFigure

isBusy = False

simulationData = None

def SaveData():
    if(simulationData != None):
        
        data, energie, distanceToOrigin = simulationData

        np.savetxt('histogram.txt',data)

def GetFigure(_valuesChanged):

    global simulationData

    formation = session['formation_AC']
    isotropic = session['isotropic_AC']
    randomSeed = session['randomSeed_AC']
    receiverNumber =  session['numberReceiver_AC']
    senderNumber =  session['numberSender_AC']
    receiverOrigin = (session['receiverOrigin_AC'][0], session['receiverOrigin_AC'][1], session['receiverOrigin_AC'][2])
    radius = session['radius_AC']
    wavelength = session['wavelength_AC']
    pathLoss = session['pathLoss_AC']
    bValue = session['bValue_AC']
    receivedValue = session['receivedValue_AC']
    signalType = session['signalType_AC']
    originRadius = session['originRadius_AC']
    iterations = session['iterations_AC']
    algorithm = session['algorithm_AC']
    minRange= session['minRange_AC']
    maxRange = session['maxRange_AC']
    topRange = session['topRange_AC']
    saveData = session['saveData_AC']

    isBusy = True

    plt.close('all')

    if(_valuesChanged or simulationData == None):
        simulationData = Simulate(algorithm, receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                                                pathLoss, bValue, randomSeed, formation, isotropic, iterations)

                            
    data, energie, distanceToOrigin = simulationData
    
    figure = CreateFigure(algorithm, data, energie, signalType, receivedValue, iterations, originRadius, distanceToOrigin,
                            receiverNumber, senderNumber, radius, formation, bValue, pathLoss, wavelength, minRange,
                            maxRange, topRange)


    isBusy = False

    return figure