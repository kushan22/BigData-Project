from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField,DateField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from datetime import  date

class CrimeForm(FlaskForm):
    locationDescription = StringField('Location_description',id='loc_desc',widget=TextArea(),validators=[DataRequired()])
    arrest = BooleanField('Arrest')
    domestic = BooleanField('Domestic')
    beat = StringField('Beat',id='beat',validators=[DataRequired()])
    district_code = StringField('District Code',id='district_code',validators=[DataRequired()])
    ward_code = StringField('Ward Code',id='ward',validators=[DataRequired()])
    community_area = StringField('Community Area',id='community_area',validators=[DataRequired()])
    fbi_code = StringField('FBI Code',id='fbi_code',validators=[DataRequired()])
    dateofcrime = DateField('Date of Crime',default=date.today(), format='%Y-%m-%d')

    submit = SubmitField('Submit')

class Visualization(FlaskForm):
    questionDropdown =  SelectField(
        'Question',
        choices=[('cpy', 'Crimes Per Year'), ('cpm', 'Crimes Per Month'), ('t5y', 'Top 5 type of Crimes per year') ], validators = [DataRequired()])
    submit = SubmitField('Submit')