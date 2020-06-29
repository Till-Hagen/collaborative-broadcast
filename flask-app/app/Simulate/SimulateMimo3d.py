from numba import jit, prange
import sys
import cmath
import math
from flask import session
import numpy as np
from Simulate.Algorithms import ExecuteAlgorithm, SignalAtReceiver
from MimoSphereValues import GetMimoSphereValues

def SimulateMimo3d(_receiverNumber, _senderNumber, _receiverOrigin, _radius, _wavelength, 
                _pathLoss, _bValue, _algorithm, _randomSeed, _isotropic, _debug = False):

    if _debug:
        print("Start Simulate Mimo3d")

    np.random.seed(_randomSeed)

    R = np.random.uniform(0,1,_senderNumber)

    R = np.sqrt(R)

    Z = np.random.uniform(0,1,_senderNumber) * 2 * math.pi

    S_X = np.cos(Z) * R

    S_Y = np.sin(Z) * R

    R = np.random.uniform(0,1,_receiverNumber)

    u = np.random.uniform(0,1,_receiverNumber)
    v = np.random.uniform(0,1,_receiverNumber)
    theta = u * 2 * math.pi
    phi = np.arccos(2.0 * v - 1.0)
    r = np.cbrt(R) * _radius
    sinTheta = np.sin(theta)
    cosTheta = np.cos(theta)
    sinPhi = np.sin(phi)
    cosPhi = np.cos(phi)
    R_X = r * sinPhi * cosTheta + _receiverOrigin[0]
    R_Y = r * sinPhi * sinTheta + _receiverOrigin[1]
    R_Z = r * cosPhi + _receiverOrigin[2]

    varphi, a = ExecuteAlgorithm(_algorithm, S_X, S_Y, _wavelength, _bValue)

    distanceToOrigin = np.sqrt(np.square(R_X) + np.square(R_Y) + np.square(R_Z))

    value_receiver = SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, R_Z, _wavelength, _pathLoss, _receiverNumber, varphi, a, _isotropic)

    if _debug:
        print("End Simulate Mimo3d")

    return (R_X, R_Y, R_Z, value_receiver, np.sum(a), distanceToOrigin)


@jit(nopython=True, nogil=True, parallel=True)
def SignalAtMultipleRandomReceiver(S_X, S_Y, R_X, R_Y, R_Z, __wavelength, __pathLoss, __receiverNumber, _varphi, _a, __isotropic):
    res = np.zeros(__receiverNumber, dtype=np.complex128)
    for i in prange(0,__receiverNumber):
        signal = SignalAtReceiver(( R_X[i], R_Y[i], R_Z[i]), S_X, S_Y, _varphi, _a, __wavelength, __pathLoss, __isotropic)
        res[i] = np.sum(signal)

    return res