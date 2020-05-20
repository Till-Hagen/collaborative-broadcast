from flask import session

def GetMisoValues():
    if 'numberSenderMiso' not in session:
        session['numberSenderMiso'] = 100

    if 'receiverPos' not in session:
        session['receiverPos'] = (7,0,0)

    if 'wavelength' not in session:
        session['wavelength'] = 0.1

    if 'pathLoss' not in session:
        session['pathLoss'] = 2

    if 'algorithm' not in session:
        session['algorithm'] = 'Parametrized Supernova'

    if 'color' not in session:
        session['color'] = 'Greys'

    if 'bvalue' not in session:
        session['bvalue'] = 1

    if 'randomSeed' not in session:
        session['randomSeed'] = 1

    if 'dimension' not in session:
        session['dimension'] = '2d'

    if 'misoPlotTyp' not in session:
        session['misoPlotTyp'] = 'real'


    return (session['numberSenderMiso'], session['receiverPos'], session['wavelength'], 
            session['pathLoss'], session['bvalue'], session['algorithm'], session['color'], 
            session['randomSeed'], session['dimension'], session['misoPlotTyp'])


def ValuesChanged(form):
    if  (
        session['numberReceiver'] != form.numberReceiver.data or
        session['randomSeed'] != form.randomSeed.data or
        session['numberSender'] != form.numberSender.data or
        session['receiverPos'] != (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  or
        session['radius'] != form.radius.data or
        session['orientation'] != form.orientation.data or
        session['wavelength'] != form.wavelength.data or
        session['pathLoss'] != form.pathLoss.data or
        session['bvalue'] != form.b.data or
        session['formation'] != form.formation.data or
        session['algorithm'] != form.algorithms.data):
        print("Values changed")
        return True
    else:
        print("Values not changed")
        return False



def GetMimoValues():
    if 'numberReceiver' not in session:
        session['numberReceiver'] = 100000

    if 'numberSender' not in session:
        session['numberSender'] = 100

    if 'receiverPosMimo' not in session:
        session['receiverPosMimo'] = (0,0,0)

    if 'radius' not in session:
        session['radius'] = 15.0

    if 'orientation' not in session:
        session['orientation'] = 'Horizontal'

    if 'wavelength' not in session:
        session['wavelength'] = 0.1

    if 'pathLoss' not in session:
        session['pathLoss'] = 2

    if 'bvalue' not in session:
        session['bvalue'] = 1

    if 'algorithm' not in session:
        session['algorithm'] = 'Parametrized Supernova'

    if 'color' not in session:
        session['color'] = 'Greys'

    if 'vmin' not in session:
        session['vmin'] = -1

    if 'vmax' not in session:
        session['vmax'] = 1

    if 'plotTyp' not in session:
        session['plotTyp'] = 'all'

    if 'dimension' not in session:
        session['dimension'] = '2d'
    
    if 'randomSeed' not in session:
        session['randomSeed'] = 1
    
    if 'useMin' not in session:
        session['useMin'] = True

    if 'useMax' not in session:
        session['useMax'] = True
    
    if 'formation' not in session:
        session['formation'] = 'grid'

    if 'logScale' not in session:
        session['logScale'] = True

    return (session['numberReceiver'], session['numberSender'], session['receiverPosMimo'], session['radius'],
             session['orientation'], session['wavelength'], session['pathLoss'], session['bvalue'], 
             session['algorithm'], session['color'], session['vmin'], session['vmax'], session['plotTyp'], 
             session['dimension'], session['randomSeed'], session['useMin'], session['useMax'], session['formation'], session['logScale'])