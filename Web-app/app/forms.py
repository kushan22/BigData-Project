from flask_wtf import FlaskForm


from wtforms import StringField, SubmitField,BooleanField,DateField, SelectField

from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
import datetime
from wtforms.fields.html5 import DateTimeField

class CrimeForm(FlaskForm):
    locationDescription = StringField('Location_description',id='loc_desc',widget=TextArea(),validators=[DataRequired()])
    arrest = BooleanField('Arrest')
    domestic = BooleanField('Domestic')
    beat = StringField('Beat',id='beat',validators=[DataRequired()])
    district_code = StringField('District Code',id='district_code',validators=[DataRequired()])
    ward_code = StringField('Ward Code',id='ward',validators=[DataRequired()])
    community_area = StringField('Community Area',id='community_area',validators=[DataRequired()])
    fbi_code = StringField('FBI Code',id='fbi_code',validators=[DataRequired()])
    dateofcrime = DateTimeField('Date and time of Crime',default=datetime.datetime.now(),format="%Y-%m-%d %H:%M:%S")

    submit = SubmitField('Submit')

class Visualization(FlaskForm):
    questionDropdown =  SelectField(
        'Question',
        choices=[('cpy', 'Crimes Per Year'), ('cpm', 'Crimes Per Month'), ('t5y', 'Top 5 type of Crimes per year') , ('gam', 'Gambling crimes with arrests'), ('war', 'Number of incidents per police ward 2019'), ('dis', 'Number of incidents per police district 2019'), ('ptm', 'Primary Type Plot for 2019 crimes'), ('ptc', 'Primary Type of crimes Over the years') ], validators = [DataRequired()])
    submit = SubmitField('Submit')