#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2017/4/22 14:40
"""

s = 'akdsakjhdjkashdjkhasjkdhasjkdhkjashdaskjhfoopnnm,ioqouiew'*100000

for i in s:
    for j in s:
        s.count(j)