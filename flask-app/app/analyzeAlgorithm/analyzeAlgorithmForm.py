from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, Optional
import models


class AnalyzeAlgorithmFrom(FlaskForm):

    numberReceiver = IntegerField('Receiver', validators=[InputRequired(), NumberRange(1,1000000000)])
    numberSender = IntegerField('Sender', validators=[InputRequired(), NumberRange(1,1000000000)])
    randomSeed = IntegerField('Random Seed', validators=[InputRequired()])
    formation = SelectField('formation',choices=[('sphere', 'sphere'),('plain horizontal', 'plain horizontal'),('plain vertical', 'plain vertical')])
    calcs_inLog10 = FloatField('calcs_inLog10', validators=[InputRequired(), NumberRange(0,9)])
    receiverX = FloatField('X', validators=[InputRequired()])
    receiverY = FloatField('Y', validators=[InputRequired()])
    receiverZ = FloatField('Z', validators=[InputRequired()])
    radius = FloatField('radius', validators=[InputRequired()])
    wavelength = FloatField('Wavelength', validators=[InputRequired()])
    pathLoss = FloatField('Path loss', validators=[InputRequired(), NumberRange(1,6)])
    bValue = FloatField('b', validators=[InputRequired(), NumberRange(-3,3)])
    receivedValue = FloatField('receivedValue', validators=[InputRequired()])
    signalType = SelectField('signalType',choices=[('real', 'real'),('imag', 'imag'),('|z|^2', '|z|^2'),('|z|', '|z|')])
    originRadius = FloatField('originRadius', validators=[InputRequired()])
    iterations = IntegerField('iterations', validators=[InputRequired(), NumberRange(1,10000)])
    algorithms = SelectField('Algorithm', choices=[('Parametrized Supernova', 'Parametrized Supernova')])

    isotropic = BooleanField('isotropic')
    submit = SubmitField('Simulate')

    def __init__(self, *args, **kwargs):
        super(AnalyzeAlgorithmFrom, self).__init__(*args, **kwargs)
        self.algorithms.choices.extend([(algo.algorithmName, algo.algorithmName)  for algo in models.Algorithm.query.filter_by(legit=True)])