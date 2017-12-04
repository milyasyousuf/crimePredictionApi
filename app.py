from flask import Flask
from flask import request
import model
import os
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#loaded_model = joblib.load(APP_ROOT+"/joblib.pkl")

@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    if(request.is_json):
        content = request.json()
        print(content)
        data = model.init(content)
        return data
    return "None json"

@app.route('/getCrimeType', methods=['GET'])
def test():
    crimeDate = request.args.get("cDate")
    crimeLng = request.args.get("cLng")
    crimeLtd = request.args.get("cLtd")
    df =pd.DataFrame({"crimeDate":[crimeDate],"crimeLng":[float(crimeLng)],"crimeLtd":[float(crimeLtd)]})
    data = model.init(df,model)
    return  crimeDate


app.run(host='0.0.0.0', port=8000)