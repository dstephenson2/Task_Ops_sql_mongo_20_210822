from flask import Flask, request, jsonify # pip install flask for every project env
import mysql.connector as conn # pip install mysql-connector-python

app = Flask(__name__) # create an app

mydb = conn.connect(host="localhost", user="root", passwd="God!77merciful") # create and establish connection with mysql
cursor = mydb.cursor() # create cursor to execute queries
cursor.execute("create database if not exists task4ops") # create database
cursor.execute("create table if not exists task4ops.mysqltable(name varchar(30), number int)") # create table schema, schema means structure columns and col names

@app.route('/insert', methods=['POST'])
def insert():
    if (request.method == 'POST'):
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into task4ops.mysqltable values(%s , %s)",(name , number)) # %s is place holder
        mydb.commit() # call commit
        return jsonify(str('successfully inserted'))

@app.route('/update', methods=['POST']) # calling the below function through api (flask)
def update():
    if (request.method == 'POST'):
        get_name = request.json['get_name']
        cursor.execute("update task4ops.mysqltable set number = number + 500 where name = %s", (get_name,))
        mydb.commit()
        return jsonify(str('updated successfully'))

@app.route('/delete', methods=['POST'])
def delete():
    if (request.method == 'POST'):
        del_name = request.json['del_name']
        cursor.execute("delete from task4ops.mysqltable where name = %s", (del_name, ))
        mydb.commit()
        return jsonify(str('deleted successfully'))

@app.route('/fetch', methods=['POST'])
def fetch_data():
    cursor.execute("select * from task4ops.mysqltable")
    for i in cursor.fetchall(): # fetches all (or all remaining) rows of a query result set and returns a list of tuples
        return jsonify(str(i))

@app.route('/fetchall', methods=['POST'])
def fetch_data_list():
    cursor.execute("select * from task4ops.mysqltable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

if __name__ == '__main__':
    app.run()
