from flask import Flask, render_template ,make_response, url_for, flash, redirect
import io
from flask import Response, session, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from Modules.CompareModule.compareForm import CompareFrom
from Modules.CompareModule.compareEngineInterface import GetFigure, SaveData
from Modules.CompareModule.compareSession import InitSession, ValuesChanged

valuesChanged = True

def ComparePng():
    InitSession()
    fig = GetFigure(valuesChanged)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def CompareRouting():
    form = CompareFrom()
    if(form.getData.data):
        SaveData()
        path = "compare.txt"
        try:
            return send_file(path, as_attachment=True)
        except Exception as inst:
            return ('', 204)
    else:
        return CompareSimulate(form)

def CompareSimulate(form):
    InitSession()
    show = False
    global valuesChanged
    if form.validate_on_submit():
        valuesChanged = ValuesChanged(form)
        session['randomSeed_C'] = form.randomSeed.data
        session['numberReceiver_C'] = form.numberReceiver.data
        session['numberSender_C'] = form.numberSender.data
        session['receiverOrigin_C'] = (form.receiverX.data, form.receiverY.data, form.receiverZ.data)  
        session['radius_C']= form.radius.data
        session['wavelength_C'] = form.wavelength.data
        session['pathLoss_C'] = form.pathLoss.data
        session['bValue_C']= form.bValue.data
        session['formation_C'] = form.formation.data
        session['isotropic_C'] = form.isotropic.data
        session['minReceivedValue_C'] = form.minReceivedValue.data
        session['signalType_C'] = form.signalType.data
        session['originRadius_C'] = form.originRadius.data
        session['plotRange_C'] = form.plotRange.data
        if form.calcs_inLog10.data <= 9:
            show = True
    form.formation.default = session['formation_C']
    form.isotropic.default = session['isotropic_C']
    form.randomSeed.default = session['randomSeed_C']
    form.numberReceiver.default =  session['numberReceiver_C']
    form.numberSender.default =  session['numberSender_C']
    form.receiverX.default = session['receiverOrigin_C'][0]
    form.receiverY.default = session['receiverOrigin_C'][1]
    form.receiverZ.default = session['receiverOrigin_C'][2]
    form.radius.default = session['radius_C']
    form.wavelength.default = session['wavelength_C']
    form.pathLoss.default = session['pathLoss_C']
    form.bValue.default = session['bValue_C']
    form.minReceivedValue.default = session['minReceivedValue_C']
    form.signalType.default = session['signalType_C']
    form.originRadius.default = session['originRadius_C']
    form.plotRange.default = session['plotRange_C']
    form.process()
    return render_template('compare.html', form=form, show=show)
