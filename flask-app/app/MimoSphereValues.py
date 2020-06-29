from flask import session

def GetMimoSphereValues():
    if 'senderNumberMimo3d' not in session:
        session['senderNumberMimo3d'] = 10000

    if 'receiverNumberMimo3d' not in session:
        session['receiverNumberMimo3d'] = 10000

    if 'receiverOriginMimo3d' not in session:
        session['receiverOriginMimo3d'] = (0,0,0)

    if 'radiusMimo3d' not in session:
        session['radiusMimo3d'] = 2

    if 'wavelengthMimo3d' not in session:
        session['wavelengthMimo3d'] = 0.1

    if 'pathLossMimo3d' not in session:
        session['pathLossMimo3d'] = 2

    if 'bValueMimo3d' not in session:
        session['bValueMimo3d'] = 1

    if 'algorithmMimo3d' not in session:
        session['algorithmMimo3d'] = 'Parametrized Supernova'

    if 'randomSeedMimo3d' not in session:
        session['randomSeedMimo3d'] = 1

    if 'isotropic_RS' not in session:
        session['isotropic_RS'] = False

    if 'color' not in session:
        session['color'] = 'Greys'

    if 'vmin' not in session:
        session['vmin'] = -1

    if 'vmax' not in session:
        session['vmax'] = 1

    if 'plotTypMimo3d' not in session:
        session['plotTypMimo3d'] = '|z|^2'
    
    if 'useMin' not in session:
        session['useMin'] = True

    if 'useMax' not in session:
        session['useMax'] = True

    if 'logScale' not in session:
        session['logScale'] = False

    if 'cutOrigin_RS' not in session:
        session['cutOrigin_RS'] = True

    if 'originRadius_RS' not in session:
        session['originRadius_RS'] = 1

    if 'elevation_RS' not in session:
        session['elevation_RS'] = 30

    if 'azimuth_RS' not in session:
        session['azimuth_RS'] = 30



    return(session['senderNumberMimo3d'], session['receiverNumberMimo3d'], session['receiverOriginMimo3d'], 
            session['radiusMimo3d'], session['wavelengthMimo3d'], session['pathLossMimo3d'], session['bValueMimo3d'],
            session['algorithmMimo3d'], session['randomSeedMimo3d'], session['color'], session['vmin'], session['vmax'], 
            session['plotTypMimo3d'], session['useMin'], session['useMax'], session['logScale'], session['isotropic_RS'],
            session['cutOrigin_RS'], session['originRadius_RS'], session['elevation_RS'], session['azimuth_RS'])


def ValuesChanged(form, _debug = False):
    if  (
        session['randomSeedMimo3d'] != form.randomSeed.data or
        session['receiverNumberMimo3d'] != form.numberReceiver.data or
        session['senderNumberMimo3d'] != form.numberSender.data or
        session['receiverOriginMimo3d'] != (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  or
        session['radiusMimo3d'] != form.radius.data or
        session['isotropic_RS'] != form.isotropic.data or
        session['wavelengthMimo3d'] != form.wavelength.data or
        session['pathLossMimo3d'] != form.pathLoss.data or
        session['bValueMimo3d'] != form.bValue.data or
        session['algorithmMimo3d'] != form.algorithms.data):
        if _debug:
            print("Values changed")
        return True
    else:
        if _debug:
            print("Values not changed")
        return False
