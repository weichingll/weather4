from flask import Flask
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
currentDateAndTime = datetime.now()
"""
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello,World"

if __name__=="__main__":
    app.run()
"""
#爬蟲

url="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-ECA1DCB0-4E41-4652-A560-818FECF67A13&format=JSON"
respond=requests.get(url)
data=respond.json()
finaldata=data["records"]["location"]
a=""
i=0
for k in finaldata:
    a=a+(k["locationName"]+"<br/>&ensp;天氣狀況為："+k["weatherElement"][0]["time"][0]["parameter"]["parameterName"]+"<br/>"+"&ensp;氣溫:"+k["weatherElement"][2]["time"][0]["parameter"]["parameterName"]+"度c"+"<br/>")
    #a.append([])
    #a[i].append(k["locationName"])
    #a[i].append("天氣狀況為：")
    #a[i].append(k["weatherElement"][0]["time"][0]["parameter"]["parameterName"])
    #a[i].append(" 氣溫:")
    #a[i].append(k["weatherElement"][2]["time"][0]["parameter"]["parameterName"])
    #a[i].append("度c")
    #i+=1
    #print(" 氣溫:",k["weatherElement"][2]["time"][0]["parameter"]["parameterName"],"度c")
a=a+("最後更新時間："+str(currentDateAndTime))

for k in a:
    for j in k:
        print(j,end=" ")
    print()

app=Flask(__name__)
@app.route("/")
def hello():
    return a

if __name__=="__main__":
    app.run()
