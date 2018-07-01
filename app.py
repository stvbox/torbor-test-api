#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests, json
from bottle import Bottle, run, response, request, get, post, static_file
from common import is_auth
app = Bottle()

maps_api_key = 'AIzaSyCt-dlf4PG78Gp9ihWD-jPxoTzM4uu-a7k'

@app.route('/<filename>')
def server_static(filename):
    print filename
    return static_file(filename, root='./')

@app.route('/static/js/<filename>')
def server_static(filename):
    print filename
    return static_file(filename, root='./static/js/')

@app.route('/static/css/<filename>')
def server_static(filename):
    print filename
    return static_file(filename, root='./static/css/')

@app.route('/static/assets/<filename>')
def server_static(filename):
    print filename
    return static_file(filename, root='./static/assets/')

@app.route('/api/geocoding')
#@app.route('/api/geocoding', method='GET')
#def test_get():
#    req = { 'address': "Краснодар", 'key': maps_api_key }
#    mapsresponse = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=req)
#    response.content_type = 'application/json'
#    return mapsresponse

@app.route('/api/geocoding', method='POST')
def geocoding():
    
    postdata = request.body.read()
    postdata = json.loads(postdata)
    print postdata #this goes to log file only, not to client

    address = postdata['address']
    req = { 'address': address, 'key': maps_api_key }
    mapsresponse = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=req)
    response.content_type = 'application/json'

    return {
        'url': mapsresponse.url,
        'data': json.loads(mapsresponse.text),
        'request': req
    }

@app.route('/api/routing', method='POST')
def routing():
    postdata = request.body.read()
    postdata = json.loads(postdata)
    print postdata #this goes to log file only, not to client

    city1 = 'place_id:' + postdata['places'][0]
    city2 = 'place_id:' +  postdata['places'][1]

    payload = {'origins': city1, 'destinations': city2, 'key': maps_api_key}

    mapsresponse = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=payload)
    response.content_type = 'application/json'

    return {
        'url': mapsresponse.url,
        'data': json.loads(mapsresponse.text),
        'request': payload
    }


@app.route('/api/')
#@is_auth

def calc_dist():
    city1 = request.query.get('city1')
    city2 = request.query.get('city2')
    #price = request.query.get('price')
    payload = {'origins': city1, 'destinations': city2, 'key': maps_api_key}
    mapsresponse = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params=payload)
    response.content_type = 'application/json'
    return mapsresponse

run(app, host='0.0.0.0', port=8080)


