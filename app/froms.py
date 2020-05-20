from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange

AlgorithmField = SelectField('Algorithm', choices=[('Parametrized Supernova', 'Parametrized Supernova'),('Alternating Supernova', 'Alternating Supernova')])
RandomSeedField = IntegerField('Random Seed', validators=[InputRequired()])
ColorsField = SelectField('Colors',choices=[('Greys', 'Greys'),('PiYG', 'PiYG'),('Greens', 'Greens'),('Set1', 'Set1')])
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
    dimension = DimensionField
    misoPlotTyp = SelectField('PlotTyp',choices=[('real', 'real'),('imag', 'imag'),('|z|^2', '|z|^2'),
                                            ('|a| + |b|', '|a| + |b|'),('|z|', '|z|'),('phase', 'phase')])

    submit = SubmitField('Simulate')

class SimulationMimoFrom(FlaskForm):

    numberReceiver = IntegerField('Receiver', validators=[InputRequired(), NumberRange(1,1000000000)])
    numberSender = IntegerField('Sender', validators=[InputRequired(), NumberRange(1,1000000000)])
    randomSeed = RandomSeedField
    formation = SelectField('formation',choices=[('random', 'random'),('grid', 'grid')])
    calcs_inLog10 = FloatField('calcs_inLog10', validators=[InputRequired(), NumberRange(2,9)])
    receiverX = FloatField('X', validators=[InputRequired()])
    receiverY = FloatField('Y', validators=[InputRequired()])
    receiverZ = FloatField('Z', validators=[InputRequired()])
    radius = FloatField('radius', validators=[InputRequired()])
    orientation = SelectField('Orientation', choices=[('Horizontal', 'Horizontal'),('Vertical', 'Vertical')])
    wavelength = FloatField('Wavelength', validators=[InputRequired()])
    pathLoss = FloatField('Path loss', validators=[InputRequired(), NumberRange(1,6)])
    b = FloatField('b', validators=[InputRequired(), NumberRange(-3,3)])
    algorithms = AlgorithmField
    upperBound = FloatField('UpperBound', validators=[InputRequired()])
    useMax = BooleanField('useMax')
    lowerBound = FloatField('LowerBound', validators=[InputRequired()])
    useMin = BooleanField('useMin')
    logScale = BooleanField('logScale')
    dimension = DimensionField
    plotTyp = SelectField('PlotTyp',choices=[('all', 'all'),('real', 'real'),('imag', 'imag'),('|z|^2', '|z|^2'),
                                            ('|a| + |b|', '|a| + |b|'),('|z|', '|z|'),('phase', 'phase')])
    colors = ColorsField
    submit = SubmitField('Simulate')