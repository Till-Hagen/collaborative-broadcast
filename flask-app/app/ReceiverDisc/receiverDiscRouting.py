from flask import Flask, render_template ,make_response, url_for, flash, redirect
import io
from flask import Response, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from ReceiverDisc.receiverDiscSession import InitSession, ValuesChanged
from ReceiverDisc.receiverDiscForm import ReceiverDiscFrom
from ReceiverDisc.receiverDiscManager import GetFigure
from froms import SimulationMimoFrom

valuesChanged = True

def ReceiverDiscPng():
    print("DiscPng")
    InitSession()
    fig = GetFigure(valuesChanged)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def ReceiverDiscRouting():
    InitSession()
    show = False
    global valuesChanged
    form = ReceiverDiscFrom()
    if form.validate_on_submit():
        print("hello")
        valuesChanged = ValuesChanged(form)
        session['randomSeed_RD'] = form.randomSeed.data
        session['numberReceiver_RD'] = form.numberReceiver.data
        session['numberSender_RD'] = form.numberSender.data
        receiverPos = (form.receiverX.data, form.receiverY.data, form.receiverZ.data)
        session['receiverPos_RD'] = receiverPos  
        session['radius_RD']= form.radius.data
        session['orientation_RD']= form.orientation.data
        session['wavelength_RD'] = form.wavelength.data
        session['pathLoss_RD'] = form.pathLoss.data
        session['bvalue_RD']= form.b.data
        session['algorithm_RD']= form.algorithms.data
        session['vmax_RD'] = form.upperBound.data
        session['vmin_RD']= form.lowerBound.data
        session['dimension_RD']= form.dimension.data
        session['plotTyp_RD']= form.plotTyp.data
        session['color_RD']= form.colors.data
        session['useMin_RD']= form.useMin.data
        session['useMax_RD']= form.useMax.data
        session['formation_RD']= form.formation.data
        session['logScale_RD'] = form.logScale.data
        session['cutOrigin_RD'] = form.cutOrigin.data
        session['originRadius_RD'] = form.originRadius.data
        session['isotropic_RD'] = form.isotropic.data
        print(form.calcs_inLog10.data)
        if form.calcs_inLog10.data <= 9:
            show = True
    form.randomSeed.default = session['randomSeed_RD']
    form.numberReceiver.default = session['numberReceiver_RD']
    form.numberSender.default = session['numberSender_RD']
    form.receiverX.default, form.receiverY.default, form.receiverZ.default = session['receiverPosMimo_RD']
    form.radius.default = session['radius_RD']
    form.orientation.default = session['orientation_RD']
    form.wavelength.default = session['wavelength_RD']
    form.pathLoss.default = session['pathLoss_RD']
    form.b.default = session['bvalue_RD']
    form.algorithms.default = session['algorithm_RD']
    form.upperBound.default = session['vmax_RD']
    form.lowerBound.default = session['vmin_RD']
    form.dimension.default = session['dimension_RD']
    form.plotTyp.default = session['plotTyp_RD']
    form.colors.default = session['color_RD']
    form.useMin.default = session['useMin_RD']
    form.useMax.default = session['useMax_RD']
    form.formation.default = session['formation_RD']
    form.logScale.default = session['logScale_RD'] 
    form.cutOrigin.default = session['cutOrigin_RD'] 
    form.originRadius.default = session['originRadius_RD']
    form.isotropic.default = session['isotropic_RD']
    form.process()
    print(show)
    return render_template('receiverDisc.html', form=form, show=show)