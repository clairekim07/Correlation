import csv
import numpy as np
import plotly.express as plot
def getDataSource(data_path):
    with open("sleep.csv") as file:
        sleep = []
        coffee = []
        df = csv.reader(file)
        for f in df:
            sleep.append(float(f["sleep in hours"]))
            coffee.append(float(f["Coffee in ml"]))
        return {"x":sleep,"y":coffee,}
        
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between hours of sleep and ml of coffee is:" + str(correlation))
            


def setup():
    data_path = "/Users/claire/Desktop/python"
    sc = plot.scatter(data_path,x=sleep,y=coffee)
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
