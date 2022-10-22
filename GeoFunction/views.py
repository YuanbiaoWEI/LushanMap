import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import GeoFunction.models as models


# Create your views here.
@csrf_exempt
@login_required
def querybybound(request):
    param = json.loads(request.body.decode('utf-8'))
    BoundGeojson = param["BoundGeojson"]
    SQL = models.SQLQueryByBound(BoundGeojson)
    response = models.execSQL(SQL)
    FeatureCollection = {
        "type":"FeatureCollection",
        "features":[]
    }
    for eachpoint in response:
        feature = {
            "type": "Feature",
            "properties": {
                "name": eachpoint['name']
            },
            "geometry": {
                "type": "Point",
                "coordinates": [eachpoint['x'],eachpoint['y']]
            }
        }
        FeatureCollection["features"].append(feature)
    return JsonResponse(FeatureCollection)

@csrf_exempt
@login_required
def querybyname(request):
    param = json.loads(request.body.decode('utf-8'))
    name = param["name"]
    SQL = models.SQLQueryByName(name)
    response = models.execSQL(SQL)
    FeatureCollection = {
        "type": "FeatureCollection",
        "features": []
    }
    for eachpoint in response:
        feature = {
            "type": "Feature",
            "properties": {
                "name": eachpoint['name']
            },
            "geometry": {
                "type": "Point",
                "coordinates": [eachpoint['x'], eachpoint['y']]
            }
        }
        FeatureCollection["features"].append(feature)
    return JsonResponse(FeatureCollection)