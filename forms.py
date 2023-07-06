from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, URLField
from wtforms.validators import InputRequired, Email, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = URLField('Photo URL', validators=[Optional(), URL()])
    age = FloatField('Age', validators=[Optional()])
    notes = StringField('Notes', validators=[Optional()])