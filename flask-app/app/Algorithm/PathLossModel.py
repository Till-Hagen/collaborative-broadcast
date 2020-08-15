from numba import jit, prange
import cmath
import math
import numpy as np
import models
import sys

@jit(nopython=True, nogil=True)
def SignalAtReceiver(receiverPos, X, Y, varphi, _a, _wavelength, _pathloss, _isotropic):
    
    #distance ||s_j||
    #senderDist = np.sqrt(np.square(X) + np.square(Y))

    cons = (2 * cmath.pi / _wavelength)

    #distance ||r - s_j||
    dist_to_receiver = np.sqrt(np.square(X - receiverPos[0]) + np.square(Y - receiverPos[1]) + np.square(receiverPos[2]))

    # varphi - (2pi/lambda * ||r - s_j|| )
    varphi_cons_dist = varphi - (dist_to_receiver * cons)

    #cast to complex number 
    complex_res = varphi_cons_dist * 1j

    #e^{i * (varphi - (2pi/lambda * ||r - s_j|| ) }
    exp_res = np.exp(complex_res)

    #divisor ( ||r - s_j|| )^{a / 2}
    divisor = np.power(dist_to_receiver, (_pathloss / 2))

    quotient = exp_res / divisor

    #sin^2(Theta(r - s_j))
    sinX = receiverPos[0] - X

    sinY = receiverPos[1] - Y

    distance_sin_XY = np.sqrt(np.square(sinX) + np.square(sinY))

    distance_sin_XYZ = np.sqrt(np.square(sinX) + np.square(sinY) + np.square(receiverPos[2]))

    sin_theta = np.square(distance_sin_XY / distance_sin_XYZ)

    quotient = quotient * _a

    #quotient * sin^2(Theta(r - s_j))
    if(_isotropic):
        return quotient
    
    return quotient * sin_theta