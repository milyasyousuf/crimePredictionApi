import json
import pandas as pd

def convertJsonToCSV(filename):
    anyIdentVehical = []
    crimeDate = []
    casualties = []
    crimeLng = []
    crimeLtd = []
    crimeLocation = []
    crimeVictim = []
    crimeVehicle = []
    noOfCriminal = []
    typeOfCrime = []
    Vsr = []
    with open(filename, 'r') as f:
        array = json.load(f)
        for i in array['Questionnaires']:
            anyIdentVehical.append(array['Questionnaires'][i][' Any Identification of Vehicle'][0])
            crimeDate.append(array['Questionnaires'][i]['Crime Date'][0])
            casualties.append(array['Questionnaires'][i]['Casualties'][0])
            if('Crime Location' in array['Questionnaires'][i]):
                crimeLng.append(array['Questionnaires'][i]['Crime Location'][0])
                crimeLtd.append(array['Questionnaires'][i]['Crime Location'][1])
                crimeLocation.append(array['Questionnaires'][i]['Crime Location'][2])
            else:
                crimeLng.append("  ")
                crimeLtd.append("  ")
                crimeLocation.append(" ")
            crimeVictim.append(array['Questionnaires'][i]['Crime Victim '][0])
            if('Criminal Vehicle' in array['Questionnaires'][i]):
                crimeVehicle.append(array['Questionnaires'][i]['Criminal Vehicle'][0])
            else:
                crimeVehicle.append(" ")
            noOfCriminal.append(array['Questionnaires'][i]['No of Criminal'][0])
            typeOfCrime.append(array['Questionnaires'][i]['Type Of Crime'][0])
            if ('Vehicle snaching Related' in array['Questionnaires'][i]):
                Vsr.append(array['Questionnaires'][i]['Vehicle snaching Related'][0])
            else:
                Vsr.append(" ")
            #break

    df = pd.DataFrame()
    df['identificationOfVehicle'] = anyIdentVehical
    df['crimeDate']= crimeDate
    df['casualties'] = casualties
    df['crimeLng'] = crimeLng
    df['crimeLtd'] = crimeLtd
    df['crimeLocation'] = crimeLocation
    df['crimeVictim'] = crimeVictim
    df['crimeVehicle'] = crimeVehicle

    df['noOfCriminal'] = noOfCriminal
    df['typeOfCrime'] = typeOfCrime
    df['Vsr'] = Vsr
    df.to_csv("final.csv")

convertJsonToCSV("dataset.json")