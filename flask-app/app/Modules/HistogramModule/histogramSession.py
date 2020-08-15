from flask import session

def InitSession():
    if 'numberSender_AC' not in session:
        session['numberSender_AC'] = 10

    if 'numberReceiver_AC' not in session:
        session['numberReceiver_AC'] = 1000

    if 'receiverOrigin_AC' not in session:
        session['receiverOrigin_AC'] = (0,0,0)

    if 'radius_AC' not in session:
        session['radius_AC'] = 100.0

    if 'wavelength_AC' not in session:
        session['wavelength_AC'] = 0.1

    if 'pathLoss_AC' not in session:
        session['pathLoss_AC'] = 2

    if 'bValue_AC' not in session:
        session['bValue_AC'] = 1

    if 'randomSeed_AC' not in session:
        session['randomSeed_AC'] = 1

    if 'isotropic_AC' not in session:
        session['isotropic_AC'] = False

    if 'formation_AC' not in session:
        session['formation_AC'] = 'sphere'

    if 'receivedValue_AC' not in session:
        session['receivedValue_AC'] = 0.02

    if 'signalType_AC' not in session:
        session['signalType_AC'] = '|z|'

    if 'originRadius_AC' not in session:
        session['originRadius_AC'] = 0

    if 'iterations_AC' not in session:
        session['iterations_AC'] = 2000

    if 'minRange_AC' not in session:
        session['minRange_AC'] = 400

    if 'maxRange_AC' not in session:
        session['maxRange_AC'] = 700

    if 'topRange_AC' not in session:
        session['topRange_AC'] = 0.1

    if 'saveData_AC' not in session:
        session['saveData_AC'] = False

    if 'algorithm_AC' not in session:
        session['algorithm_AC'] = 'Parametrized Supernova'

def ValuesChanged(form):
    if  (
        session['numberReceiver_AC'] != form.numberReceiver.data or
        session['numberSender_AC'] != form.numberSender.data or
        session['receiverOrigin_AC'] != (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  or
        session['radius_AC'] != form.radius.data or
        session['wavelength_AC'] != form.wavelength.data or
        session['pathLoss_AC'] != form.pathLoss.data or
        session['bValue_AC'] != form.bValue.data or
        session['algorithm_AC'] != form.algorithms.data or
        session['formation_AC'] != form.formation.data or
        session['randomSeed_AC'] != form.randomSeed.data or
        session['iterations_AC'] != form.iterations.data or
        session['isotropic_AC'] != form.isotropic.data):
        return True
    else:
        return False
