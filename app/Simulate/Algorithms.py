from numba import jit, prange
import cmath
import math
import numpy as np

def ExecuteAlgorithm(_algorithm ,_X, _Y, _wavelength, _b):
    if(_algorithm == 'Parametrized Supernova'):
        return ParametrizedSupernova(_X, _Y, _wavelength, _b)
    elif(_algorithm == 'Alternating Supernova'):
        return AlternatingSupernova(_X, _Y, _wavelength, _b)

def ParametrizedSupernova(_X, _Y, _wavelength, _b):
    senderDist = np.sqrt(np.square(_X) + np.square(_Y))
    cons = 2 * cmath.pi / _wavelength
    varphi =  _b * cons * senderDist 
    return varphi

def AlternatingSupernova(_X, _Y, _wavelength, _b):
    senderDist = np.sqrt(np.square(_X) + np.square(_Y))
    senderXplusY = _X +_Y
    b = np.where(senderXplusY < 0, _b, -_b)
    cons = 2 * cmath.pi / _wavelength
    varphi =  b * cons * senderDist 
    return varphi

@jit(nopython=True, nogil=True)
def SignalAtReceiver(receiverPos, X, Y, varphi, _wavelength, _pathloss):
    
    #distance ||s_j||
    senderDist = np.sqrt(np.square(X) + np.square(Y))

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

    #quotient * sin^2(Theta(r - s_j))
    result = quotient * sin_theta

    #Create circle 
    circle_result =  np.where(senderDist < 1.0, result, 0 + 0j)

    return circle_result