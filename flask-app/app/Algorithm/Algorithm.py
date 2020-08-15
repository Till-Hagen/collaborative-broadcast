from numba import jit, prange
import cmath
import math
import numpy as np
import models
import sys

def ExecuteAlgorithm(_algorithm ,_X, _Y, _wavelength, _b):
    if(_algorithm == 'Parametrized Supernova'):
        return ParametrizedSupernova(_X, _Y, _wavelength, _b)
    # elif(_algorithm == 'Alternating Supernova'):
    #     return AlternatingSupernova(_X, _Y, _wavelength, _b)
    else:
        #TestAlgorithm(_algorithm ,_X, _Y, _wavelength, _b)
        return RunCunstomAlgorithm(_algorithm,_X, _Y, _wavelength, _b)

def TestAlgorithm(_algorithmName,_executionString):
    try:
        _X = np.array([1, 2, 3, 23 ,42])
        _Y = np.array([1, 2, 3, 23 ,12])
        defString = 'def ' + _algorithmName.replace(" ", "") + '(_X, _Y, _wavelength, _b):\r\n'
        code = defString + _executionString
        eval(compile(code.replace('\n', '\n    '), '<string>', 'exec'))
        res1, res2 = eval(_algorithmName.replace(" ", "") + '(_X, _Y, 0.1, 1)')
        if(np.shape(res1) == np.shape(_X) and np.shape(res2) == np.shape(_X)):
            return (True, "seems legit")
        else:
            return (False, "Return must be a tuple (a, b), a and b type ndarray same shape as _X and _Y")
    except Exception as inst:
        return (False, repr(type(inst)) + "\n" + repr(inst.args) + "\n" + repr(inst))

def RunCunstomAlgorithm(_algorithm ,_X, _Y, _wavelength, _b):
    algorithmModel = models.Algorithm.query.filter_by(algorithmName=_algorithm).first()
    defString = 'def ' + algorithmModel.algorithmName.replace(" ", "") + '(_X, _Y, _wavelength, _b):\r\n'
    code = defString + algorithmModel.exceString
    eval(compile(code.replace('\n', '\n    '), '<string>', 'exec'))
    return eval(algorithmModel.algorithmName.replace(" ", "") + '(_X, _Y, _wavelength, _b)')

def ParametrizedSupernova(_X, _Y, _wavelength, _b):
    senderDist = np.sqrt(np.square(_X) + np.square(_Y))
    cons = 2 * cmath.pi / _wavelength
    varphi =  -_b * cons * senderDist 
    a = np.ones(_X.shape)
    return (varphi, a)

# def AlternatingSupernova(_X, _Y, _wavelength, _b):
#     senderDist = np.sqrt(np.square(_X) + np.square(_Y))
#     senderXplusY = _X +_Y
#     b = np.where(senderXplusY < 0, _b, -_b)
#     cons = 2 * cmath.pi / _wavelength
#     varphi =  b * cons * senderDist 
#     return (varphi, 1)

# #@jit(nopython=True, nogil=True)
# def SignalAtReceiver(receiverPos, X, Y, varphi, _a, _wavelength, _pathloss, _isotropic):
    
#     #distance ||s_j||
#     #senderDist = np.sqrt(np.square(X) + np.square(Y))

#     cons = (2 * cmath.pi / _wavelength)

#     #distance ||r - s_j||
#     dist_to_receiver = np.sqrt(np.square(X - receiverPos[0]) + np.square(Y - receiverPos[1]) + np.square(receiverPos[2]))

#     # varphi - (2pi/lambda * ||r - s_j|| )
#     varphi_cons_dist = varphi - (dist_to_receiver * cons)

#     #cast to complex number 
#     complex_res = varphi_cons_dist * 1j

#     #e^{i * (varphi - (2pi/lambda * ||r - s_j|| ) }
#     exp_res = np.exp(complex_res)

#     #divisor ( ||r - s_j|| )^{a / 2}
#     divisor = np.power(dist_to_receiver, (_pathloss / 2))

#     quotient = exp_res / divisor

#     #sin^2(Theta(r - s_j))
#     sinX = receiverPos[0] - X

#     sinY = receiverPos[1] - Y

#     distance_sin_XY = np.sqrt(np.square(sinX) + np.square(sinY))

#     distance_sin_XYZ = np.sqrt(np.square(sinX) + np.square(sinY) + np.square(receiverPos[2]))

#     sin_theta = np.square(distance_sin_XY / distance_sin_XYZ)

#     quotient = quotient * _a

#     #quotient * sin^2(Theta(r - s_j))
#     if(_isotropic):
#         return quotient
    
#     return quotient * sin_theta