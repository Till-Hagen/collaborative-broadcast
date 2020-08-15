from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, Optional


class CompareFrom(FlaskForm):

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
    minReceivedValue = FloatField('minReceivedValue', validators=[InputRequired()])
    signalType = SelectField('signalType',choices=[('real', 'real'),('imag', 'imag'),('|z|^2', '|z|^2'),('|z|', '|z|')])
    originRadius = FloatField('originRadius', validators=[InputRequired()])
    plotRange = FloatField('plotRange', validators=[InputRequired()])
    getData = SubmitField('Download Data')

    isotropic = BooleanField('isotropic')
    submit = SubmitField('Simulate')