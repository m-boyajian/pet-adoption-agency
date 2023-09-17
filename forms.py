from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, Length, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name",  validators=[ 
                       InputRequired(message="Pet Name cannot be blank")])
    species = SelectField("Choose Species", choices=[("bird", "Bird"), ("bunny", "Bunny"), ("cat", "Cat"), ("dog", "Dog"), ("ferret", "Ferret"), ("gerbil", "Gerbil"), ("hampster", "Hampster"), ("porcupine", "Porcupine"), ("turtle", "Turtle")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes about pet", validators=[Optional(), Length(min=10, max=100)])
    """Optional allows empty input and stops the validation chain from continuing."""

class EditPetForm(FlaskForm):
    notes = TextAreaField("Edit notes about pet")
    photo_url = StringField("Change Photo URL", validators=[Optional(), URL()])
    available = BooleanField("Is pet available?") 