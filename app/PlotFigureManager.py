import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from Simulate.SimulateMimo3d import SimulateMimo3d 
from Simulate.SimulateMiso import SimulateMiso
from Simulate.SimulateMimo import SimulateMimo
from matplotlib import cm
from Figure.Mimo3dFigure import CreateMimo3dFigure
from Figure.MimoReceiverFigure import CreateMimoReceiverFigure
from Figure.MisoSenderFigure import CreateMisoSenderFigure
import numpy as np
import cmath

isBusy = False

MimoReceiverFigure = None

def GetMimoReceiverFigure(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, 
                        _wavelength, _pathLoss, _b, _algorithm, _colors, _vmin, _vmax, _plotTyp, _dimension,
                         _randomSeed, _useMin, _useMax, _formation, _logScale, _valuesChange):
    global isBusy

    global MimoReceiverFigure

    if isBusy:
        return

    isBusy = True

    plt.close('all')

    if(_valuesChange):
        print("values changed so calculate new")
        MimoReceiverFigure = SimulateMimo(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, 
                                                _wavelength, _pathLoss, _b, _algorithm, _randomSeed, _formation)
    else:
        print("values not changed so dont calculate new")
        if MimoReceiverFigure == None:
            print("But MimoFigure == None so calculate new")
            MimoReceiverFigure = SimulateMimo(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, 
                                        _wavelength, _pathLoss, _b, _algorithm, _randomSeed, _formation)

    # MimoReceiverFigure = SimulateMimo3d(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, 
    #                                      _wavelength, _pathLoss, _b, _algorithm, _randomSeed)

    vmin, vmax = None, None
    if(_useMin):
        vmin = _vmin
    if(_useMax):
        vmax = _vmax
    
    receiver_Mimo_figure = CreateMimoReceiverFigure(MimoReceiverFigure, _colors, _receiverPos, _radius, 
                                                    _orientation, vmin, vmax, _plotTyp, _dimension, _logScale)

    isBusy = False

    return receiver_Mimo_figure

def Create_miso_figure(_senderNumber, _receiverPos, _wavelength, _pathLoss, _b,  _algorithm, _colors, _randomSeed, _dimension, _plotTyp):

    sender_f = SimulateMiso(_senderNumber, _receiverPos, _wavelength, _pathLoss, _b, _algorithm, _randomSeed)

    return CreateMisoSenderFigure(sender_f, _colors, _receiverPos, _wavelength, _pathLoss, _b, _dimension, _plotTyp)

