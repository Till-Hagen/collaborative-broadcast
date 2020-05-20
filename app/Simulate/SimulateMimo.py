from numba import jit, prange
import math
import time
import numpy as np
from Simulate.Algorithms import ExecuteAlgorithm, SignalAtReceiver

def SimulateMimo(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, _wavelength, 
                _pathLoss, _b, _algorithm, _randomSeed, _formation):

    start = time.time()
    print("Start Simulate Mimo")

    M = int(math.sqrt(_receiverNumber))

    np.random.seed(_randomSeed)

    S_X = np.random.uniform(-1,1,_senderNumber)

    S_Y = np.random.uniform(-1,1,_senderNumber)

    if _orientation == 'Horizontal':
       
        if(_formation == 'random'):
            R_X = np.random.uniform(_receiverPos[0] - _radius,_receiverPos[0] + _radius,_receiverNumber)

            R_Y = np.random.uniform(_receiverPos[1] - _radius,_receiverPos[1] + _radius,_receiverNumber)
        else:
            R_X, R_Y = np.meshgrid(np.linspace(_receiverPos[0] - _radius,_receiverPos[0] + _radius, M),
                                                    np.linspace(_receiverPos[1] - _radius,_receiverPos[1] + _radius, M))
 

        receiverDist = np.sqrt((np.add(np.square(R_X - _receiverPos[0]),np.square(R_Y - _receiverPos[1]))))

    else:

        if(_formation == 'random'):
            R_X = np.random.uniform(_receiverPos[0] - _radius,_receiverPos[0] + _radius,_receiverNumber)

            R_Y = np.random.uniform(_receiverPos[2] - _radius,_receiverPos[2] + _radius,_receiverNumber)
        else:
            R_X, R_Y  = np.meshgrid(np.linspace(_receiverPos[0] - _radius,_receiverPos[0] + _radius, M),
                                                 np.linspace(_receiverPos[2] - _radius,_receiverPos[2] + _radius, M))

        receiverDist = np.sqrt((np.add(np.square(R_X - _receiverPos[0]),np.square(R_Y - _receiverPos[2]))))

    
    varphi = ExecuteAlgorithm(_algorithm, S_X, S_Y, _wavelength, _b)

    if(_formation == 'random'):
        value_receiver = SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, 
                                                        _pathLoss, _receiverNumber, varphi, _orientation)
    else:
        value_receiver = SignalAtMultipleReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, 
                                                        _pathLoss, M, varphi, _orientation)

    end = time.time()

    print('End Simulate Mimo, elapsed Time: {0}'.format(end - start))

    return (R_X, R_Y, value_receiver, receiverDist)


@jit(nopython=True, nogil=True, parallel=True)
def SignalAtMultipleReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, _pathloss, M,_varphi, _orientation):
    res = np.zeros((M,M), dtype=np.complex128)
    if _orientation == 'Horizontal':
        for i in prange(0,M):
            for j in prange(0,M):
                signal = SignalAtReceiver(( R_X[i,j], R_Y[i,j], _receiverPos[2]), S_X, S_Y, _varphi, _wavelength, _pathloss)
                res[i,j] = np.sum(signal)
    else:
        for i in prange(0,M):
            for j in prange(0,M):
                signal = SignalAtReceiver(( R_X[i,j], _receiverPos[1], R_Y[i,j]), S_X, S_Y, _varphi, _wavelength, _pathloss)
                res[i,j] = np.sum(signal)

    return res

@jit(nopython=True, nogil=True, parallel=True)
def SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, _pathloss, _receiverNumber,_varphi, _orientation):
    res = np.zeros(_receiverNumber, dtype=np.complex128)
    if _orientation == 'Horizontal':
        for i in prange(0,_receiverNumber):
            signal = SignalAtReceiver(( R_X[i], R_Y[i], _receiverPos[2]), S_X, S_Y, _varphi, _wavelength, _pathloss)
            res[i] = np.sum(signal)
    else:
        for i in prange(0,_receiverNumber):
            signal = SignalAtReceiver(( R_X[i], _receiverPos[1], R_Y[i]), S_X, S_Y, _varphi, _wavelength, _pathloss)
            res[i] = np.sum(signal)

    return res