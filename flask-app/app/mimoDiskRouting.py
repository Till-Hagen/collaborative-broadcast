from flask import Flask, render_template ,make_response, url_for, flash, redirect
import PlotFigureManager as cFigure
import io
from flask import Response, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from froms import SimulationMimoFrom
import SessionValues as v

valuesChanged = True

def MimoDiskPng():
    values = v.GetMimoValues()
    fig = cFigure.GetMimoReceiverFigure(values[0], values[1], values[2], values[3], values[4],
                                     values[5], values[6], values[7], values[8], values[9],
                                     values[10], values[11], values[12], values[13], values[14], 
                                     values[15], values[16], values[17], values[18], valuesChanged)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def MimoDiskRouting():
    show = False
    global valuesChanged
    form = SimulationMimoFrom()
    if form.validate_on_submit():
        valuesChanged = v.ValuesChanged(form)
        session['randomSeed'] = form.randomSeed.data
        session['numberReceiver'] = form.numberReceiver.data
        session['numberSender'] = form.numberSender.data
        receiverPos = (form.receiverX.data, form.receiverY.data, form.receiverZ.data)
        session['receiverPosMimo'] = receiverPos  
        session['radius']= form.radius.data
        session['orientation']= form.orientation.data
        session['wavelength'] = form.wavelength.data
        session['pathLoss'] = form.pathLoss.data
        session['bvalue']= form.b.data
        session['algorithm']= form.algorithms.data
        session['vmax'] = form.upperBound.data
        session['vmin']= form.lowerBound.data
        session['dimension']= form.dimension.data
        session['plotTyp']= form.plotTyp.data
        session['color']= form.colors.data
        session['useMin']= form.useMin.data
        session['useMax']= form.useMax.data
        session['formation']= form.formation.data
        session['logScale'] = form.logScale.data
        session['cutOrigin'] = form.cutOrigin.data
        session['originRadius'] = form.originRadius.data
        session['isotropic'] = form.isotropic.data
        if form.calcs_inLog10.data <= 9:
            show = True
    values = v.GetMimoValues()
    form.orientation.default = values[4]
    form.algorithms.default = values[8]
    form.plotTyp.default = values[12]
    form.dimension.default = values[13]
    form.colors.default = values[9]
    form.useMin.default = values[15]
    form.useMax.default = values[16]
    form.formation.default = values[17]
    form.logScale.default = values[18]
    form.cutOrigin.default = values[19]
    form.originRadius.default = values[20]
    form.isotropic.default = values[21]
    form.process()
    return render_template('mimo.html', form=form, 
                            numberReceiver= values[0],
                            numberSender= values[1],
                            receiverPos= values[2],
                            radius= values[3],
                            orientation= values[4],
                            wavelength = values[5],
                            pathLoss = values[6],
                            bvalue=values[7],
                            algorithm=values[8],
                            color=values[9],
                            lowerBound=values[10],
                            upperBound=values[11],
                            plotTyp=values[12],
                            dimension=values[13],
                            randomSeed=values[14],
                            useMin=values[15],
                            useMax=values[16],
                            cutOrigin=values[19],
                            originRadius=values[20], 
                            show=show)