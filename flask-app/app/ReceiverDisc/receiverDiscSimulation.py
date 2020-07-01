from numba import jit, prange
import math
import time
import numpy as np
from flask import session
from Simulate.Algorithms import ExecuteAlgorithm, SignalAtReceiver

def Simulate(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, _wavelength, 
                _pathLoss, _b, _algorithm, _randomSeed, _formation, _isotropic, _debug = False):

    if _debug:
        start = time.time()
        print("Start Simulate Mimo")


    M = int(math.sqrt(_receiverNumber))

    np.random.seed(_randomSeed)

    R = np.random.uniform(0,1,_senderNumber)

    R = np.sqrt(R)

    Z = np.random.uniform(0,1,_senderNumber) * 2 * math.pi

    S_X = np.cos(Z) * R

    S_Y = np.sin(Z) * R

    if _orientation == 'Horizontal':
       
        if(_formation == 'random'):
            R = np.random.uniform(0,1,_receiverNumber)

            R = np.sqrt(R) * _radius

            Z = np.random.uniform(0,1,_receiverNumber) * 2 * math.pi

            R_X = np.cos(Z) * R + _receiverPos[0]

            R_Y = np.sin(Z) * R + _receiverPos[1]
        else:
            R_X, R_Y = np.meshgrid(np.linspace(_receiverPos[0] - _radius,_receiverPos[0] + _radius, M),
                                                    np.linspace(_receiverPos[1] - _radius,_receiverPos[1] + _radius, M))
 

        receiverDist = np.sqrt((np.add(np.square(R_X - _receiverPos[0]),np.square(R_Y - _receiverPos[1]))))

    else:

        if(_formation == 'random'):
            R = np.random.uniform(0,1,_receiverNumber)

            R = np.sqrt(R) * _radius

            Z = np.random.uniform(0,1,_receiverNumber) * 2 * math.pi

            R_X = np.cos(Z) * R + _receiverPos[0]

            R_Y = np.sin(Z) * R + _receiverPos[2]
        else:
            R_X, R_Y  = np.meshgrid(np.linspace(_receiverPos[0] - _radius,_receiverPos[0] + _radius, M),
                                                 np.linspace(_receiverPos[2] - _radius,_receiverPos[2] + _radius, M))

        receiverDist = np.sqrt((np.add(np.square(R_X - _receiverPos[0]),np.square(R_Y - _receiverPos[2]))))

    
    varphi, a = ExecuteAlgorithm(_algorithm, S_X, S_Y, _wavelength, _b)

    if(_formation == 'random'):
        value_receiver = SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, 
                                                        _pathLoss, _receiverNumber, varphi, a,_orientation, _isotropic)
    else:
        value_receiver = SignalAtMultipleReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, 
                                                        _pathLoss, M, varphi, a, _orientation, _isotropic)

    end = time.time()

    if _debug:
        print('End Simulate Mimo, elapsed Time: {0}'.format(end - start))

    return (R_X, R_Y, value_receiver, receiverDist, np.sum(a))


@jit(nopython=True, nogil=True, parallel=True)
def SignalAtMultipleReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, _pathloss, M,_varphi, _a, _orientation, _isotropic):
    res = np.zeros((M,M), dtype=np.complex128)
    if _orientation == 'Horizontal':
        for i in prange(0,M):
            for j in prange(0,M):
                signal = SignalAtReceiver(( R_X[i,j], R_Y[i,j], _receiverPos[2]), S_X, S_Y, _varphi, _a, _wavelength, _pathloss,_isotropic)
                res[i,j] = np.sum(signal)
    else:
        for i in prange(0,M):
            for j in prange(0,M):
                signal = SignalAtReceiver(( R_X[i,j], _receiverPos[1], R_Y[i,j]), S_X, S_Y, _varphi, _a, _wavelength, _pathloss,_isotropic)
                res[i,j] = np.sum(signal)

    return res

@jit(nopython=True, nogil=True, parallel=True)
def SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, _pathloss, _receiverNumber,_varphi, _a, _orientation, _isotropic):
    res = np.zeros(_receiverNumber, dtype=np.complex128)
    if _orientation == 'Horizontal':
        for i in prange(0,_receiverNumber):
            signal = SignalAtReceiver(( R_X[i], R_Y[i], _receiverPos[2]), S_X, S_Y, _varphi, _a, _wavelength, _pathloss, _isotropic)
            res[i] = np.sum(signal)
    else:
        for i in prange(0,_receiverNumber):
            signal = SignalAtReceiver(( R_X[i], _receiverPos[1], R_Y[i]), S_X, S_Y, _varphi, _a, _wavelength, _pathloss,_isotropic)
            res[i] = np.sum(signal)

    return res