import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from matplotlib import cm
from flask import session
import numpy as np
import cmath

def CreateFigure(_model:float, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale):

    if(_plotTyp == 'all'):
        i, j, n = 2,2,1
        fig = plt.figure(figsize=(7, 6.2))
    else:
        i, j, n = 1,1,1
        fig = plt.figure(figsize=(7, 6.2))

    if(_dimension == '3d'):
        projection = '3d'
    else:
        projection = None

    if(_plotTyp == 'all' or _plotTyp == 'real'):
        ax = fig.add_subplot(i, j, n, projection=projection)
        n += 1
        Z = _model[2].real
        ax.set_title("real")
        InitFigure(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale)

    if(_plotTyp == 'all' or _plotTyp == 'imag'):
        ax = fig.add_subplot(i, j, n, projection=projection)
        n += 1
        Z = _model[2].imag
        ax.set_title("imag")
        InitFigure(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale)

    if(_plotTyp == 'all' or _plotTyp == '|z|^2'):
        ax = fig.add_subplot(i, j, n, projection=projection)
        n += 1
        Z = np.square(np.absolute(_model[2]))
        ax.set_title(r'$|z|^2$')
        InitFigure(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale)

    # if(_plotTyp == 'all' or _plotTyp == '|a| + |b|'):
    #     ax = fig.add_subplot(i, j, n, projection=projection)
    #     n += 1
    #     Z = np.fabs(_model[2].real) + np.fabs(_model[2].imag)

    #     ax.set_title(r'$|a| + |b|$')
    #     InitFigure(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale)


    if(_plotTyp == 'all' or _plotTyp == '|z|'):
        ax = fig.add_subplot(i, j, n, projection=projection)
        n += 1
        Z = np.sqrt(np.square(_model[2].real) + np.square(_model[2].imag))
        ax.set_title(r'$|z|$')
        InitFigure(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale)

    # if(_plotTyp == 'all' or _plotTyp == 'phase'):
    #     ax = fig.add_subplot(i, j, n, projection=projection)
    #     n += 1
    #     Z = np.angle(_model[2])
    #     ax.set_title("phase")
    #     InitFigure(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale)

    fig.tight_layout()
    return fig

def InitFigureScatter3d(ax, fig, _Z ,_model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax):
    Z = _Z
    if(session['cutOrigin_RD']):
        originRadius = session['originRadius_RD']
        distanceOrigin = np.sqrt(np.square(_model[0]) + np.square(_model[1]))
        Z = np.where(distanceOrigin <= originRadius, None, Z)
    # if(_vmin != None):
    #     Z = np.where((Z <= _vmin), None, Z)
    #Z = np.where(_model[3] > _radius, None, Z)
    XX,YY = np.where(Z == None, None, (_model[0], _model[1]))
    if _orientation == 'Horizontal':
        cs = ax.scatter(XX, YY,_receiverPos[2], c=Z, s=0.1,cmap=plt.get_cmap(_colors), alpha=1, vmin=_vmin, vmax=_vmax)
    else:
        cs = ax.scatter(XX, YY,_receiverPos[1], c=Z, s=0.1,cmap=plt.get_cmap(_colors), zdir='y', alpha=1, vmin=_vmin, vmax=_vmax)
    ax.set_zlim(_receiverPos[2] - _radius, _receiverPos[2] + _radius)
    ax.set_ylim(_receiverPos[1] - _radius, _receiverPos[1] + _radius)
    ax.set_xlim(_receiverPos[0] - _radius, _receiverPos[0] + _radius)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.colorbar(cs, ax=ax)

def InitFigureScatter2d(ax, fig, _Z,_model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _debug = False):
    #Z = np.where((Z >= _vmin) | (Z <= _vmax), None, Z)
    #Z = np.where(_model[3] > _radius, None, Z)
    Z = _Z
    if(session['cutOrigin_RD']):
        originRadius = session['originRadius_RD']
        distanceOrigin = np.sqrt(np.square(_model[0]) + np.square(_model[1]))
        Z = np.where(distanceOrigin <= originRadius, None, Z)

    XX,YY = _model[0], _model[1]
    if _orientation == 'Horizontal':
        cs = ax.scatter(XX, YY,  s=0.1, c=Z, cmap=plt.get_cmap(_colors), alpha=1, vmin=_vmin, vmax=_vmax)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_ylim(_receiverPos[1] - _radius, _receiverPos[1] + _radius)
        ax.set_xlim(_receiverPos[0] - _radius, _receiverPos[0] + _radius)
    else:
        cs = ax.scatter(XX, YY,  s=0.1, c=Z, cmap=plt.get_cmap(_colors), alpha=1, vmin=_vmin, vmax=_vmax)
        ax.set_xlabel('X')
        ax.set_ylabel('Z')
        ax.set_ylim(_receiverPos[2] - _radius, _receiverPos[2] + _radius)
        ax.set_xlim(_receiverPos[0] - _radius, _receiverPos[0] + _radius)
    fig.colorbar(cs, ax=ax)

def InitFigure(ax, fig, Z,_model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax, _plotTyp, _dimension, _logScale):
    if(_logScale):
        Z = np.log(Z)
    if(_dimension == '3d'):
        InitFigureScatter3d(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax)
    else:
        InitFigureScatter2d(ax, fig, Z , _model, _colors, _receiverPos, _radius, _orientation, _vmin, _vmax)