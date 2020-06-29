from flask import Flask, render_template ,make_response, url_for, flash, redirect
import PlotFigureManager as cFigure
import io
from flask import Response, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from froms import SimulationMisoFrom
import SessionValues as v

valuesChanged = True

def MisoPng():
    values = v.GetMisoValues()
    fig = cFigure.Create_miso_figure(values[0], values[1], values[2], values[3], values[4],values[5], values[6], values[7], values[8], values[9])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def MisoRouting():
    form = SimulationMisoFrom()
    show = False
    if form.validate_on_submit():
        receiverPos = (form.receiverX.data, form.receiverY.data, form.receiverZ.data)
        session['randomSeed'] = form.randomSeed.data
        session['numberSenderMiso'] = form.numberSender.data
        session['receiverPos'] = receiverPos  
        session['wavelength'] = form.wavelength.data
        session['pathLoss'] = form.pathLoss.data
        session['algorithm']= form.algorithms.data
        session['color']= form.colors.data
        session['bvalue']= form.b.data
        session['algorithm']= form.algorithms.data
        session['color']= form.colors.data
        session['dimension']= form.dimension.data
        session['misoPlotTyp']= form.misoPlotTyp.data
        session['isotropic_S']= form.isotropic.data
        show = True
    values = v.GetMisoValues()

    form.dimension.default = values[8]
    form.colors.default = values[6]
    form.misoPlotTyp.default = values[9]
    form.algorithms.default = values[5]
    form.isotropic.default = session['isotropic_S'] 
    form.process()
    return render_template('miso.html', form=form,
                            numberSender= values[0],
                            receiverPos= values[1],
                            wavelength= values[2],
                            pathLoss = values[3],
                            bvalue=values[4],
                            algorithm = values[5],
                            color=values[6],
                            randomSeed= values[7],
                            show=show)