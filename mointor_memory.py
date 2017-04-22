#!/usr/bin/python
# -*-coding:utf-8-*-

import time
import MySQLdb as mysql


db = mysql.connect(user="root",passwd="1qaz@WSX",db="myweb",host="192.168.146.130")
db.autocommit(True)
cur = db.cursor()


def memory_stat():
    mem = {}
    f = open("/proc/meminfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2: continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = float(var) / 1024.0
    t = int(time.time())
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    sql = 'insert into memory (memory,time) value (%s,%s)'%(mem['MemUsed'],t)
    cur.execute(sql)
    print mem['MemUsed']

while True:
    time.sleep(1)
    memory_stat()