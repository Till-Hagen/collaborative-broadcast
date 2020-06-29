import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from matplotlib import cm
import numpy as np
import cmath

def CreateMisoSenderFigure(_model, _colors, _receiverPos, _wavelength,_pathLoss,_b, _dimension, _plotTyp, _debug = False):

    fig = plt.figure(figsize=(7, 6.2))

    if(_plotTyp == 'real'):
        Z = _model[2].real

    if(_plotTyp == 'imag'):
        Z = _model[2].imag

    if(_plotTyp == '|z|^2'):
        Z = np.square(np.absolute(_model[2]))

    if(_plotTyp == '|a| + |b|'):
        Z = np.absolute(_model[2].real) + np.absolute(_model[2].imag)

    if(_plotTyp == '|z|'):
        Z = np.absolute(_model[2])

    if(_plotTyp == 'phase'):
        Z = np.angle(_model[2])

    #Z = np.where(_model[3] > 1, None, Z)
    XX,YY = _model[0], _model[1]
    if(_dimension == '3d'):

        ax = fig.add_subplot(1, 1, 1, projection='3d')
        cs = ax.scatter(XX, YY,0, c=Z, s=0.1,cmap=plt.get_cmap('Greys'), alpha=1)
        ax.set_zlabel('Z')
        ax.set_zlim(-1, 1)
    else:
        ax = fig.add_subplot(1, 1, 1, projection=None)
        cs = ax.scatter(XX, YY,  s=0.1, c=Z, cmap=plt.get_cmap(_colors), alpha=1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    fig.colorbar(cs, ax=ax)
    #sumString = r'$\sum_{j=1}^n \frac{a_je^{i(\phi_j - \frac{2\pi}{\lambda}(||r-s_j||_2))}}{(||r-s_j||_2)^{\alpha/2}}sin^2(\Theta(r-s_j))=$'
    #ax.set_xlabel(sumString + "\n" + "\n".join(wrap(str(np.sum(_model[2])), 50)), fontsize=12)
    #ax.set_title(r'$\lambda = {0}$'.format(_wavelength) + ' loss = {0}, b = {1}'.format(_pathLoss, _b))
    ax.title.set_position([.5, 1.05])
    #ax.set_title("Signal at Receiver: " + str(np.sum(_model[2])))
    fig.tight_layout()
    return fig
