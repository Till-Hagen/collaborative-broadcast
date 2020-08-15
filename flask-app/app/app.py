from flask import Flask, render_template ,make_response, url_for, flash, redirect, send_file

import io
import random
from flask import Response, session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas



from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# db.reflect()
# db.drop_all()
migrate = Migrate(app, db)

import models
from Modules.CompareModule.compareMain import CompareRouting, ComparePng
from Modules.ReceiverDisk.receiverDiskMain import ReceiverDiskPng, ReceiverDiskRouting
from Modules.SenderModule.senderMain import SenderRouting, StartSimulationAndVisualization
from Modules.ReceiverSphere.receiverSphereMain import ReceiverSpherePng, ReceiverSphereRouting
from Modules.CustomAlgorithm.customAlgorithmMain import CustomAlgorithmRouting
from Modules.HistogramModule.histogramMain import HistogramPng, HistogramRouting


# models.Algorithm.query.delete()
# db.session.commit()

valuesChanged = True

@app.route('/', methods=['Get', 'Post'])
@app.route('/documentation/<name>', methods=['Get', 'Post'])
def docu(name = 'model'):
    return render_template('documentation/'+ name + 'Docu.html')


@app.route('/sender', methods=['Get', 'Post'])
def home():
    return SenderRouting()

@app.route('/senderPlot.png')
def plot_png():
    return StartSimulationAndVisualization()

@app.route('/receiverDisk', methods=['Get', 'Post'])
def receiverDiskRouting():
    return ReceiverDiskRouting()

@app.route('/receiverDiskPlot.png')
def receiverDiskPng():
    return ReceiverDiskPng()

@app.route('/receiverSphere', methods=['Get', 'Post'])
def mimoSphere():
    return ReceiverSphereRouting()

@app.route('/receiverSpherePlot.png')
def plot_png3():
    return ReceiverSpherePng()


@app.route('/compare', methods=['Get', 'Post'])
def compareAlgorihm():
    return CompareRouting()

@app.route('/comparePlot.png')
def compareAlgorithmPlot():
    return ComparePng()

@app.route('/histogram', methods=['Get', 'Post'])
def analyzeAlgorihm():
    return HistogramRouting()

@app.route('/histogramPlot.png')
def analyzeAlgorithmPlot():
    return HistogramPng()

@app.route('/customAlgorithm/<name>', methods=['Get', 'Post'])
def addCustom(name = None):
    return CustomAlgorithmRouting(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
