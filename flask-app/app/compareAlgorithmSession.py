from flask import session

def InitCompareAlgorithmSession():
    if 'numberSender_C' not in session:
        session['numberSender_C'] = 10000

    if 'numberReceiver_C' not in session:
        session['numberReceiver_C'] = 10000

    if 'receiverOrigin_C' not in session:
        session['receiverOrigin_C'] = (0,0,0)

    if 'radius_C' not in session:
        session['radius_C'] = 100.0

    if 'wavelength_C' not in session:
        session['wavelength_C'] = 0.1

    if 'pathLoss_C' not in session:
        session['pathLoss_C'] = 2

    if 'bValue_C' not in session:
        session['bValue_C'] = 1

    if 'randomSeed_C' not in session:
        session['randomSeed_C'] = 1

    if 'isotropic_C' not in session:
        session['isotropic_C'] = False

    if 'formation_C' not in session:
        session['formation_C'] = 'sphere'

    if 'minReceivedValue_C' not in session:
        session['minReceivedValue_C'] = 1

    if 'signalType_C' not in session:
        session['signalType_C'] = '|z|'

    if 'originRadius_C' not in session:
        session['originRadius_C'] = 0

    if 'plotRange_C' not in session:
        session['plotRange_C'] = 20

def ValuesChanged(form):
    if  (
        session['numberReceiver_C'] != form.numberReceiver.data or
        session['numberSender_C'] != form.numberSender.data or
        session['receiverOrigin_C'] != (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  or
        session['radius_C'] != form.radius.data or
        session['wavelength_C'] != form.wavelength.data or
        session['pathLoss_C'] != form.pathLoss.data or
        session['bValue_C'] != form.bValue.data or
        session['formation_C'] != form.formation.data or
        session['randomSeed_C'] != form.randomSeed.data or
        session['isotropic_C'] != form.isotropic.data):
        print("Values changed")
        return True
    else:
        print("Values not changed")
        return False
