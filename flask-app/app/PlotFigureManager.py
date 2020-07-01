import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from Simulate.SimulateMimo3d import SimulateMimo3d 
from Simulate.SimulateMiso import SimulateMiso
from Simulate.SimulateMimo import SimulateMimo
from Simulate.compareAlgorithmsSimulate import CompareAlgorithmsSimulation
from Simulate.analyzeAlgorithmsSimulate import AnalyzeAlgorithmsSimulation
from matplotlib import cm
from flask import session
from Figure.MimoSphereFigure import CreateMimoSphereFigure
from Figure.MimoReceiverFigure import CreateMimoReceiverFigure
from Figure.MisoSenderFigure import CreateMisoSenderFigure
from Figure.compareAlgorithmsFigure import CreateCompareAlgorithmsFigure
from Figure.analyzeAlgorithmsFigure import CreateAnalyzeAlgorithmFigure
import numpy as np
import cmath

isBusy = False

MimoReceiverFigure = None

Mimo3dReceiverFigure = None

compareAlgorithmsFigure = None

analyzeAlgorithmsFigure = None

def GetMimo3dReceiverFigure(_valuesChange, _debug = False):
    global isBusy

    global Mimo3dReceiverFigure

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
        Mimo3dReceiverFigure = SimulateMimo3d(receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                pathLoss, b, algorithm, randomSeed, isotropic, _debug)
    else:
        if _debug:
            print("values not changed so dont calculate new")
        if Mimo3dReceiverFigure == None:
            if _debug:
                print("But MimoFigure == None so calculate new")
            Mimo3dReceiverFigure = SimulateMimo3d(receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                pathLoss, b, algorithm, randomSeed, isotropic, _debug)
    
    receiver_Mimo3d_figure = CreateMimoSphereFigure(Mimo3dReceiverFigure)

    isBusy = False

    return receiver_Mimo3d_figure



def Create_miso_figure(_senderNumber, _receiverPos, _wavelength, _pathLoss, _b,  _algorithm, _colors, _randomSeed, _dimension, _plotTyp):

    sender_f = SimulateMiso(_senderNumber, _receiverPos, _wavelength, _pathLoss, _b, _algorithm, _randomSeed)

    return CreateMisoSenderFigure(sender_f, _colors, _receiverPos, _wavelength, _pathLoss, _b, _dimension, _plotTyp)

def GetCompareAlgorithmsFigure(_valuesChanged):

    global compareAlgorithmsFigure

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

    if(_valuesChanged or compareAlgorithmsFigure == None):
        compareAlgorithmsFigure = CompareAlgorithmsSimulation(receiverNumber, senderNumber, receiverOrigin, radius, wavelength, 
                                                pathLoss, bValue, randomSeed, formation, isotropic)
                             
    algorithm, data, energie, distanceToOrigin = compareAlgorithmsFigure
    
    figure = CreateCompareAlgorithmsFigure(algorithm, data, energie, signalType, minReceivedValue, plotRange, originRadius, distanceToOrigin)


    isBusy = False

    return figure


