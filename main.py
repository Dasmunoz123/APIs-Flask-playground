import traceback
from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
import pandas as pd
import joblib
import sys

model_file_name = 'MLmodels/lr_model.pkl'
model_columns_file_name = 'MLmodels/lr_model_columns.pkl'
app = Flask(import_name=__name__)

@app.route(rule='/landing', methods=['POST','GET'])
def test():
    return "Welcome to machine learning model APIs!"


@app.route(rule='/predict', methods=['POST'])       # type: ignore
def predict():
    if ml_model:
        try:
            request_json = request.json
            request_df = pd.DataFrame(data=request_json)
            query = pd.get_dummies(data=request_df)
            query = query.reindex(columns=ml_columns, fill_value=0)
            prediction = list(ml_model.predict(query))
            
            return jsonify({'Predictions': list(prediction)})
        
        except:
            return jsonify({'trace': traceback.format_exc()})
            
    else:
        print('There is no ML model available for the APP')
        return ('No ML model here to use')
'''
Running the defined Flask app
'''
if __name__ == '__main__':
    try: port_number = int(sys.argv[1])
    except: port_number = 5001
    ml_model = joblib.load(model_file_name)
    ml_columns = joblib.load(model_columns_file_name)
    print(f"Machine Learning model succesfully loaded")
    app.run(port=port_number, debug=True)