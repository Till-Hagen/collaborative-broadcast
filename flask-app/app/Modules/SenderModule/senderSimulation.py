import time
import numpy as np
import math
from flask import session
from Algorithm.Algorithm import ExecuteAlgorithm
from Algorithm.PathLossModel import SignalAtReceiver

def Simulate(_senderNumber, _receiverPos, _wavelength, _pathloss, _b, _algorithm, _randomSeed, _debug = False):

    isotropic = session['isotropic_S']

    np.random.seed(_randomSeed)

    mu = 0
    sigma = 1

    X = np.random.normal(mu, sigma, _senderNumber)
    Y = np.random.normal(mu, sigma, _senderNumber)

    R = np.random.uniform(0,1,_senderNumber)

    R = np.sqrt(R)

    normalize = np.sqrt(np.square(X) + np.square(Y))

    X = np.divide(X, normalize, out=np.zeros_like(X), where=normalize!=0)* R

    Y = np.divide(Y, normalize, out=np.zeros_like(Y), where=normalize!=0) * R

    # R = np.random.uniform(0,1,_senderNumber)

    # R = np.sqrt(R)

    # Z = np.random.uniform(0,1,_senderNumber)

    # Y = np.random.uniform(0,1,_senderNumber)

    # #X = X * 2 * math.pi

    # Z = Z * 2 * math.pi

    # X = np.cos(Z) * R

    # Y = np.sin(Z) * R

    senderDist = np.sqrt((np.add(np.square(X),np.square(Y))))

    varphi, a = ExecuteAlgorithm(_algorithm, X, Y, _wavelength, _b)

    if _debug:
        start = time.time()
        print("Start Simulate Miso")
    
    signal = SignalAtReceiver(_receiverPos, X, Y, varphi, a, _wavelength, _pathloss, isotropic)

    end = time.time()

    if _debug:
        print('End Simulate Miso, elapsed Time: {0}'.format(end - start))

    return (X, Y, signal, senderDist, np.sum(a))