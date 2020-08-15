from numba import jit, prange
import math
import time
import numpy as np
from flask import session
import Modules.ReceiverDisk.receiverDiskSimulation as receiverDisk
import Modules.ReceiverSphere.receiversphereSimulation as receiverSphere
import models

def Simulation(_receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _b, _randomSeed, _formation, _isotropic, _debug = False):

    if _debug:
        start = time.time()
        print("Start Compare Algorithms Simulation")

    algorithms = []
    algorithms.extend([algo.algorithmName for algo in models.Algorithm.query.filter_by(legit=True)])

    simulationData = []
    energieData = []
    distanceToOrigin = []

    if _formation == 'sphere':
        for algo in algorithms:
            data = []
            usedEnergie = []
            res = receiverSphere.Simulate(_receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _b, algo, _randomSeed, _isotropic)
            simulationData.append(res[3])
            energieData.append(res[4])
            distanceToOrigin.append(res[5])
    elif _formation == 'plain horizontal':
        for algo in algorithms:
            res = receiverDisk.Simulate(_receiverNumber, _senderNumber, _receiverOrigin, _radius, 'Horizontal', _wavelength, 
                _pathLoss, _b, algo, _randomSeed, "random", _isotropic)
            simulationData.append(res[2])
            energieData.append(res[4])
            distanceToOrigin.append(res[3])
    elif _formation == 'plain vertical':
        for algo in algorithms:
            res = receiverDisk.Simulate(_receiverNumber, _senderNumber, _receiverOrigin, _radius, 'Vertical', _wavelength, 
                _pathLoss, _b, algo, _randomSeed, "random", _isotropic)
            simulationData.append(res[2])
            energieData.append(res[4])
            distanceToOrigin.append(res[3])
    end = time.time()

    if _debug:
        print('End: {0}'.format(end - start))

    return (algorithms, simulationData, energieData, distanceToOrigin)
