from flask import Flask, request, jsonify, url_for, redirect, render_template
import util
import pickle
import numpy as np
model=pickle.load(open('artifacts/model.pkl','rb'))
app = Flask(__name__)

@app.route('/predict',methods=['POST','GET'])
def predict():
    arr = []
    for x in request.form.values():
        arr.append(int(x))
    final=np.array(arr)
    print(final)
    prediction=model.predict_proba([final])[0]
    print(prediction)
    output=round(prediction[1],2)


    if output>0.5:
        return render_template('forest.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output))
    else:
        return render_template('forest.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output))



@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
