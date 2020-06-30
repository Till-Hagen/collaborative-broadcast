import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
import matplotlib.mlab as mlab
from matplotlib import cm
from flask import session
from scipy.stats import norm
import numpy as np
import cmath

def CreateAnalyzeAlgorithmFigure(_algorithm, _data, _energie, _signalType, _receivedValue, _iterations,
                                 _originRadius, _distanceToOrigin, _receiverNumber, _senderNumber, 
                                 _radius, _formation, _b, _pathLoss, _waveLenght):

    iterations = _iterations

    energie = _energie

    fig = plt.figure(figsize=(7, 6.2))

    i = 0

    res = []

    if(_signalType == 'real'):
        Z = _data.real

    elif(_signalType == 'imag'):
        Z = _data.imag

    elif(_signalType == '|z|^2'):
        Z = np.square(np.absolute(_data))
    elif(_signalType == '|z|'):
        Z = np.absolute(_data)

    #print(_originRadius)
    #print(_distanceToOrigin)
    
    Z1 = np.where(_distanceToOrigin <= _originRadius, 0, Z)
    Z2 = np.where(Z1 >= _receivedValue, 1, 0)  
    Z3 = np.sum(Z2, axis=1)
    Z4 = np.sum(Z1, axis=1)

    ax = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    #n, bins, patches = ax.hist(_energie, 100, weights=np.ones(iterations) / iterations) #for random positions

    n, bins, patches = ax.hist(Z3, 100, weights=np.ones(iterations) / iterations)
    mu, sigma = norm.fit(Z3)
    best_fit_line = norm.pdf(bins, mu, sigma)
    ax.plot(bins, best_fit_line * np.sum(np.diff(bins) * n), '--')


    n, bins, patches = ax2.hist(Z4, 100, weights=np.ones(iterations) / iterations)
    mu, sigma = norm.fit(Z4)
    best_fit_line = norm.pdf(bins, mu, sigma)
    ax2.plot(bins, best_fit_line * np.sum(np.diff(bins) * n), '--')

    ax2.set_ylabel('Probability')
    ax2.set_xlabel('Summed signals at all Receiver')
    #ax.set_xlabel('Used energie')
    ax.set_ylabel('Probability')
    ax.set_xlabel('Receiver received signal at least signal value')

    ax.set_title( '{0}, #R = {1}, #S = {2}, Iter = {3}, {4}'.format(_algorithm, _receiverNumber, _senderNumber, iterations, _formation) + "\n"+ r'$\lambda = {0}$'.format(_waveLenght) 
                    + ' loss = {0}, b = {1}, radius = {2}, signal value = {3}'.format(_pathLoss, _b, _radius, _receivedValue))

    fig.tight_layout(pad=2.0)

    return fig