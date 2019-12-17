from flask import redirect,escape,url_for
from flask_bootstrap import Bootstrap
from flask import render_template, request

from datetime import date
from app import app
from app.forms import CrimeForm, Visualization

from pyspark.sql import SparkSession




bootstrap = Bootstrap(app)



@app.route('/',methods=['GET','POST'])
def index():
    form = CrimeForm()

    if form.validate_on_submit():

        locationDesc = escape(form.locationDescription.data)
        arrest = escape(form.arrest.data)
        domestic = escape(form.domestic.data)
        beat = escape(form.beat.data)
        districtCode = escape(form.district_code.data)
        wardCode = escape(form.ward_code.data)
        community_area = escape(form.community_area.data)
        fbi_code = escape(form.fbi_code.data)
        dateofcrime = escape(form.dateofcrime.data)

        # print(dateofcrime)
        # print(arrest)
        # print(domestic)

        spark = SparkSession.builder.appName('pbda').getOrCreate()
        sc = spark.sparkContext

        print(sc)

        return render_template('home.html',form=form,submitted=True)

    return render_template('home.html',form=form,submitted=False)

@app.route('/home',methods=['GET','POST'])
def home():
    return "Home is here"

@app.route('/vis',methods=['GET','POST'])
def vis():
    form = Visualization()
    if request.method =='GET':
        return render_template('vis.html',form=form, submitted=False)
    if request.method =='POST':
        if form.submit:
            ques = form.questionDropdown.data
            print(ques)
            if ques == 'cpy':
                return render_template('vis.html',form=form, imagetype = 'cpy', image="crimeperyear.png")
            elif ques == 'cpm':
                return render_template('vis.html',form=form, imagetype = 'cpm', image="crimespermonth.png")
            elif ques == 't5y':
                return render_template('vis.html',form=form, imagetype = 't5y', image="top5.png")
            elif ques == 'gam':
                return render_template('vis.html',form=form, imagetype = 'gam', image="bokeh.html")
            elif ques == 'war':
                return render_template('vis.html',form=form, imagetype = 'war', image="wardWise.html")
            elif ques == 'dis':
                return render_template('vis.html',form=form, imagetype = 'dis', image="districtWise.html")
            elif ques == 'ptm':
                return render_template('vis.html',form=form, imagetype = 'ptm', image="PrimaryType.png")
            else:
                return render_template('vis.html',form=form, submitted=False)
