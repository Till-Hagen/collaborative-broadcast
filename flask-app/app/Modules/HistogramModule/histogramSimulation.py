from numba import jit, prange
import math
import time
import numpy as np
from flask import session
import Modules.ReceiverDisk.receiverDiskSimulation as receiverDisk
import Modules.ReceiverSphere.receiversphereSimulation as receiverSphere
import models

def Simulate(_algorithm, _receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _b, _randomSeed, _formation, _isotropic, _iterations, _debug = False):

    if _debug:
        start = time.time()
        print("Start Histogram Simulation")

    simulationData = []
    energieData = []
    distanceToOrigin = 0

    if _formation == 'sphere':
        for i in range(_iterations):
            res = receiverSphere.Simulate(_receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _b, _algorithm, _randomSeed + i, _isotropic)
            simulationData.append(res[3])
            energieData.append(res[4])
            distanceToOrigin = res[5]
    else:
        if _formation == 'plain horizontal':
            orientation = 'Horizontal'
        else:
            orientation = 'Vertical'
        for i in range(_iterations):
            res = receiverDisk.Simulate(_receiverNumber, _senderNumber, _receiverOrigin, _radius, orientation, _wavelength, 
                _pathLoss, _b, _algorithm, _randomSeed + i, "random", _isotropic)
            simulationData.append(res[2])
            energieData.append(res[4])
            distanceToOrigin = res[3]



    if _debug:
        end = time.time()
        print('End: {0}'.format(end - start))



    return (simulationData, energieData, distanceToOrigin)
