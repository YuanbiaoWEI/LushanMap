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
    featurejson = {
        "type": "Feature",
        "geometry": {
            "type": "MultiPoint",
            "coordinates": []
        }
    }
    for eachpoint in response:
        coordin = [eachpoint['x'],eachpoint['y']]
        featurejson['geometry']["coordinates"].append(coordin)

    return JsonResponse(featurejson)
