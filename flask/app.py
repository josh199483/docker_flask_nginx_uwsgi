import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
# HOST = os.environ.get('DB_PORT_27017_TCP_ADDR')
# HOST = 'localhost'
# PORT = 27017
# MONGO_URI = "mongodb://{0}:{1}".format(HOST,PORT)
# client = MongoClient(MONGO_URI)
# db = client.test

# 'db'是docker service的名字
# client = MongoClient(
#     'localhost',
#     27017)
# db = client.tododb


@app.route('/')
def todo():
    # _items = db.tododb.find()
    # items = [item for item in _items]
    items = [{'name':'josh','age':23}]
    items1 = 'flask docker'

    return render_template('todo.html',items1=items1,items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)