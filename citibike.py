import requests
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.json import json_normalize
# database: 
import sqlite3 as lite


r = requests.get('http://www.citibikenyc.com/stations/json')
# Requires from pandas.io.json import json_normalize:
df = json_normalize(r.json()['stationBeanList'])

con = lite.connect('citi_bike.db')
cur = con.cursor()

with con:
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')



#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))


# SQL to create table: 
# CREATE TABLE citibike_reference (
#     id INT PRIMARY KEY,
#     totalDocks INT,
#     city TEXT,
#     altitude INT, 
#     stAddress2 TEXT,
#     longitude NUMERIC,
#     postalCode TEXT,
#     testStation TEXT,
#     stAddress1 TEXT,
#     stationName TEXT,
#     landMark TEXT,
#     latitude NUMERIC,
#     location TEXT
# )

