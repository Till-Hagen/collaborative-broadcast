from flask import Flask, render_template ,make_response, url_for, flash, redirect
import io
from flask import Response, session, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from Modules.HistogramModule.histogramForm import HistogramFrom
from Modules.HistogramModule.histogramSession import InitSession, ValuesChanged
from Modules.HistogramModule.histogramEngineInterface import GetFigure, SaveData

valuesChanged = True

def HistogramPng():
    InitSession()
    fig = GetFigure(valuesChanged)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def HistogramRouting():
    form = HistogramFrom()
    if(form.getData.data):
        SaveData()
        path = "histogram.txt"
        try:
            return send_file(path, as_attachment=True)
        except Exception as inst:
            return ('', 204)
    else:
        return HistogramSimulate(form)

def HistogramSimulate(form):
    InitSession()
    show = False
    global valuesChanged
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
        session['minRange_AC'] = form.rangeMin.data
        session['maxRange_AC'] = form.rangeMax.data
        session['topRange_AC'] = form.rangeTop.data
        session['saveData_AC'] = form.saveData.data
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
    form.rangeMin.default = session['minRange_AC']
    form.rangeMax.default = session['maxRange_AC']
    form.rangeTop.default = session['topRange_AC']
    form.saveData.default = session['saveData_AC']
    form.process()
    return render_template('histogram.html', form=form, show=show)