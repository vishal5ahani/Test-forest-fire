from flask import  Flask,url_for,request,render_template,jsonify
import numpy as np 
import pandas as pd
import pickle

application=Flask(__name__)
app=application

ridge_model = open('ridge.pkl', 'rb')

scaler_model = open('scaler.pkl', 'rb')


@app.route("/")
def index():
    return render_template('index.html')



@app.route('/predictdata', methods=['GET', 'POST'])
def predictdata():
    result = None
    if request.method == "POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))     
        
    new_scaler_model=sacler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
    result=ridge_model.predict(new_scaler_model)

    return render_template('hoem,html',result=result[0])

    else:
        return render_template('home.html'))



if __name__ =="__main__":
    app.run(host='0.0.0.0.')from flask import  Flask,url_for,request,render_template,jsonify
import numpy as np 
import pandas as pd
import pickle

application=Flask(__name__)
app=application

ridge_model = open('ridge.pkl', 'rb')

scaler_model =from flask import  Flask,url_for,request,render_template,jsonify
import numpy as np 
import pandas as pd
import pickle

application=Flask(__name__)
app=application

ridge_model = open('ridge.pkl', 'rb')

scaler_model = open('scaler.pkl', 'rb')


@app.route("/")
def index():
    return render_template('index.html')



@app.route('/predictdata', methods=['GET', 'POST'])
def predictdata():
    result = None
    if request.method == "POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))     
        
    new_scaler_model=sacler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
    result=ridge_model.predict(new_scaler_model)

    return render_template('hoem,html',result=result[0])

    else:
        return render_template('home.html')



if __name__ =="__main__":
    app.run(host='0.0.0.0.') open('scaler.pkl', 'rb')


@app.route("/")
def index():
    return render_template('index.html')



@app.route('/predictdata', methods=['GET', 'POST'])
def predictdata():
    result = None
    if request.method == "POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))     
        
        new_scaler_model=scaler_model.trasnform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_scaler_model)
        
        return render_template('home.html',results=result[0]) 
        
        
    else:
        return render_template('home.html')



if __name__ =="__main__":
    app.run(host='localhost')