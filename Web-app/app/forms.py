from flask_wtf import FlaskForm


from wtforms import StringField, SubmitField,BooleanField,DateField, SelectField

from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
import datetime
from wtforms.fields.html5 import DateTimeField



class Visualization(FlaskForm):
    questionDropdown =  SelectField(
        'Question',
        choices=[('cpy', 'Crimes Per Year'), ('cpm', 'Crimes Per Month'), ('t5y', 'Top 5 type of Crimes per year') , ('gam', 'Gambling crimes with arrests'), ('war', 'Number of incidents per police ward 2019'), ('dis', 'Number of incidents per police district 2019'), ('ptm', 'Primary Type Plot for 2019 crimes'), ('ptc', 'Primary Type of crimes Over the years') ], validators = [DataRequired()])
    submit = SubmitField('Submit')