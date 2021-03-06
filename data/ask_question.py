from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
import datetime
import sqlalchemy
from wtforms.validators import DataRequired


class Ask_question(FlaskForm):
    title = StringField('T i t l e:', validators=[DataRequired()])
    question = StringField('Q u e s t i o n:', validators=[DataRequired()])
    theme = StringField('T h e m e:', validators=[DataRequired()])
    submit = SubmitField('G o !')
