from django.db import models
import json
from django.db import connection

# Create your models here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# Both select and update can be executed
def execSQL(SQL):
    with connection.cursor() as cursor:
        cursor.execute(SQL)
        result = dictfetchall(cursor)
    return result

def SQLQueryByBound(BoundGeoJson):
    #print("BoundGeoJson:",BoundGeoJson)
    SQL = 'select name,ST_X(ST_Transform(geom,3857)) as x,ST_Y(ST_Transform(geom,3857)) as y from nature_point where ST_Contains( ST_Transform( ST_SetSRID( ST_GeomFromGeojson(\'{"type":"Polygon","coordinates":' + json.dumps(BoundGeoJson) + '}\'),3857), 4326), nature_point.geom) = true'
    return SQL

def SQLQueryByName(name):
    SQL = 'select name,ST_X(ST_Transform(geom,3857)) as x,ST_Y(ST_Transform(geom,3857)) as y from nature_point where name like ' + name + ';'
    return SQL