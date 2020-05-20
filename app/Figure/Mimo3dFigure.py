import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from matplotlib import cm
import numpy as np
import cmath

def CreateMimo3dFigure(_model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension):

    fig = plt.figure(figsize=(7, 6.2))
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    for value_receiver, receiverPos in _model[2]:
        Z = np.absolute(value_receiver)
        #Z = np.where((Z <= _vmin), None, Z)
        Z = np.where(_model[3] > _radius, None, Z)
        XX,YY = np.where(Z == None, None, (_model[0], _model[1]))
        cs = ax.scatter(XX, YY,receiverPos[2], c=Z, s=0.1,cmap=plt.get_cmap(_colors), alpha=0.8, vmin=_vmin, vmax=_vmax)
    
    fig.colorbar(cs, ax=ax)
    ax.set_title("Mimo 3d")
    ax.set_zlim(_receiverPos[2] - _radius, _receiverPos[2] + _radius)
    ax.set_ylim(_receiverPos[1] - _radius, _receiverPos[1] + _radius)
    ax.set_xlim(_receiverPos[0] - _radius, _receiverPos[0] + _radius)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.tight_layout()
    return fig