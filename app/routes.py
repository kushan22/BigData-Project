from flask import redirect,escape,url_for
from flask_bootstrap import Bootstrap
from flask import render_template

from datetime import date
from app import app
from app.forms import CrimeForm


bootstrap = Bootstrap(app)



@app.route('/',methods=['GET','POST'])
def index():
    form = CrimeForm()

    if form.validate_on_submit():
        return render_template('home.html',form=form,submitted=True)

    return render_template('home.html',form=form,submitted=False)

@app.route('/home',methods=['GET','POST'])
def home():
    return "Home is here"