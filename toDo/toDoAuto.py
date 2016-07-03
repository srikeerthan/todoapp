import click,os,sys
import MySQLdb
import django
import datetime


sys.path.append("C:/summerClass/jango/toDoProject")
os.environ["DJANGO_SETTINGS_MODULE"] = "toDoProject.settings"
django.setup()

from toDo.models import *


@click.group()
def onlinedb():
    """database commands"""
    pass
@onlinedb.command()
@click.argument('username')
@click.argument('password')
@click.argument('dbname')
def createdb(username,password,dbname):
    """create database"""
    conn=MySQLdb.connect(host='localhost',user=username,passwd=password)
    cursor=conn.cursor()
    query='CREATE DATABASE '+dbname
    cursor.execute(query)

@onlinedb.command()
def populatedb():
    """populatedb database"""
    for i in range(10):
        l=ToDoList(name='todo_list_'+str(i),created=datetime.date.today())
        l.save()
        for j in range(5):
            I=ToDoItem(description='description_'+str(i),duedate=datetime.date.today(),name=l)
            I.save()
    pass

if __name__=='__main__':
    onlinedb()