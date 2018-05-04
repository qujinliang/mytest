"""
 Created by qujl on 2018-04-28
"""
__author__ = 'qujl'
import json

with open('rizhi.txt', 'r') as f:
    data= []
    for i in f:
        ll = i.replace('=',':').strip('\n')
        data.append(ll)
    print(json.dumps(data))

