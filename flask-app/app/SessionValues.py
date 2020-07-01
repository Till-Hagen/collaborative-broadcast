from flask import session

def GetMisoValues():

    if 'numberSenderMiso' not in session:
        session['numberSenderMiso'] = 10000

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
        session['dimension'] = '3d'

    if 'misoPlotTyp' not in session:
        session['misoPlotTyp'] = 'real'

    if 'isotropic_S' not in session:
        session['isotropic_S'] = False


    return (session['numberSenderMiso'], session['receiverPos'], session['wavelength'], 
            session['pathLoss'], session['bvalue'], session['algorithm'], session['color'], 
            session['randomSeed'], session['dimension'], session['misoPlotTyp'], session['isotropic_S'])