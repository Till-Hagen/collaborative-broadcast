from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, Optional
import models

AlgorithmField = SelectField('Algorithm', choices=[('Parametrized Supernova', 'Parametrized Supernova')])
RandomSeedField = IntegerField('Random Seed', validators=[InputRequired()])
ColorsField = SelectField('Colors',choices=[('Greys', 'Greys'),('PiYG', 'PiYG'),('Greens', 'Greens'),('Set1', 'Set1')])
DimensionField = SelectField('Dimension',choices=[('2d','2d'),('3d', '3d')])


class CustomAlgorithmFrom(FlaskForm):
    exceStringField = TextAreaField('TextAreaField', validators=[InputRequired()])
    algorithmName = StringField('Algorithm Name', validators=[InputRequired()])
    algorithms = SelectField('CustomAlgorithm', choices=[('new', 'new')])
    save = SubmitField('Save')
    delete = SubmitField('Delete')
    def __init__(self, *args, **kwargs):
        super(CustomAlgorithmFrom, self).__init__(*args, **kwargs)
        self.algorithms.choices.extend([(algo.algorithmName, algo.algorithmName)  for algo in models.Algorithm.query.all()])