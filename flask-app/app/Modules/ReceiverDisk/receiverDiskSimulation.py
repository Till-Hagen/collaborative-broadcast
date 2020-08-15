from numba import jit, prange
import math
import time
import numpy as np
from flask import session
from Algorithm.Algorithm import ExecuteAlgorithm
from Algorithm.PathLossModel import SignalAtReceiver

def Simulate(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, _wavelength, 
                _pathLoss, _b, _algorithm, _randomSeed, _formation, _isotropic, _debug = False):

    if _debug:
        start = time.time()
        print("Start Simulate Mimo")

    M = int(math.sqrt(_receiverNumber))

    np.random.seed(_randomSeed)

    mu = 0
    sigma = 1

    X = np.random.normal(mu, sigma, _senderNumber)
    Y = np.random.normal(mu, sigma, _senderNumber)

    S_R = np.random.uniform(0,1,_senderNumber)

    S_R = np.sqrt(S_R)

    normalize = np.sqrt(np.square(X) + np.square(Y))

    S_X = np.divide(X, normalize, out=np.zeros_like(X), where=normalize!=0)* S_R

    S_Y  = np.divide(Y, normalize, out=np.zeros_like(Y), where=normalize!=0) * S_R

    if _orientation == 'Horizontal':
       
        if(_formation == 'random'):
            X = np.random.normal(mu, sigma, _receiverNumber)
            Y = np.random.normal(mu, sigma, _receiverNumber)

            R = np.random.uniform(0,1,_receiverNumber)

            R = np.sqrt(R)

            normalize = np.sqrt(np.square(X) + np.square(Y))

            R_X = np.divide(X, normalize, out=np.zeros_like(X), where=normalize!=0)* R * _radius + _receiverPos[0]

            R_Y = np.divide(Y, normalize, out=np.zeros_like(Y), where=normalize!=0) * R * _radius + _receiverPos[1]
        else:
            R_X, R_Y = np.meshgrid(np.linspace(_receiverPos[0] - _radius,_receiverPos[0] + _radius, M),
                                                    np.linspace(_receiverPos[1] - _radius,_receiverPos[1] + _radius, M))
 
        receiverDist = np.sqrt((np.add(np.square(R_X - _receiverPos[0]),np.square(R_Y - _receiverPos[1]))))

    else:

        if(_formation == 'random'):
            X = np.random.normal(mu, sigma, _receiverNumber)
            Y = np.random.normal(mu, sigma, _receiverNumber)

            R = np.random.uniform(0,1,_receiverNumber)

            R = np.sqrt(R)

            normalize = np.sqrt(np.square(X) + np.square(Y))

            R_X = np.divide(X, normalize, out=np.zeros_like(X), where=normalize!=0)* R * _radius + _receiverPos[0]

            R_Y = np.divide(Y, normalize, out=np.zeros_like(Y), where=normalize!=0) * R * _radius + _receiverPos[2]
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