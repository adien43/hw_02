import json
import matplotlib.pyplot as plt


def readData():
    json_data = None
    with open('1880-2016.json', 'r') as f:
        json_data = json.load(f)
        #print(json_data)
        return json_data

def datasyn(json_data):
    x = []
    y = []
    #print(len(json_data))
    #print(json_data[0])
    #print(type(json_data[0]))

    #print(json_data[]["date"])
    #print(json_data[0]["stop-and-search"])
    for key in json_data.keys(): 
        if key == "description":
            pass
        else:
            #print(key)
            for years in json_data[key].keys():
                #print(years)
                if int(years) > 1949 and int(years)% 2 == 0:
                    x.append(years)
                    y.append(float(json_data[key][years]))
    return x, y

def readData1():
    json_data1 = None 
    with open ('110-pcp-ytd-12-1895-2016.json','r') as f:
        json_data1 = json.load(f)
    return json_data1
def datasyn1(json_data1):
    x1 = []
    y1 = []
    for key in json_data1.keys():
        if key == "description":
            pass
        else:
            print(key)
            for years in json_data1[key].keys():
                if int(years) > 195000 and int(years[0:4])% 2 == 0:
                    years_and_months = years
                    years = years[0:4]
                    x1.append(years)
                    y1.append(float(json_data1[key][years_and_months]["anomaly"]))
    
    #print(x1, y1)
    return x1, y1 

"""
def datasun(json_data1)
    x1 = []
    y1 = []
 
    return x, y
"""
def makeBarChart(x, y):
    plt.bar(x,y)
    plt.xlabel("Year")
    plt.ylabel("Anomalies")
    plt.title("Global Land and Ocean Temperature Anomalies")
    plt.xticks(rotation='vertical')
    plt.show()

def makeXxChart2(x, y, x1, y1):
    
    # plotting the line 1 points 
    plt.plot(x, y, label = "Global Land and Ocean Temperature Anomalies")
    # plotting the line 2 points 
    plt.plot(x1, y1, label = "Contiguous U.S., Precipitation Anomalies")
    plt.xlabel('Year')
    # Set the y axis label of the current axis.
    plt.ylabel('Anomalies')
    # Set a title of the current axes.
    plt.title('Global Land and Ocean Temperature anomalies against U.S Percipitation anomalies')
    # show a legend on the plot
    plt.legend()
    # Display a figure.
    plt.xticks(rotation='vertical')
    plt.show()
    #print(22)

if __name__=="__main__":
    json_data = readData()
    x, y = datasyn(json_data)
    json_data1 = readData1()
    x1, y1 = datasyn1(json_data1)
    makeBarChart(x, y)
    makeXxChart2(x, y, x1, y1)
    print(x,x1)
