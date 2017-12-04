from sklearn.externals import joblib
#import databaseModule as db
import pandas as pd
import numpy as np
import json,collections
import simplejson as json
loaded_model = joblib.load("joblib.pkl")

#'Mobile snatching':1,'Robbery':2,'Kidnapping':3,'Blast':4,'Vehicle Snatching':5,"Sexual harassment:6,'Murder':7
def init(data):
    data['crimeDate'] = pd.to_datetime(data['crimeDate'], format='%d : %m : %Y').dt.dayofweek
    x = data.as_matrix()
    print(loaded_model.predict(x))

    
    #print(a.dtype())
    #df = pd.read_json(test)
    #print (elevations['crimeDate'])
    #return df

crimeDate = "28 : 7 : 2017"
crimeLng = "67.0689859"
crimeLtd = "24.810707100000002"
df =pd.DataFrame({"crimeDate":[crimeDate],"crimeLng":[float(crimeLng)],"crimeLtd":[float(crimeLtd)]})
    

init(df)
