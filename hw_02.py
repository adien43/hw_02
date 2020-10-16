import json
import matplotlib.pyplot as plt


#def readData():
json_data = None
with open('crimes-street-dates.json', 'r') as f:
    json_data = json.load(f)
    print(json_data)
    #return json_data
'''
def datasyn(json_data):
    x = []
    y = []
    print(len(json_data))
    #print(json_data[0])
    #print(type(json_data[0]))

    #print(json_data[0]["date"])
    #print(json_data[0]["stop-and-search"])

    for i in range(len(json_data)):
        #print(json_data[i]["date"])
        #print(len(json_data[i]["stop-and-search"]))
        #print(json_data[i]["date"].startswith('2019'))
        if json_data[i]["date"].startswith('2019'):
            x.append(json_data[i]["date"])
            y.append(len(json_data[i]["stop-and-search"]))

    #x = json_data[0]["date"]
    #y = len(json_data[0]["stop-and-search"])

    return x, y

def makeBarChart(x, y):
    plt.plot(x,y)
    plt.xticks(rotation='vertical')
    plt.show()

def makeXxChart2(x, y):
    print(22)
'''
if __name__=="__main__":
    json_data = readData()
    x, y = datasyn(json_data)
    makeBarChart(x, y)
    #makeXxChart2(x, y)
