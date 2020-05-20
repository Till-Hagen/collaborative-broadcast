from flask import Flask, render_template ,make_response, url_for, flash, redirect
import PlotFigureManager as cFigure
import io
import SessionValues as v
from flask import Response, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from froms import SimulationMimoFrom, SimulationMisoFrom
app = Flask(__name__)

app.config['SECRET_KEY'] = '12k9k91xe9k190j1y22s1o0so0vadfla484sjac81e4ab1t4'


# _ = cFigure.create_figure2((7,0,0), 0.1, 1, 'Parametrized Supernova', 'PiYG',True, 1, 3, 3)
# _ = cFigure.create_figure((7,0,0), 0.1, 1, 'Parametrized Supernova', 'PiYG',True, 1, 3)

valuesChanged = True

@app.route('/miso.png')
def plot_png():
    values = v.GetMisoValues()
    fig = cFigure.Create_miso_figure(values[0], values[1], values[2], values[3], values[4],values[5], values[6], values[7], values[8], values[9])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot2.png')
def plot_png2():
    values = v.GetMimoValues()
    fig = cFigure.GetMimoReceiverFigure(values[0], values[1], values[2], values[3], values[4],
                                     values[5], values[6], values[7], values[8], values[9],
                                     values[10], values[11], values[12], values[13], values[14], 
                                     values[15], values[16], values[17], values[18], valuesChanged)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/', methods=['Get', 'Post'])
@app.route('/miso', methods=['Get', 'Post'])
def home():
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
        show = True
    values = v.GetMisoValues()
    form.dimension.default = values[8]
    form.colors.default = values[6]
    form.misoPlotTyp.default = values[9]
    form.algorithms.default = values[5]
    form.process()
    return render_template('miso.html', form=form,
                            numberSender= values[0],
                            receiverPos= values[1],
                            wavelenght= values[2],
                            pathLoss = values[3],
                            bvalue=values[4],
                            algorithm = values[5],
                            color=values[6],
                            randomSeed= values[7],
                            show=show)

@app.route('/mimo', methods=['Get', 'Post'])
def mimo():
    show = True
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
                            show=show)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
