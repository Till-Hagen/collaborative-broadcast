from flask import Flask, render_template ,make_response, url_for, flash, redirect
import SimulationVisualizationInterface.analyzeAlgorithmInterface as cFigure
import io
from flask import Response, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from froms import SimulationMimoFrom
from analyzeAlgorithm.analyzeAlgorithmSession import InitAnalyzeAlgorithmSession, ValuesChanged
from analyzeAlgorithm.analyzeAlgorithmForm import AnalyzeAlgorithmFrom

valuesChanged = True

def AnalyzeAlgorithmPng():
    InitAnalyzeAlgorithmSession()
    fig = cFigure.GetAnalyzeAlgorithmsFigure(valuesChanged)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def AnalyzeAlgorithmRouting():
    InitAnalyzeAlgorithmSession()
    show = False
    global valuesChanged
    form = AnalyzeAlgorithmFrom()
    if form.validate_on_submit():
        valuesChanged = ValuesChanged(form)
        session['randomSeed_AC'] = form.randomSeed.data
        session['numberReceiver_AC'] = form.numberReceiver.data
        session['numberSender_AC'] = form.numberSender.data
        session['receiverOrigin_AC'] = (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  
        session['radius_AC']= form.radius.data
        session['wavelength_AC'] = form.wavelength.data
        session['pathLoss_AC'] = form.pathLoss.data
        session['bValue_AC']= form.bValue.data
        session['formation_AC'] = form.formation.data
        session['isotropic_AC'] = form.isotropic.data
        session['receivedValue_AC'] = form.receivedValue.data
        session['signalType_AC'] = form.signalType.data
        session['originRadius_AC'] = form.originRadius.data
        session['iterations_AC'] = form.iterations.data
        session['algorithm_AC'] = form.algorithms.data
        if form.calcs_inLog10.data <= 9:
            show = True
    form.formation.default = session['formation_AC']
    form.isotropic.default = session['isotropic_AC']
    form.randomSeed.default = session['randomSeed_AC']
    form.numberReceiver.default =  session['numberReceiver_AC']
    form.numberSender.default =  session['numberSender_AC']
    form.receiverX.default = session['receiverOrigin_AC'][0]
    form.receiverY.default = session['receiverOrigin_AC'][1]
    form.receiverZ.default = session['receiverOrigin_AC'][2]
    form.radius.default = session['radius_AC']
    form.algorithms.default = session['algorithm_AC']
    form.wavelength.default = session['wavelength_AC']
    form.pathLoss.default = session['pathLoss_AC']
    form.bValue.default = session['bValue_AC']
    form.receivedValue.default = session['receivedValue_AC']
    form.signalType.default = session['signalType_AC']
    form.originRadius.default = session['originRadius_AC']
    form.iterations.default = session['iterations_AC']
    form.process()
    return render_template('analyzeAlgorithm.html', form=form, show=show)