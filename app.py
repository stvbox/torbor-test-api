#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bottle import Bottle, run, response
app = Bottle()


token = 'fgh8974yhfkh4'
maps_api_key = 'AIzaSyCt-dlf4PG78Gp9ihWD-jPxoTzM4uu-a7k'

@app.route('/api/'+token+'/city1=:city1&city2=:city2&price=:price')
def calc_dist(city1, city2, price):
    payload = {'origins': city1, 'destinations': city2, 'key': maps_api_key}
    mapsresponse = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=payload)
    response.content_type = 'application/json'
    return mapsresponse

run(app, host='0.0.0.0', port=8080)

