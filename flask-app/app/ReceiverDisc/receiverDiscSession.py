from flask import session

def InitSession():
    if 'numberReceiver_RD' not in session:
        session['numberReceiver_RD'] = 10000

    if 'numberSender_RD' not in session:
        session['numberSender_RD'] = 10000

    if 'receiverPos_RD' not in session:
        session['receiverPos_RD'] = (0,0,0)

    if 'radius_RD' not in session:
        session['radius_RD'] = 15.0

    if 'orientation_RD' not in session:
        session['orientation_RD'] = 'Horizontal'

    if 'wavelength_RD' not in session:
        session['wavelength_RD'] = 0.1

    if 'pathLoss_RD' not in session:
        session['pathLoss_RD'] = 2

    if 'bvalue_RD' not in session:
        session['bvalue_RD'] = 1

    if 'algorithm_RD' not in session:
        session['algorithm_RD'] = 'Parametrized Supernova'

    if 'color_RD' not in session:
        session['color_RD'] = 'Greys'

    if 'vmin_RD' not in session:
        session['vmin_RD'] = 0

    if 'vmax_RD' not in session:
        session['vmax_RD'] = 1

    if 'plotTyp_RD' not in session:
        session['plotTyp_RD'] = 'all'

    if 'dimension_RD' not in session:
        session['dimension_RD'] = '3d'
    
    if 'randomSeed_RD' not in session:
        session['randomSeed_RD'] = 1
    
    if 'useMin_RD' not in session:
        session['useMin_RD'] = True

    if 'useMax_RD' not in session:
        session['useMax_RD'] = False
    
    if 'formation_RD' not in session:
        session['formation_RD'] = 'grid'

    if 'logScale_RD' not in session:
        session['logScale_RD'] = False

    if 'isotropic_RD' not in session:
        session['isotropic_RD'] = False
        
    if 'cutOrigin_RD' not in session:
        session['cutOrigin_RD'] = True

    if 'originRadius_RD' not in session:
        session['originRadius_RD'] = 2

def ValuesChanged(form):
    if  (
        session['numberReceiver_RD'] != form.numberReceiver.data or
        session['randomSeed_RD'] != form.randomSeed.data or
        session['numberSender_RD'] != form.numberSender.data or
        session['receiverPos_RD'] != (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  or
        session['radius_RD'] != form.radius.data or
        session['orientation_RD'] != form.orientation.data or
        session['wavelength_RD'] != form.wavelength.data or
        session['pathLoss_RD'] != form.pathLoss.data or
        session['bvalue_RD'] != form.b.data or
        session['formation_RD'] != form.formation.data or
        session['algorithm_RD'] != form.algorithms.data):
        return True
    else:
        return False