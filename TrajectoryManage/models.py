from django.db import models
import json
import datetime
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

def updateSQL(SQL):
    with connection.cursor() as cursor:
        cursor.execute(SQL)

def SQLSearchTrajectoryByUsername(name):
    SQL = "select ST_AsGeoJSON(geom) as trajectory from trajectory where owner like '"+name+"';"
    return SQL

def UpdateTrajectory(geometry, username, filename):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    SQL = """insert into trajectory (owner,time,name,length,geom) values ('"""+ username +"""','"""+ today +"""','"""+ filename +"""',
            ST_Length(
                ST_Force2D(
                    ST_GeomFromGeoJSON('"""+ json.dumps(geometry) +"""')
                )
            )
            ,
            st_transform(
                ST_Force2D(
                    ST_Multi(
                        ST_GeomFromGeoJSON('"""+ json.dumps(geometry) +"""')
                    )
                )
            ,3857))"""
    return SQL

def DeleteTrajectory(idtuple):
    SQL = """ delete from trajectory where gid in (""" + idtuple +""");"""
    return SQL