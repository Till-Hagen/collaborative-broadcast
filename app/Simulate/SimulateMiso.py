import time
import numpy as np
from Simulate.Algorithms import ExecuteAlgorithm, SignalAtReceiver

def SimulateMiso(_senderNumber, _receiverPos, _wavelength, _pathloss, _b, _algorithm, _randomSeed):

    start = time.time()

    print("Start Simulate Miso")

    np.random.seed(_randomSeed)

    X = np.random.uniform(-1,1,_senderNumber)

    Y = np.random.uniform(-1,1,_senderNumber)

    senderDist = np.sqrt((np.add(np.square(X),np.square(Y))))

    varphi = ExecuteAlgorithm(_algorithm, X, Y, _wavelength, _b)

    signal = SignalAtReceiver(_receiverPos, X, Y, varphi, _wavelength, _pathloss)

    end = time.time()

    print('End Simulate Miso, elapsed Time: {0}'.format(end - start))

    return (X, Y, signal, senderDist)