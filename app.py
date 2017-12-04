from flask import Flask
from flask import request,jsonify
import model
import os
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
loaded_model = joblib.load(APP_ROOT+"/joblib.pkl")

#localhost:8000/getCrimeType?cDate=28%20:%207%20:%202017&cLtd=67.0689859&cLng=24.810707100000002

@app.route('/getCrimeType', methods=['GET'])
def getCrimeType():
    crimeDate = request.args.get("cDate")
    crimeLng = request.args.get("cLng")
    crimeLtd = request.args.get("cLtd")
    df =pd.DataFrame({"crimeDate":[crimeDate],"crimeLng":[float(crimeLng)],"crimeLtd":[float(crimeLtd)]})
    crimeType = model.init(df,loaded_model)
    return  jsonify(crimeType=str(crimeType[0]))

#localhost:8000/getAllCrimes

@app.route('/getAllCrimes', methods=['GET'])
def getAllCrimes():
    return model.getCrimesList(APP_ROOT)


app.run(host='0.0.0.0', port=8000)