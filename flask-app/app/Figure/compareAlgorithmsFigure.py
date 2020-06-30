import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
import matplotlib.mlab as mlab
from matplotlib import cm
from flask import session
from scipy.stats import norm
import numpy as np
import cmath

def CreateCompareAlgorithmsFigure(_algorithms, _data, _energie, _signalType, _minReceivedValue, _range, _originRadius, _distanceToOrigin):

    singalValues = np.arange(_minReceivedValue, _minReceivedValue + _range, _range / 100 )

    fig, ax = plt.subplots(figsize=(7.25, 6))

    for i in range(0,len(_algorithms)):
        res = []

        if(_signalType == 'real'):
            Z = _data[i].real

        elif(_signalType == 'imag'):
            Z = _data[i].imag

        elif(_signalType == '|z|^2'):
            Z = np.square(np.absolute(_data[i]))

        elif(_signalType == '|z|'):
            Z = np.absolute(_data[i])
        
        Z1 = np.where(_distanceToOrigin[i] <= _originRadius, float('-inf'), Z)

        for s in singalValues:
            Z2 = np.where(Z1 > s, 1, 0)  
            res.append(np.sum(Z2))
        ax.plot(singalValues, res, label=_algorithms[i])

    plt.subplots_adjust(left=0.1)
    ax.set(xlabel='Signal Value', ylabel='#Receiver')
    ax.grid()

    ax.set_xlim()

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 1, box.height - 0.05])
    legend1 = ax.legend(_energie, bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',title="Used energy sum(a)",
           ncol=4, mode="expand", borderaxespad=0.)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    ax.legend(bbox_to_anchor=(1, 0.5))
    ax.legend(bbox_to_anchor=(1.1, 1.00))

    ax.add_artist(legend1)



    return fig