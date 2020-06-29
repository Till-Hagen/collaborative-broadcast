from numba import jit, prange
import math
import time
import numpy as np
from flask import session
from Simulate.SimulateMimo3d import SimulateMimo3d 
from Simulate.SimulateMimo import SimulateMimo
import models

def CompareAlgorithmsSimulation(_receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _b, _randomSeed, _formation, _isotropic, _debug = False):

    if _debug:
        start = time.time()
        print("Start Compare Algorithms Simulation")

    algorithms = ['Parametrized Supernova']
    algorithms.extend([algo.algorithmName for algo in models.Algorithm.query.filter_by(legit=True)])

    simulationData = []
    energieData = []
    distanceToOrigin = []
    iterations = 1000

    if _formation == 'sphere':
        #for algo in algorithms:
        data = []
        usedEnergie = []
        for i in range(iterations):
            res = SimulateMimo3d(_receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _b, algorithms[3], _randomSeed + i, _isotropic)
            data.append(res[3])
            usedEnergie.append(res[4])
        simulationData.append(data)
        energieData.append(usedEnergie)
        distanceToOrigin.append(res[5])
    elif _formation == 'plain horizontal':
        for algo in algorithms:
            data = np.zeros(_receiverNumber)
            usedEnergie = 0
            for i in range(iterations):
                res = SimulateMimo(_receiverNumber, _senderNumber, _receiverOrigin, _radius, 'Horizontal', _wavelength, 
                    _pathLoss, _b, algo, _randomSeed, "random", _isotropic)
                data = data + res[2]
                usedEnergie = (int)(usedEnergie + res[4])
            simulationData.append(data / iterations)
            energieData.append(usedEnergie / iterations)
            distanceToOrigin.append(res[3])
    elif _formation == 'plain vertical':
        for algo in algorithms:
            data = np.zeros(_receiverNumber)
            usedEnergie = 0
            for i in range(iterations):
                res = SimulateMimo(_receiverNumber, _senderNumber, _receiverOrigin, _radius, 'Vertical', _wavelength, 
                    _pathLoss, _b, algo, _randomSeed, "random", _isotropic)
                data = data + res[2]
                usedEnergie = (int)(usedEnergie + res[4])
            simulationData.append(data / iterations)
            energieData.append(usedEnergie / iterations)
            distanceToOrigin.append(res[3])
    end = time.time()

    if _debug:
        print('End: {0}'.format(end - start))



    return (algorithms, simulationData, energieData, distanceToOrigin)
