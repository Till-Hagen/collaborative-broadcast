from flask import Flask, render_template ,make_response, url_for, flash, redirect
import PlotFigureManager as cFigure
import io
from flask import Response, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from froms import SimulationMimoSphereFrom
from MimoSphereValues import GetMimoSphereValues, ValuesChanged

valuesChanged = True
debug = False

def MimoSpherePng():
    fig = cFigure.GetMimo3dReceiverFigure(valuesChanged, debug)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def MimoSphereRouting():
    global valuesChanged
    show = False
    form = SimulationMimoSphereFrom()
    if form.validate_on_submit():
        valuesChanged = ValuesChanged(form, debug)
        session['randomSeedMimo3d'] = form.randomSeed.data
        session['receiverNumberMimo3d'] = form.numberReceiver.data
        session['senderNumberMimo3d'] = form.numberSender.data
        receiverPos = (form.receiverX.data, form.receiverY.data, form.receiverZ.data)
        session['receiverOriginMimo3d'] = receiverPos  
        session['radiusMimo3d']= form.radius.data
        session['wavelengthMimo3d'] = form.wavelength.data
        session['pathLossMimo3d'] = form.pathLoss.data
        session['bValueMimo3d']= form.bValue.data
        session['algorithmMimo3d']= form.algorithms.data
        session['vmax'] = form.upperBound.data
        session['vmin']= form.lowerBound.data
        session['plotTypMimo3d'] = form.plotTyp.data
        session['color']= form.colors.data
        session['useMin']= form.useMin.data
        session['useMax']= form.useMax.data
        session['logScale'] = form.logScale.data
        session['originRadius_RS'] = form.originRadius.data
        session['cutOrigin_RS'] = form.cutOrigin.data
        session['isotropic_RS'] = form.isotropic.data
        session['elevation_RS'] = form.elevation.data
        session['azimuth_RS'] =  form.azimuth.data
        if form.calcs_inLog10.data <= 9:
            show = True
    values = GetMimoSphereValues()
    form.algorithms.default = values[7]
    form.plotTyp.default = session['plotTypMimo3d']
    form.colors.default = values[9]
    form.useMin.default = values[13]
    form.useMax.default = values[14]
    form.logScale.default = values[15]
    form.isotropic.default = session['isotropic_RS']
    form.originRadius.default = session['originRadius_RS']
    form.cutOrigin.default = session['cutOrigin_RS']
    form.azimuth.default = session['azimuth_RS']
    form.elevation.default = session['elevation_RS']
    form.process()
    return render_template('mimo3d.html', form=form, 
                            numberSender= values[0],
                            numberReceiver= values[1],
                            receiverPos= values[2],
                            radius= values[3],
                            wavelength = values[4],
                            pathLoss = values[5],
                            bvalue=values[6],
                            algorithm=values[7],
                            randomSeed=values[8],
                            color=values[9],
                            lowerBound=values[10],
                            upperBound=values[11],
                            plotTyp=values[12],
                            useMin=values[13],
                            useMax=values[14],
                            logScale=values[15],
                            show = show)