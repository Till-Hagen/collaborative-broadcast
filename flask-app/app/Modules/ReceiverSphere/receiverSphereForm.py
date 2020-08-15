from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, Optional
import models

AlgorithmField = SelectField('Algorithm', choices=[('Parametrized Supernova', 'Parametrized Supernova')])
RandomSeedField = IntegerField('Random Seed', validators=[InputRequired()])
ColorsField = SelectField('Colors',choices=[('Greys', 'Greys'),('PiYG', 'PiYG'),('Greens', 'Greens'),('Set1', 'Set1')])
DimensionField = SelectField('Dimension',choices=[('2d','2d'),('3d', '3d')])

class ReceiverSphereFrom(FlaskForm):

    numberReceiver = IntegerField('Receiver', validators=[InputRequired(), NumberRange(1,1000000000)])
    numberSender = IntegerField('Sender', validators=[InputRequired(), NumberRange(1,1000000000)])
    randomSeed = RandomSeedField
    calcs_inLog10 = FloatField('calcs_inLog10', validators=[InputRequired(), NumberRange(2,9)])
    receiverX = FloatField('X', validators=[InputRequired()])
    receiverY = FloatField('Y', validators=[InputRequired()])
    receiverZ = FloatField('Z', validators=[InputRequired()])
    radius = FloatField('radius', validators=[InputRequired()])
    wavelength = FloatField('Wavelength', validators=[InputRequired()])
    pathLoss = FloatField('Path loss', validators=[InputRequired(), NumberRange(1,6)])
    bValue = FloatField('b', validators=[InputRequired(), NumberRange(-3,3)])
    elevation = FloatField('elevation', validators=[InputRequired(), NumberRange(0,360)])
    azimuth = FloatField('azimuth', validators=[InputRequired(), NumberRange(0,360)])
    algorithms = AlgorithmField
    upperBound = FloatField('UpperBound', validators=[InputRequired()])
    useMax = BooleanField('useMax')
    lowerBound = FloatField('LowerBound', validators=[InputRequired()])
    useMin = BooleanField('useMin')
    logScale = BooleanField('logScale')
    isotropic = BooleanField('isotropic')
    originRadius = FloatField('originRadius', validators=[InputRequired()])
    cutOrigin = BooleanField('cutOrigin')
    plotTyp = SelectField('PlotTyp',choices=[('real', 'real'),('imag', 'imag'),('|z|^2', '|z|^2'),('|z|', '|z|')])
    colors = ColorsField
    submit = SubmitField('Simulate')
    getData = SubmitField('Download Data')
    def __init__(self, *args, **kwargs):
        super(ReceiverSphereFrom, self).__init__(*args, **kwargs)
        self.algorithms.choices.extend([(algo.algorithmName, algo.algorithmName)  for algo in models.Algorithm.query.filter_by(legit=True)])