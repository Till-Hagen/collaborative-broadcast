from numba import jit, prange
import sys
import cmath
import math
import numpy as np
from Simulate.Algorithms import ExecuteAlgorithm, SignalAtReceiver

def SimulateMimo3d(_receiverNumber, _senderNumber, _receiverPos, _radius, _orientation, _wavelength, _pathLoss, _b, _algorithm, _randomSeed):

    print("Start Simulate Mimo3d")

    res = []

    N = int(math.sqrt(_senderNumber))

    M = int(math.sqrt(_receiverNumber))

    np.random.seed(_randomSeed)

    S_X = np.sort(np.random.uniform(-1,1,N ** 2).reshape(N,N))

    S_Y = np.sort(np.random.uniform(-1,1,N ** 2)).reshape(N,N)

   # S_X, S_Y = np.meshgrid(np.linspace(-1, 1, N), np.linspace(-1, 1, N))

    R_X, R_Y = np.meshgrid(np.linspace(_receiverPos[0] - _radius,_receiverPos[0] + _radius, M),
                                            np.linspace(_receiverPos[1] - _radius,_receiverPos[1] + _radius, M))
    receiverDist = np.sqrt((np.add(np.square(R_X - _receiverPos[0]),np.square(R_Y - _receiverPos[1]))))

    varphi = ExecuteAlgorithm(_algorithm, S_X, S_Y, _wavelength, _b)

    receiverPos = (_receiverPos[0], _receiverPos[1], _receiverPos[2])
    value_receiver = calculateMimo(S_X, S_Y, R_X, R_Y, receiverPos,_wavelength, _pathLoss,  N, M, varphi, _orientation)
    res.append((value_receiver, receiverPos))

    print("End Simulate Mimo3d")

    print(receiverDist)

    print(res)

    return (R_X, R_Y, res, receiverDist)


@jit(nopython=True, nogil=True, parallel=True)
def calculateMimo(S_X, S_Y, R_X, R_Y, _receiverPos, _wavelength, _pathloss, N, M,_varphi,  _orientation):
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