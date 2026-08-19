import pickle

from flask import Flask
from flask import request
from flask import jsonify #turn python dict in our result back to jyson


model_file = "model_C=1.0.bin"

with open(model_file, "rb") as f_in: #change wb to rb for reading
    dv, model = pickle.load(f_in)
    
app = Flask("churn")

@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()  #will get the json file below and return it as a python dictionary 
    
    X = dv.transform([customer]) #in a real project, this would be put inside a separate function
    y_pred = model.predict_proba(X)[0, 1] #This returns a NumPy float type
    churn = y_pred >= 0.5 #we make the decision ourselves and this returns a NumPy boolean type
    
    result = {
        
        # Cast both values explicitly to standard Python float() and bool() types inside your dictionary
        # Why : because Flask is returning a NumPy boolean or float type, which standard Python jsonify cannot serialize into JSON.
        'churn_probability': float(y_pred), #the result is numpy and 
        'churn':bool(churn)
        
    }
    
    return jsonify(result)

if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    app.run(host= "127.0.0.1", debug=True, port=9696)
    
#the information with be sent and received in JSON format that uses double quotes instead of single qoutes
  