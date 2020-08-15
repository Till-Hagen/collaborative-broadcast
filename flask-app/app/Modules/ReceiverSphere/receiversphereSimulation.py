from numba import jit, prange
import sys
import cmath
import math
import time
import random as random
from flask import session
import numpy as np
from Algorithm.Algorithm import ExecuteAlgorithm
from Algorithm.PathLossModel import SignalAtReceiver

def Simulate(_receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _bValue, _algorithm, _randomSeed, _isotropic, _debug = False):

    if _debug:
        print("Start Simulate Mimo3d")

    start = time.time()

    # R_X, R_Y, R_Z = [],[],[]


    # while(len(R_X) < _receiverNumber):
    #     x = random.uniform(-_radius, _radius)
    #     y = random.uniform(-_radius, _radius)
    #     z = random.uniform(-_radius, _radius)
    #     if(math.sqrt(x * x + y * y + z * z) <= _radius):
    #         R_X.append(x)
    #         R_Y.append(y)
    #         R_Z.append(z)

    # R_X = np.array(R_X)
    # R_Y = np.array(R_Y)
    # R_Z = np.array(R_Z)
    
    R = np.random.uniform(0,1,_senderNumber)

    R = np.sqrt(R)

    Z = np.random.uniform(0,1,_senderNumber) * 2 * math.pi

    S_X = np.cos(Z) * R

    S_Y = np.sin(Z) * R

    end = time.time()



    mu = 0
    sigma = 1

    X = np.random.normal(mu, sigma, _receiverNumber)
    Y = np.random.normal(mu, sigma, _receiverNumber)
    Z = np.random.normal(mu, sigma, _receiverNumber)

    R = np.random.uniform(0,1,_receiverNumber)

    R = np.cbrt(R)

    normalize = np.sqrt(np.square(X) + np.square(Y) + np.square(Z))

    R_X = np.divide(X, normalize, out=np.zeros_like(X), where=normalize!=0)* R * _radius + _receiverOrigin[0]

    R_Y = np.divide(Y, normalize, out=np.zeros_like(Y), where=normalize!=0) * R * _radius + _receiverOrigin[1]

    R_Z = np.divide(Z, normalize, out=np.zeros_like(Z), where=normalize!=0) * R * _radius + _receiverOrigin[2]




    # R = np.random.uniform(0,1,_receiverNumber)

    # u = np.random.uniform(0,1,_receiverNumber)
    # v = np.random.uniform(0,1,_receiverNumber)
    # theta = u * 2 * math.pi
    # phi = np.arccos(2.0 * v - 1.0)
    # r = np.cbrt(R) * _radius
    # sinTheta = np.sin(theta)
    # cosTheta = np.cos(theta)
    # sinPhi = np.sin(phi)
    # cosPhi = np.cos(phi)
    # R_X = r * sinPhi * cosTheta + _receiverOrigin[0]
    # R_Y = r * sinPhi * sinTheta + _receiverOrigin[1]
    # R_Z = r * cosPhi + _receiverOrigin[2]


    varphi, a = ExecuteAlgorithm(_algorithm, S_X, S_Y, _wavelength, _bValue)

    distanceToOrigin = np.sqrt(np.square(R_X) + np.square(R_Y) + np.square(R_Z))

    value_receiver = SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, R_Z, _wavelength, _pathLoss, _receiverNumber, varphi, a, _isotropic)

    if _debug:
        print('Elapsed Time: {0}'.format(end - start))

    return (R_X, R_Y, R_Z, value_receiver, np.sum(a), distanceToOrigin)


@jit(nopython=True, nogil=True, parallel=True)
def SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, R_Z, __wavelength, __pathLoss, __receiverNumber, _varphi, _a, __isotropic):
    res = np.zeros(__receiverNumber, dtype=np.complex128)
    for i in prange(0,__receiverNumber):
        signal = SignalAtReceiver(( R_X[i], R_Y[i], R_Z[i]), S_X, S_Y, _varphi, _a, __wavelength, __pathLoss, __isotropic)
        res[i] = np.sum(signal)

    return res