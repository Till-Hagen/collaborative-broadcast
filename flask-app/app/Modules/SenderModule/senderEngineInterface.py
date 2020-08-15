import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from matplotlib import cm
from Modules.SenderModule.senderVisualization import Visualize
from Modules.SenderModule.senderSimulation import Simulate
import numpy as np
import cmath

sender_f = None

def SaveData():
    if(sender_f != None):
        np.savetxt('sender.txt', (sender_f[0],sender_f[1],sender_f[2]))

def GetFigure(_senderNumber, _receiverPos, _wavelength, _pathLoss, _b,  _algorithm, _colors, _randomSeed, _dimension, _plotTyp):

    global sender_f

    sender_f = Simulate(_senderNumber, _receiverPos, _wavelength, _pathLoss, _b, _algorithm, _randomSeed)

    return Visualize(sender_f, _colors, _receiverPos, _wavelength, _pathLoss, _b, _dimension, _plotTyp)
