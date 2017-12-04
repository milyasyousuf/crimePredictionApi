from sklearn.externals import joblib
#import databaseModule as db
import pandas as pd
import numpy as np
import json,collections
import simplejson as json
import datetime as datetime
#loaded_model = joblib.load("joblib.pkl")

#'Mobile snatching':1,'Robbery':2,'Kidnapping':3,'Blast':4,'Vehicle Snatching':5,"Sexual harassment:6,'Murder':7
def init(data,model):
    data['crimeDate'] = pd.to_datetime(data['crimeDate'], format='%d : %m : %Y').dt.dayofweek
    x = data.as_matrix()
    return model.predict(x)

def getCrimesList(dir=None):
    df = pd.read_csv(dir+"/final.csv")
    today =(datetime.datetime.now().weekday())
    df['dayofWeek'] = pd.to_datetime(df['crimeDate'], format='%d : %m : %Y').dt.dayofweek
    return (df.loc[df['dayofWeek'] == today][['crimeLng','crimeLtd','typeOfCrime']].to_json(orient='records'))



#getCrimesList()