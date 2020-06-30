import matplotlib.pyplot as plt
from textwrap import wrap
from flask import session
from Figure.analyzeAlgorithmsFigure import CreateAnalyzeAlgorithmFigure
from Simulate.analyzeAlgorithmsSimulate import AnalyzeAlgorithmsSimulation

isBusy = False

analyzeAlgorithmsFigure = None


def GetAnalyzeAlgorithmsFigure(_valuesChanged):

    global analyzeAlgorithmsFigure

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

    isBusy = True

    plt.close('all')

    if(_valuesChanged or analyzeAlgorithmsFigure == None):
        analyzeAlgorithmsFigure = AnalyzeAlgorithmsSimulation(algorithm, receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                                                pathLoss, bValue, randomSeed, formation, isotropic, iterations)
                             
    data, energie, distanceToOrigin = analyzeAlgorithmsFigure
    
    figure = CreateAnalyzeAlgorithmFigure(algorithm, data, energie, signalType, receivedValue, iterations, originRadius, distanceToOrigin,
                            receiverNumber, senderNumber, radius, formation, bValue, pathLoss, wavelength)


    isBusy = False

    return figure