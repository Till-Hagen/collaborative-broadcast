from flask import Flask, render_template ,make_response, url_for, flash, redirect
import io
from flask import Response, session
from froms import AddCustomFrom
from app import db
import models
from Simulate.Algorithms import TestAlgorithm


def AddCustomRouting(_name):
    form = AddCustomFrom()
    name = _name
    if form.validate_on_submit():
        #Get Model if stored
        algoModel = models.Algorithm.query.filter_by(algorithmName=form.algorithms.data).first()
        if(form.delete.data):
            if(algoModel is not None):
                db.session.delete(algoModel)
                form.algorithms.choices.remove((algoModel.algorithmName, algoModel.algorithmName))
        else:
            #Test
            legit, msg = TestAlgorithm(form.algorithmName.data, form.exceStringField.data)
            if(legit):
                flash(msg, "notification")
            else:
                flash(msg, "error")

            if(algoModel is None):
                algoModel = models.Algorithm(algorithmName = form.algorithmName.data, exceString=form.exceStringField.data, legit=legit)
                db.session.add(algoModel)
                form.algorithms.choices.append((form.algorithmName.data, form.algorithmName.data))
            elif(algoModel is not None):
                algoModel.algorithmName = form.algorithmName.data
                algoModel.exceString = form.exceStringField.data
                algoModel.legit = legit
                form.algorithms.choices.remove((form.algorithms.data, form.algorithms.data))
                form.algorithms.choices.append((form.algorithmName.data, form.algorithmName.data))
                
            name = algoModel.algorithmName
        db.session.commit()

    #Get Model by name, is not from submit then new show not have any model. and update form.
    algorithmModel = models.Algorithm.query.filter_by(algorithmName=name).first()
    if(algorithmModel is not None):   
        UpdateFormFields(form, algorithmModel)
   
    form.process()
    return render_template('addCustom.html', form=form, functionName=name.replace(" ", "") )

def UpdateFormFields(_form, _algorithmModel):
        _form.exceStringField.default = _algorithmModel.exceString
        _form.algorithmName.default = _algorithmModel.algorithmName
        _form.exceStringField.data = _algorithmModel.exceString
        _form.algorithmName.data = _algorithmModel.algorithmName
        _form.algorithms.default = _algorithmModel.algorithmName
