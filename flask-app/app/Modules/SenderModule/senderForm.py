from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, Optional
import models

AlgorithmField = SelectField('Algorithm', choices=[('Parametrized Supernova', 'Parametrized Supernova')])
RandomSeedField = IntegerField('Random Seed', validators=[InputRequired()])
ColorsField = SelectField('Colors',choices=[('Greys', 'Greys'),('PiYG', 'PiYG'),('Greens', 'Greens'),('Set1', 'Set1'),('Set2', 'Set2')])
DimensionField = SelectField('Dimension',choices=[('2d','2d'),('3d', '3d')])

class SimulationMisoFrom(FlaskForm):
    defname = 1
    randomSeed = RandomSeedField
    receiverX = FloatField('X', validators=[InputRequired()])
    receiverY = FloatField('Y', validators=[InputRequired()])
    receiverZ = FloatField('Z', validators=[InputRequired()])
    numberSender = IntegerField('Sender', validators=[InputRequired(), NumberRange(1,1000000)])
    wavelength = FloatField('Wavelength', validators=[InputRequired()])
    pathLoss = FloatField('Path loss', validators=[InputRequired(), NumberRange(1,6)])
    b = FloatField('b', validators=[InputRequired(), NumberRange(-3,3)])
    algorithms = AlgorithmField
    colors = ColorsField
    isotropic = BooleanField('isotropic')
    dimension = DimensionField
    misoPlotTyp = SelectField('PlotTyp',choices=[('real', 'real'),('imag', 'imag'),('|z|^2', '|z|^2'),('|z|', '|z|'),('phase', 'phase')])

    submit = SubmitField('Simulate')
    getData = SubmitField('Download Data')
    def __init__(self, *args, **kwargs):
        super(SimulationMisoFrom, self).__init__(*args, **kwargs)
        self.algorithms.choices.extend([(algo.algorithmName, algo.algorithmName)  for algo in models.Algorithm.query.filter_by(legit=True)])