#!/usr/bin/python
# -*-coding:utf-8-*-

from flask import Flask,render_template,request
import MySQLdb as mysql

con = mysql.connect(user='root',passwd='1qaz@WSX',host='192.168.146.130',db='myweb')

con.autocommit(True)
cur = con.cursor()
app = Flask(__name__)
import json

# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/')
def data():
    sql = 'select * from memory'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    # return json.dumps(arr)
	return render_template('index.html',data = json.dumps(arr))

@app.route('/new_memory',methods=['GET'])
def getnew():
    cur.execute('select * from memory order by time desc limit 1')
    v = cur.fetchone()
    top = [v[1]*1000,v[0]]
    print top
    return json.dumps(top)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)