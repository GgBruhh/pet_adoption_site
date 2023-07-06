from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, URLField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = URLField('Photo URL', validators=[Optional(), URL()])
    age = FloatField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes', validators=[Optional()])