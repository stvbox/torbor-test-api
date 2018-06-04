#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bottle import Bottle, run, response, request
from common import is_auth
app = Bottle()

maps_api_key = 'AIzaSyCt-dlf4PG78Gp9ihWD-jPxoTzM4uu-a7k'

@app.route('/api/')
@is_auth

def calc_dist():
    city1 = request.query.get('city1')
    city2 = request.query.get('city2')
    price = request.query.get('price')
    payload = {'origins': city1, 'destinations': city2, 'key': maps_api_key}
    mapsresponse = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=payload)
    response.content_type = 'application/json'
    return mapsresponse

run(app, host='0.0.0.0', port=8080)


