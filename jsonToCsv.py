
# coding: utf-8

# In[35]:


import json
import pandas as pd


# In[57]:


identificationOfVehicle = []
crimeDate = []
casualties = []
crimeLng = []
crimeLtd = []
crimeLocation = []
crimeTime = []
crimeVictim = [] 
crimeVehicle = []
noOfCriminal = []
msr = []
typeOfCrime = []
Vsr =[]
with open('dataset.json') as json_data:
    d = json.load(json_data)
    for i in d['Questionnaires']:
        
        identificationOfVehicle.append(d['Questionnaires'][i][' Any Identification of Vehicle'][0])
        crimeDate.append(d['Questionnaires'][i]['Crime Date'][0])
        casualties.append(d['Questionnaires'][i]['Casualties'][0])
        if('Criminal Vehicle' in d['Questionnaires'][i]):
            crimeLng.append(d['Questionnaires'][i]['Crime Location'][0])
            crimeLtd.append(d['Questionnaires'][i]['Crime Location'][1])
            crimeLocation.append(d['Questionnaires'][i]['Crime Location'][2])
        else:
            crimeLng.append("")
            crimeLtd.append("")
            crimeLocation.append("")
        crimeTime.append(d['Questionnaires'][i]['Crime Time'][0])
        crimeVictim.append(d['Questionnaires'][i]['Crime Victim '][0])
        noOfCriminal.append(d['Questionnaires'][i]['No of Criminal'][0])
        if('Mobile snaching Related' in d['Questionnaires'][i]):
            msr.append(d['Questionnaires'][i]['Mobile snaching Related'][0])
        else:
            msr.append("")
        
        if('Criminal Vehicle' in d['Questionnaires'][i]):
            crimeVehicle.append(d['Questionnaires'][i]['Criminal Vehicle'][0])
        else:
            crimeVehicle.append(" ")
        typeOfCrime.append(d['Questionnaires'][i]['Type Of Crime'][0])
        if('Vehicle snaching Related' in d['Questionnaires'][i]):
            Vsr.append(d['Questionnaires'][i]['Vehicle snaching Related'][0])
        else:
            Vsr.append("")
        
        
        
        


# In[58]:


df = pd.DataFrame()


# In[59]:


df['identificationOfVehicle'] = identificationOfVehicle
df['crimeDate']=crimeDate
df['casualties']=casualties
df['crimeLng']=crimeLng
df['crimeLtd'] = crimeLtd
df['crimeLocation'] = crimeLocation
df['crimeTime']=crimeTime
df['crimeVictim']=crimeVictim
df['crimeVehicle']=crimeVehicle
df['noOfCriminal']=noOfCriminal
df['msr']=msr
df['typeOfCrime']=typeOfCrime
df['Vsr']=Vsr



# In[61]:


df.to_csv("semi_final.csv",index=False)

