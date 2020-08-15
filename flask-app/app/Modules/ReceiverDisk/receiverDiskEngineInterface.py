import matplotlib.pyplot as plt
from textwrap import wrap
from flask import session
import numpy as np
from Modules.ReceiverDisk.receiverDiskSimulation import Simulate
from Modules.ReceiverDisk.receiverDiskVisualization import CreateFigure

isBusy = False

simulationData = None

def SaveData():
    if(simulationData != None and session['formation_RD'] == "random"):
        np.savetxt('receiverDisk.txt',(simulationData[0],simulationData[1],simulationData[2]))

def GetFigure(_valuesChange, _debug = False):

    global isBusy
    global simulationData

    randomSeed = session['randomSeed_RD']
    receiverNumber = session['numberReceiver_RD']
    senderNumber = session['numberSender_RD']
    receiverPos = session['receiverPos_RD']
    radius = session['radius_RD']
    orientation = session['orientation_RD']
    wavelength = session['wavelength_RD']
    pathLoss = session['pathLoss_RD']
    b = session['bvalue_RD']
    algorithm = session['algorithm_RD']
    upperBound = session['vmax_RD']
    lowerBound = session['vmin_RD']
    dimension = session['dimension_RD']
    plotTyp = session['plotTyp_RD']
    colors = session['color_RD']
    useMin = session['useMin_RD']
    useMax = session['useMax_RD']
    formation = session['formation_RD']
    logScale = session['logScale_RD'] 
    cutOrigin = session['cutOrigin_RD'] 
    originRadius = session['originRadius_RD']
    isotropic = session['isotropic_RD']

    if isBusy:
        return

    isBusy = True

    vmin, vmax = None, None
    if(useMin):
        vmin = lowerBound
    if(useMax):
        vmax = upperBound

    plt.close('all')

    if(_valuesChange):
        if _debug:
            print("values changed so calculate new")
        simulationData = Simulate(receiverNumber, senderNumber, receiverPos, radius, orientation, 
                                                wavelength, pathLoss, b, algorithm, randomSeed, formation, isotropic)
    else:
        if _debug:
            print("values not changed so dont calculate new")
        if simulationData == None:
            if _debug:
                print("But MimoFigure == None so calculate new")
            simulationData = Simulate(receiverNumber, senderNumber, receiverPos, radius, orientation, 
                                        wavelength, pathLoss, b, algorithm, randomSeed, formation, isotropic)
                       

    
    figure = CreateFigure(simulationData, colors, receiverPos, radius, 
                                                    orientation, vmin, vmax, plotTyp, dimension, logScale)

    isBusy = False

    return figure