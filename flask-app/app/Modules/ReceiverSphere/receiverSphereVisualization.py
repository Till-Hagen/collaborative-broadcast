import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from textwrap import wrap
from matplotlib import cm
import numpy as np
from flask import session
import cmath
from Modules.ReceiverSphere.receiverSphereSession import GetReceiverSphereValues

def CreateFigure(_model, _debug = False):

    if _debug:
        print("Create mimo sphare figure")

    values = GetReceiverSphereValues()

    receiverOrigin = values[2]
    radius = values[3]
    color = values[9]
    vmin = values[10]
    vmax = values[11]
    plotTyp = values[12]
    useMin = values[13]
    useMax = values[14]
    azimuth = session['azimuth_RS']
    elevation = session['elevation_RS']
    plotTyp = session['plotTyp_RS']
    

    if not useMin:
        vmin = None
    if not useMax:
        vmax = None

    fig = plt.figure(figsize=(7, 6.2))
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    if(plotTyp == 'real'):
        Z = _model[3].real


    if(plotTyp == 'imag'):
        Z = _model[3].imag

    if(plotTyp == '|z|^2'):
        Z = np.square(np.absolute(_model[3]))

    if(plotTyp == '|z|'):
        Z = np.sqrt(np.square(_model[3].real) + np.square(_model[3].imag))

    if(session['cutOrigin_RS'] and useMin):
        originRadius = session['originRadius_RS']
        distanceOrigin = np.sqrt(np.square(_model[0]) + np.square(_model[1]) + np.square(_model[2]))
        Z = np.where(np.logical_or(distanceOrigin <= originRadius, Z <= vmin), None, Z)

    elif useMin:
        Z = np.where(Z <= vmin, None, Z)

    elif(session['cutOrigin_RS']):
        originRadius = session['originRadius_RS']
        distanceOrigin = np.sqrt(np.square(_model[0]) + np.square(_model[1]) + np.square(_model[2]))
        Z = np.where(distanceOrigin <= originRadius, None, Z)

    XX = np.where((Z == None), None,_model[0])
    YY = np.where((Z == None), None,_model[1])
    ZZ = _model[2]
    cs = ax.scatter(XX, YY,ZZ, c=Z, s=0.1,cmap=plt.get_cmap(color), alpha=1, vmin=vmin, vmax=vmax)
    #cs = ax.scatter(XX, YY,ZZ, c="Grey", s=0.1, alpha=1)
    fig.colorbar(cs, ax=ax)
    ax.set_title("Receiver sphere")
    ax.set_zlim(receiverOrigin[2] - radius, receiverOrigin[2] + radius)
    ax.set_ylim(receiverOrigin[1] - radius, receiverOrigin[1] + radius)
    ax.set_xlim(receiverOrigin[0] - radius, receiverOrigin[0] + radius)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.view_init(elevation, azimuth)

    plt.tight_layout()

    if _debug:
        print("End Create mimo sphare figure")
    return fig