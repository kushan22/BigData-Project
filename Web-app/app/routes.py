from flask import redirect,escape,url_for
from flask_bootstrap import Bootstrap
from flask import render_template, request

from datetime import date
from app import app
from app.forms import Visualization

from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.feature import IndexToString



from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("HW2")\
        .getOrCreate()

sc = spark.sparkContext



bootstrap = Bootstrap(app)

labels = ['THEFT',
 'BATTERY',
 'CRIMINAL DAMAGE',
 'NARCOTICS',
 'OTHER OFFENSE',
 'ASSAULT',
 'BURGLARY',
 'MOTOR VEHICLE THEFT',
 'ROBBERY',
 'DECEPTIVE PRACTICE',
 'CRIMINAL TRESPASS',
 'PROSTITUTION',
 'WEAPONS VIOLATION',
 'PUBLIC PEACE VIOLATION',
 'OFFENSE INVOLVING CHILDREN',
 'CRIM SEXUAL ASSAULT',
 'SEX OFFENSE',
 'GAMBLING',
 'LIQUOR LAW VIOLATION',
 'INTERFERENCE WITH PUBLIC OFFICER',
 'ARSON',
 'HOMICIDE',
 'KIDNAPPING',
 'INTIMIDATION',
 'STALKING',
 'OBSCENITY',
 'PUBLIC INDECENCY',
 'OTHER NARCOTIC VIOLATION',
 'NON-CRIMINAL',
 'CONCEALED CARRY LICENSE VIOLATION',
 'NON - CRIMINAL',
 'HUMAN TRAFFICKING',
 'RITUALISM',
 'NON-CRIMINAL (SUBJECT SPECIFIED)']


labelConverter = IndexToString(inputCol="prediction", outputCol="predictionLabel", labels=labels)

@app.route('/',methods=['GET','POST'])
def index():
    return redirect('/home')


@app.route('/home',methods=['GET','POST'])
def home():

    predictionLabels = []
    labels = []
    newModel = RandomForestClassificationModel.read().load("./app/static/rf-model")
    test_df = spark.read.parquet("./app/static/test/*.parquet")


    predictions = newModel.transform(test_df)
    convertedDf = labelConverter.transform(predictions)

    print(convertedDf.printSchema())

    predictionLabel = convertedDf.select("predictionLabel").limit(5).collect()

    label = convertedDf.select("primary_type").limit(5).collect()

    for i in range(len(predictionLabel)):
        predictionLabels.append(predictionLabel[i]["predictionLabel"])

    for i in range(len(label)):
        labels.append(label[i]["primary_type"])

    length = len(labels)




    return render_template('home.html',labels=labels,predictionLabels=predictionLabels)

@app.route('/nav',methods=['GET','POST'])
def nav():
    return render_template('homepage.html')


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
            elif ques == 'ptc':
                return render_template('vis.html',form=form, imagetype = 'ptc', image="PrimaryCt.png")
            else:
                return render_template('vis.html',form=form, submitted=False)

@app.route('/tableau',methods=['GET','POST'])
def tab():
    return render_template('story.html')
