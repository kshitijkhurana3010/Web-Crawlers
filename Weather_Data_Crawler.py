# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:39:59 2017

@author: kshitij
"""
import json
import urllib.request
import csv
from datetime import datetime, timedelta

From_Date = '20161201'
#To_Date = '20170331'

#From_Date = datetime.strptime(From_Date, '%Y%m%d').date()
#print(From_Date)
#From_Date = From_Date + timedelta(1)
#From_Date = From_Date.strftime('%Y%m%d') 
#print(From_Date)


def get_from_web_to_python(date):
    #urlData = weblink
    urlData = "http://api.wunderground.com/api/f0bc8c8eb066140c/history_"+ date + "/q/US/Newyork.json"
    print(urlData)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    jsonToPython = json.loads(data)
    return (jsonToPython)
    


with open ('E:\Rise Spring 2017\Advance Business Intelligence\Project\Dec2016.csv','w',newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        list_column_name  = [ 'Hour','Time & Date', 'Temperature', 'Snow', 'Rain', 'Wind Speed','humidity']
        a.writerow(list_column_name)
        #date = 20161201
        while (From_Date != '20170101'):
            #date = str(date)
            From_Date = datetime.strptime(From_Date, '%Y%m%d').date()
            From_Date = From_Date.strftime('%Y%m%d') 
            print(From_Date)
            jsonToPython = get_from_web_to_python(From_Date)   
            list_data = []
            i = 0;
            n=0;
            A = []
            M = '23'
            while(n < 24):
                try:
                    list_data.append(jsonToPython['history']['observations'][i]['date']['hour'])
                    list_data.append(jsonToPython['history']['observations'][i]['date']['pretty'])
                    list_data.append(jsonToPython['history']['observations'][i]['tempi'])
                    list_data.append(jsonToPython['history']['observations'][i]['snow'])
                    list_data.append(jsonToPython['history']['observations'][i]['rain'])
                    list_data.append(jsonToPython['history']['observations'][i]['wspdi'])
                    list_data.append(jsonToPython['history']['observations'][i]['hum'])
                #print("initial",A)
                    if (list_data[0] == A):
                        if (str(list_data[0]) == M):
                            n = n+1
                        
                        list_data = []
                        i = i + 1
                    
                    elif (list_data[0] != A):
                        A = list_data[0]
                        i = i + 1
                        n = n + 1
                        a.writerow(list_data)
                        list_data = []
                except:
                    n = 24
            From_Date = datetime.strptime(From_Date, '%Y%m%d').date()
            From_Date = From_Date + timedelta(1)
            From_Date = From_Date.strftime('%Y%m%d') 
            


    