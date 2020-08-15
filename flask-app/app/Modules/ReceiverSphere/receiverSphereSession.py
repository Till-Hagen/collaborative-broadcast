from flask import session

def GetReceiverSphereValues():
    if 'senderNumber_RS' not in session:
        session['senderNumber_RS'] = 10000

    if 'receiverNumber_RS' not in session:
        session['receiverNumber_RS'] = 10000

    if 'receiverOrigin_RS' not in session:
        session['receiverOrigin_RS'] = (0,0,0)

    if 'radius_RS' not in session:
        session['radius_RS'] = 2

    if 'wavelength_RS' not in session:
        session['wavelength_RS'] = 0.1

    if 'pathLoss_RS' not in session:
        session['pathLoss_RS'] = 2

    if 'bValue_RS' not in session:
        session['bValue_RS'] = 1

    if 'algorithm_RS' not in session:
        session['algorithm_RS'] = 'Parametrized Supernova'

    if 'randomSeed_RS' not in session:
        session['randomSeed_RS'] = 1

    if 'isotropic_RS' not in session:
        session['isotropic_RS'] = False

    if 'color_RS' not in session:
        session['color_RS'] = 'Greys'

    if 'vmin_RS' not in session:
        session['vmin_RS'] = -1

    if 'vmax_RS' not in session:
        session['vmax_RS'] = 1

    if 'plotTyp_RS' not in session:
        session['plotTyp_RS'] = '|z|^2'
    
    if 'useMin_RS' not in session:
        session['useMin_RS'] = True

    if 'useMax_RS' not in session:
        session['useMax_RS'] = True

    if 'logScale_RS' not in session:
        session['logScale_RS'] = False

    if 'cutOrigin_RS' not in session:
        session['cutOrigin_RS'] = True

    if 'originRadius_RS' not in session:
        session['originRadius_RS'] = 1

    if 'elevation_RS' not in session:
        session['elevation_RS'] = 30

    if 'azimuth_RS' not in session:
        session['azimuth_RS'] = 30

    if 'saveData_RS' not in session:
        session['saveData_RS'] = False


    return(session['senderNumber_RS'], session['receiverNumber_RS'], session['receiverOrigin_RS'], 
            session['radius_RS'], session['wavelength_RS'], session['pathLoss_RS'], session['bValue_RS'],
            session['algorithm_RS'], session['randomSeed_RS'], session['color_RS'], session['vmin_RS'], session['vmax_RS'], 
            session['plotTyp_RS'], session['useMin_RS'], session['useMax_RS'], session['logScale_RS'], session['isotropic_RS'],
            session['cutOrigin_RS'], session['originRadius_RS'], session['elevation_RS'], session['azimuth_RS'])


def ValuesChanged(form, _debug = False):
    if  (
        session['randomSeed_RS'] != form.randomSeed.data or
        session['receiverNumber_RS'] != form.numberReceiver.data or
        session['senderNumber_RS'] != form.numberSender.data or
        session['receiverOrigin_RS'] != (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  or
        session['radius_RS'] != form.radius.data or
        session['isotropic_RS'] != form.isotropic.data or
        session['wavelength_RS'] != form.wavelength.data or
        session['pathLoss_RS'] != form.pathLoss.data or
        session['bValue_RS'] != form.bValue.data or
        session['algorithm_RS'] != form.algorithms.data):
        if _debug:
            print("Values changed")
        return True
    else:
        if _debug:
            print("Values not changed")
        return False
