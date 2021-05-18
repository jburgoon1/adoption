from flask_wtf import FlaskForm
from wtforms import (IntegerField, SelectField, BooleanField, StringField)

class addPetForm(FlaskForm):
    name = StringField('Pet Name')
    species = SelectField('Species of Pet', choices = ['Cat', 'Dog', 'Porcupine'])
    photo_url = StringField('Pet Image')
    age =IntegerField('Pet age')
    notes = StringField('Anything we need to know about your pet?')
    available = BooleanField('Is this pet available?', default = True)

class editPetForm(FlaskForm):
    photo_url = StringField('Pet Image')
    age =IntegerField('Pet age')
    notes = StringField('Anything we need to know about your pet?')
    available = BooleanField('Is this pet available?', default = True)