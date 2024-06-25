from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('thyroid_model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_thyroid():
    t3_resin=int(request.form.get('T3-resin'))

    thyroxin=float(request.form.get('thyroxin'))
    
    triiodothyronine = float(request.form.get('triiodothyronine'))

    tsh = float(request.form.get('TSH'))

    diff_TSH = float(request.form.get('diff-TSH'))

    #predict the score
    result=model.predict(np.array([t3_resin,thyroxin,triiodothyronine,tsh,diff_TSH]).reshape(1,5))

    if result[0]==1:
        result1= "Not having Thyroid Disaese"
    else:
        result1= "Suffering from Thyroid Disease"
    
    return render_template('index.html',result=result1)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)

