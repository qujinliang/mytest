# map
import random

list_x = list(range(1,8))
list_y = list(range(1,9))

f = map(lambda x,y : x * x + y, list_x,list_y)
print(list(f))