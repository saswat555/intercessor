#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import pymongo
from pymongo import MongoClient
from pmdarima import auto_arima
import warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.arima_model import ARIMA
from add import *
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bananaforecast')
def bananaforecast():

    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):

            self.dBName = dBName
            self.collectionName = collectionName

            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/banana?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )

            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            """
............:param path: Path os csv File
............:return: None
............"""

            df = pd.read_csv('forebanana.csv')
            data = df.to_dict('records')

            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='banana', collectionName='banana')
    airline = pd.read_csv('banana.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    from pmdarima import auto_arima
    import warnings
    warnings.filterwarnings('ignore')
    from statsmodels.tsa.arima_model import ARIMA

    model = ARIMA(airline, order=(0, 1, 1))

    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forebanana.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forebanana.csv')
    mongodb.InsertData(path='forebanana.csv')
    return render_template('success.html')


@app.route('/appleforecast')
def appleforecast():

    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/apple?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('foreapple.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='apple', collectionName='apple')
    airline = pd.read_csv('apples.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(1, 0, 0))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'foreapple.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('foreapple.csv')
    mongodb.InsertData(path='foreapple.csv')
    return render_template('success.html')
@app.route('/watermelonforecast')
def watermelonforecast():

    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/watermelon?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forewatermelon.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='watermelon', collectionName='watermelon')
    airline = pd.read_csv('watermelon.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forewatermelon.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forewatermelon.csv')
    mongodb.InsertData(path='forewatermelon.csv')
    return render_template('success.html')
@app.route('/grapesforecast')
def grapesforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/grapes?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('foregrapes.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='grapes', collectionName='grapes')
    airline = pd.read_csv('grapes.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(1, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'foregrapes.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('foregrapes.csv')
    mongodb.InsertData(path='foregrapes.csv')
    return render_template('success.html')

@app.route('/mangoforecast')
def mangoforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/mango?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('foremango.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='mango', collectionName='mango')
    airline = pd.read_csv('mango.csv', index_col='Date',
                          parse_dates=True)

    airline.head()

    model = ARIMA(airline, order=(0, 1, 2))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'foremango.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('foremango.csv')
    mongodb.InsertData(path='foremango.csv')
    return render_template('success.html')


@app.route('/beefforecast')
def beefforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/beef?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forebeef.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='grapes', collectionName='grapes')
    airline = pd.read_csv('grapes.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0,2,2))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forebeef.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forebeef.csv')
    mongodb.InsertData(path='forebeef.csv')
    return render_template('success.html')

@app.route('/chickenforecast')
def chickenforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/chicken?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forechicken.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='chicken', collectionName='chicken')
    airline = pd.read_csv('chicken.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 0))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forechicken.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forechicken.csv')
    mongodb.InsertData(path='forechicken.csv')
    return render_template('success.html')

@app.route('/crabsforecast')
def crabsforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/crabs?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forecrabs.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='crabs', collectionName='crabs')
    airline = pd.read_csv('crabs.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forecrabs.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forecrabs.csv')
    mongodb.InsertData(path='forecrabs.csv')
    return render_template('success.html')

@app.route('/pomfretforecast')
def pomfretforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/pomfret?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forepomfret.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='pomfret', collectionName='pomfret')
    airline = pd.read_csv('pomfret.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(1, 1, 2))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forepomfret.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forepomfret.csv')
    mongodb.InsertData(path='forepomfret.csv')
    return render_template('success.html')



@app.route('/porkforecast')
def porkforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/pork?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forepork.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='pork', collectionName='pork')
    airline = pd.read_csv('pork.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(2, 0, 0))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forepork.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forepork.csv')
    mongodb.InsertData(path='forepork.csv')
    return render_template('success.html')

@app.route('/prawnsforecast')
def prawnsforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/prawns?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('foreprawns.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='prawns', collectionName='prawns')
    airline = pd.read_csv('prawns.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'foreprawns.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('foreprawns.csv')
    mongodb.InsertData(path='foreprawns.csv')
    return render_template('success.html')

@app.route('/rohuforecast')
def rohuforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/rohu?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forerohu.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='rohu', collectionName='rohu')
    airline = pd.read_csv('rohu.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(2, 1, 0))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forerohu.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forerohu.csv')
    mongodb.InsertData(path='forerohu.csv')
    return render_template('success.html')


@app.route('/milkforecast')
def milkforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/milk?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('foremilk.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='milk', collectionName='milk')
    airline = pd.read_csv('milk.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'foremilk.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('foremilk.csv')
    mongodb.InsertData(path='foremilk.csv')
    return render_template('success.html')

@app.route('/curdforecast')
def curdforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/curd?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forecurd.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='curd', collectionName='curd')
    airline = pd.read_csv('curd.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forecurd.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forecurd.csv')
    mongodb.InsertData(path='forecurd.csv')
    return render_template('success.html')

@app.route('/butterforecast')
def butterforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/butter?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forebutter.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='butter', collectionName='butter')
    airline = pd.read_csv('butter.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forebutter.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forebutter.csv')
    mongodb.InsertData(path='forebutter.csv')
    return render_template('success.html')

@app.route('/cheeseforecast')
def cheeseforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/cheese?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forecheese.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='cheese', collectionName='cheese')
    airline = pd.read_csv('cheese.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 1))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forecheese.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forecheese.csv')
    mongodb.InsertData(path='forecheese.csv')
    return render_template('success.html')


@app.route('/paneerforecast')
def paneerforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/paneer?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('forepaneer.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='paneer', collectionName='paneer')
    airline = pd.read_csv('paneer.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 2))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'forepaneer.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('forepaneer.csv')
    mongodb.InsertData(path='forepaneer.csv')
    return render_template('success.html')

@app.route('/muttonforecast')
def muttonforecast():
    class MongoDB(object):

        def __init__(self, dBName=None, collectionName=None):
            self.dBName = dBName
            self.collectionName = collectionName
            self.client = \
                MongoClient('mongodb://saswatp99:saswat05@cluster0-shard-00-00-sw2f4.mongodb.net:27017,cluster0-shard-00-01-sw2f4.mongodb.net:27017,cluster0-shard-00-02-sw2f4.mongodb.net:27017/mutton?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
                            )
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]

        def InsertData(self, path=None):
            df = pd.read_csv('foremutton.csv')
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            print('All the Data has been Exported to Mongo DB Server .... ')

    mongodb = MongoDB(dBName='mutton', collectionName='mutton')
    airline = pd.read_csv('mutton.csv', index_col='Date',
                          parse_dates=True)

    airline.head()
    model = ARIMA(airline, order=(0, 1, 0))
    result = model.fit()
    forecast = result.predict(start=len(airline), end=len(airline)
                              + 14, typ='levels').rename('Forecast')
    forecast = pd.DataFrame(forecast)
    filename = 'foremutton.csv'
    f = open(filename, 'w+')
    f.close()
    forecast.to_csv('foremutton.csv')
    mongodb.InsertData(path='foremutton.csv')
    return render_template('success.html')


@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/fruit')
def fruit():
    return render_template('fruit.html')

@app.route('/fish')
def fish():
    return render_template('fish.html')

@app.route('/meat')
def meat():
    return render_template('meat.html')

@app.route('/banana')
def banana():
    return render_template('banana.html')

@app.route('/apple')
def apple():
    return render_template('apple.html')


@app.route('/mango')
def mango():
    return render_template('mango.html')

@app.route('/grapes')
def grapes():
    return render_template('grapes.html')

@app.route('/watermelon')
def watermelon():
    return render_template('watermelon.html')

@app.route('/rohu')
def rohu():
    return render_template('rohu.html')

@app.route('/catfish')
def catfish():
    return render_template('crabs.html')
@app.route('/crabs')
def crabs():
    return render_template('crabs.html')
@app.route('/prawns')
def prawns():
    return render_template('prawns.html')

@app.route('/adda',methods=["GET", "POST"])
def adda():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addapple(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addb',methods=["GET", "POST"])
def addb():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addbanana(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addg',methods=["GET", "POST"])
def addg():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addgrapes(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'
    

@app.route('/addm',methods=["GET", "POST"])
def addm():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addmango(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addw',methods=["GET", "POST"])
def addw():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addwatermelon(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addbe',methods=["GET", "POST"])
def addbe():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addbeef(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addch',methods=["GET", "POST"])
def addch():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addchicken(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addcr',methods=["GET", "POST"])
def addcr():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addcrabs(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'


@app.route('/addpom',methods=["GET", "POST"])
def addpom():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addpomfret(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addpo',methods=["GET", "POST"])
def addpo():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addpork(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addpr',methods=["GET", "POST"])
def addpr():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addprawn(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addmi',methods=["GET", "POST"])
def addmi():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addmilk(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'
@app.route('/addbu',methods=["GET", "POST"])
def addbu():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addbutter(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addcu',methods=["GET", "POST"])
def addcu():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addcurd(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addpa',methods=["GET", "POST"])
def addpa():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addpaneer(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addche',methods=["GET", "POST"])
def addche():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addcheese(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'

@app.route('/addmu',methods=["GET", "POST"])
def addmu():
    if request.method == 'POST':
        Date=request.form['Date']
        GDP=request.form['GDP']
        status = addmutton(Date, GDP)
        return render_template('successupdate.html')
    else:
        return 'failed'


@app.route('/appleform')
def appleform():
    return render_template('addapple.html')


@app.route('/bananaform')
def bananaform():
    return render_template('addbanana.html')

@app.route('/grapesform')
def grapesform():
    return render_template('addgrapes.html')

@app.route('/mangoform')
def mangoform():
    return render_template('addmango.html')

@app.route('/watermelonform')
def watermelonform():
    return render_template('addwatermelon.html')


@app.route('/beefform')
def beefform():
    return render_template('addbeef.html')


@app.route('/chickenform')
def chickenform():
    return render_template('addchicken.html')

@app.route('/crabsform')
def crabsform():
    return render_template('addcrabs.html')


@app.route('/prawnform')
def prawnform():
    return render_template('addprawn.html')

@app.route('/porkform')
def porkform():
    return render_template('addpork.html')

@app.route('/pomfretform')
def pomfretform():
    return render_template('addpomfret.html')

@app.route('/milkform')
def milkform():
    return render_template('addmilk.html')

@app.route('/butterform')
def butterform():
    return render_template('addbutter.html')
@app.route('/cheeseform')
def cheeseform():
    return render_template('addcheese.html')
@app.route('/paneerform')
def paneerform():
    return render_template('addpaneer.html')
@app.route('/curdform')
def curdform():
    return render_template('addcurd.html')
@app.route('/rohuform')
def rohuform():
    return render_template('addrohu.html')
@app.route('/muttonform')
def muttonform():
    return render_template('addmutton.html')
@app.route('/curd')
def curd():
    return render_template('curd.html')

@app.route('/appletable')
def appletable():
    data = pd.read_csv('foreapple.csv')

    return render_template('appletable.html',tables=[data.to_html()])

@app.route('/bananatable')
def bananatable():
    data = pd.read_csv('forebanana.csv')

    return render_template('bananatable.html',tables=[data.to_html()])

@app.route('/grapestable')
def grapestable():
    data = pd.read_csv('foregrapes.csv')

    return render_template('grapestable.html',tables=[data.to_html()])

@app.route('/mangostable')
def mangotable():
    data = pd.read_csv('foremango.csv')

    return render_template('mangotable.html',tables=[data.to_html()])

@app.route('/watermelontable')
def watermelontable():
    data = pd.read_csv('forewatermelon.csv')

    return render_template('watermelontable.html',tables=[data.to_html()])

@app.route('/prawntable')
def prawntable():
    data = pd.read_csv('foreprawns.csv')

    return render_template('prawntable.html',tables=[data.to_html()])


@app.route('/chickentable')
def chickentable():
    data = pd.read_csv('forechicken.csv')

    return render_template('chickentable.html',tables=[data.to_html()])

@app.route('/crabstable')
def crabstable():
    data = pd.read_csv('forecrabs.csv')

    return render_template('crabtable.html',tables=[data.to_html()])

@app.route('/pomfrettable')
def pomfrettable():
    data = pd.read_csv('forepomfret.csv')

    return render_template('pomfrettable.html',tables=[data.to_html()])

@app.route('/rohutable')
def rohutable():
    data = pd.read_csv('forerohu.csv')

    return render_template('rohutable.html',tables=[data.to_html()])

@app.route('/beeftable')
def beeftable():
    data = pd.read_csv('forebeef.csv')

    return render_template('beeftable.html',tables=[data.to_html()])

@app.route('/porktable')
def porktable():
    data = pd.read_csv('forepork.csv')

    return render_template('porktable.html',tables=[data.to_html()])

@app.route('/muttontable')
def muttontable():
    data = pd.read_csv('foremutton.csv')

    return render_template('muttontable.html',tables=[data.to_html()])

@app.route('/milktable')
def milktable():
    data = pd.read_csv('foremilk.csv')

    return render_template('milktable.html',tables=[data.to_html()])

@app.route('/buttertable')
def buttertable():
    data = pd.read_csv('forebutter.csv')

    return render_template('buttertable.html',tables=[data.to_html()])

@app.route('/cheesetable')
def cheesetable():
    data = pd.read_csv('forecheese.csv')

    return render_template('cheesetable.html',tables=[data.to_html()])

@app.route('/paneertable')
def paneertable():
    data = pd.read_csv('forepaneer.csv')

    return render_template('paneertable.html',tables=[data.to_html()])

@app.route('/curdtable')
def curdtable():
    data = pd.read_csv('forecurd.csv')

    return render_template('curdtable.html',tables=[data.to_html()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('home.html')
    return render_template('login.html', error=error)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/vhome')
def vhome():
    return render_template('vhome.html')

@app.route('/nstock')
def nstock():
    return render_template('nstock.html')

@app.route('/cstock')
def cstock():
    return render_template('checkstock.html')
 
@app.route('/dairy')
def dairy():
    return render_template('dairy.html')

@app.route('/vdairy')
def vdairy():
    return render_template('vdairy.html')

@app.route('/vfruit')
def vfruit():
    return render_template('vfruit.html')
@app.route('/vmeat')
def vmeat():
    return render_template('vmeat.html')
@app.route('/vfish')
def vfish():
    return render_template('vfish.html')

@app.route('/home')
def home():
    return render_template('home.html')    
    
@app.route('/butter')
def butter():
    return render_template('butter.html')    
    
@app.route('/cheese')
def cheese():
    return render_template('cheese.html')    
    
@app.route('/milk')
def milk():
    return render_template('milk.html') 
@app.route('/paneer')
def paneer():
    return render_template('paneer.html') 
@app.route('/mutton')
def mutton():
    return render_template('mutton.html') 

@app.route('/pork')
def pork():
    return render_template('pork.html') 
@app.route('/beef')
def beef():
    return render_template('beef.html')
@app.route('/chicken')
def chicken():
    return render_template('chicken.html')  
@app.route('/pomfret')
def pomfret():
    return render_template('pomfret.html')

@app.route('/vbanana')
def vbanana():
    return render_template('vbanana.html')

@app.route('/vapple')
def vapple():
    return render_template('vapple.html')


@app.route('/vmango')
def vmango():
    return render_template('vmango.html')

@app.route('/vgrapes')
def vgrapes():
    return render_template('vgrapes.html')

@app.route('/vwatermelon')
def vwatermelon():
    return render_template('vwatermelon.html')

@app.route('/vrohu')
def vrohu():
    return render_template('vrohu.html')

@app.route('/vcrabs')
def vcrabs():
    return render_template('vcrabs.html')
@app.route('/vprawns')
def vprawns():
    return render_template('vprawns.html')

@app.route('/vbutter')
def vbutter():
    return render_template('vbutter.html')    
    
@app.route('/vcheese')
def vcheese():
    return render_template('vcheese.html')    
    
@app.route('/vmilk')
def vmilk():
    return render_template('vmilk.html') 
@app.route('/vpaneer')
def vpaneer():
    return render_template('vpaneer.html') 
@app.route('/vmutton')
def vmutton():
    return render_template('vmutton.html') 

@app.route('/vpork')
def vpork():
    return render_template('vpork.html') 
@app.route('/vbeef')
def vbeef():
    return render_template('vbeef.html')
@app.route('/vchicken')
def vchicken():
    return render_template('vchicken.html')  
@app.route('/vpomfret')
def vpomfret():
    return render_template('vpomfret.html')
@app.route('/vcurd')
def vcurd():
    return render_template('vcurd.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/waste')
def waste():
    return render_template('waste.html')



if __name__ == '__main__':
    app.run(debug=True)
