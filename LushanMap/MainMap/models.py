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

def SQLSearchTrajectoryByUsername(name):
    SQL = "select gid,time,length,name from trajectory where owner like '"+name+"';"
    return SQL