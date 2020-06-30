from flask import Flask, render_template ,make_response, url_for, flash, redirect, send_file

import io
import random
import SessionValues as v
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


import PlotFigureManager as cFigure
import models
from froms import SimulationMimoFrom, SimulationMisoFrom, AddCustomFrom
from MimoSphereRouting import MimoSphereRouting, MimoSpherePng
from addCustomRouting import AddCustomRouting
from mimoDiskRouting import MimoDiskRouting, MimoDiskPng
from misoRouting import MisoRouting, MisoPng
from compareAlgorithm import CompareAlgorithmRouting, CompareAlgorithmPng
from analyzeAlgorithm.analyzeAlgorithm import AnalyzeAlgorithmRouting, AnalyzeAlgorithmPng


# models.Algorithm.query.delete()
# db.session.commit()

valuesChanged = True

@app.route('/documentation/<name>', methods=['Get', 'Post'])
def docu(name):
    return render_template('documentation/'+ name + 'Docu.html')

@app.route('/miso.png')
def plot_png():
    return MisoPng()

@app.route('/addCustom/<name>', methods=['Get', 'Post'])
def addCustom(name = None):
    return AddCustomRouting(name)


@app.route('/plot2.png')
def plot_png2():
    return MimoDiskPng()

@app.route('/plot3.png')
def plot_png3():
    return MimoSpherePng()

@app.route('/compareAlgorithmPlot.png')
def compareAlgorithmPlot():
    return CompareAlgorithmPng()

@app.route('/analyzeAlgorithmPlot.png')
def analyzeAlgorithmPlot():
    return AnalyzeAlgorithmPng()


@app.route('/', methods=['Get', 'Post'])
@app.route('/miso', methods=['Get', 'Post'])
def home():
    return MisoRouting()
    
@app.route('/compareAlgorithm', methods=['Get', 'Post'])
def compareAlgorihm():
    return CompareAlgorithmRouting()

@app.route('/analyzeAlgorithm', methods=['Get', 'Post'])
def analyzeAlgorihm():
    return AnalyzeAlgorithmRouting()

@app.route('/mimoSphere', methods=['Get', 'Post'])
def mimoSphere():
    return MimoSphereRouting()
    

@app.route('/mimo', methods=['Get', 'Post'])
def mimo():
    return MimoDiskRouting()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
