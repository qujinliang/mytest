"""
 Created by qujl on 2018-06-12
"""
__author__ = 'qujl'
from random import randint
from collections import Counter

ball = [randint(1,11) for _ in range(100)]
print(Counter(ball).most_common(11))