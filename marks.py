  
import plotly.express as px
import csv
import numpy as np

def getDataSource(DataPath):
    RollNo = []
    MarksInPercentage = []
    with open (DataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Temperature.append(float(row["RollNo"]))
            IceCreamSales.append(float(row["MarksInPercentage"])     
        return {"x":RollNo,"y":MarksInPercentage}

def findCo_Relation(DataSource):
    corelation = np.corrcoef(DataSource["x"],DataSource["y"])
    print("Co-Relation Between Roll no and temperature: \n --->",corelation[0,1])

def Main():
    createDataPth = "marks.csv"
    DataSource = getDataSource(createDataPth)
    findCo_Relation(DataSource)

Main()