import json
import os
import time

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import GeoFunction.models as models
from LushanMap import settings


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

@csrf_exempt
@login_required
def heatmap(request):
    SQL = models.SQLAllPoint()
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

@csrf_exempt
@login_required
def servicearea(request):
    SQL = models.SQLServiceArea()
    response = models.execSQL(SQL)
    FeatureCollection = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "name": "ServiceArea"
                },
                "geometry": json.loads(response[0]['st_asgeojson'])
            }
        ]
    }
    return JsonResponse(FeatureCollection)

@csrf_exempt
@login_required
def mytrajectory(request):
    SQL = models.SQLSearchTrajectoryByUsername(request.user.username)
    response = models.execSQL(SQL)
    FeatureCollection = {
        "type": "FeatureCollection",
        "features": []
    }
    for eachline in response:
        feature = {
            "type": "Feature",
            "geometry": json.loads(eachline['trajectory'])
        }
        FeatureCollection["features"].append(feature)

    return JsonResponse(FeatureCollection)

@csrf_exempt
@login_required
def uploadtrajectory(request):
    response = {}

    # 解析前端传来的数据流文件
    fileStream = request.FILES['UserTrajectory']
    fileData = json.loads(fileStream.file.read().decode())

    # 解析geojson文件是否合法
    features = fileData.get('features')
    geometry = fileData.get('geometry')
    geometries = []
    faillist = []
    if features:
        for eachfeature in features:
            if eachfeature.get('geometry')['type'] == 'MultiLineString' or eachfeature.get('geometry')['type'] == 'LineString':
                geometries.append(eachfeature.get('geometry'))
            else:
                faillist.append(eachfeature)
    elif geometry:
        if geometry['type'] == 'MultiLineString' or geometry['type'] == 'LineString':
            geometries.append(geometry)
        else:
            faillist.append(geometry)
    else:
        response['detail'] = '无法解析该文件，原因：无geometry属性。'
        return render(request,'Map/UploadTrajectory.html', response)

    # 将合法数据保存至数据库


    # 给前端提交反馈
    if features:
        response['detail'] = ('成功保存了 %d 个轨迹, 失败了 %d 个, 若几何要素非线要素或多线要素则无法保存。' %(len(features)-len(faillist), len(faillist)))
        return render(request,'Map/UploadTrajectory.html', response)
    else:
        response['detail'] = ('成功保存了 %d 个轨迹, 失败了 %d 个, 若几何要素非线要素或多线要素则无法保存。' % (1-len(faillist),len(faillist)))
        return render(request,'Map/UploadTrajectory.html', response)