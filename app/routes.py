from flask import redirect,escape,url_for
from flask_bootstrap import Bootstrap
from flask import render_template

from datetime import date
from app import app
from app.forms import CrimeForm

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