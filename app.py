#app.py
from flask import Flask,request, url_for, redirect, render_template
import tensorflow as tf
from tensorflow import keras
import numpy as np

app = Flask(__name__)
#model=pickle.load(open('model.h5','rb'))
model=tf.keras.models.load_model('model.h5')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    # receive the values send by user in three text boxes thru request object -> requesst.form.values()
    
    int_features = [eval(x) for x in request.form.values()]
    print(int_features)
   
    return render_template('index.html', pred='Student passing probability is :  {}'.format(int_features))

if __name__ == '__main__':
    app.run(debug=False)
