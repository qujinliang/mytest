# reduce
from functools import reduce

list_x = list(range(1,10))
s  = sum(list_x)
print(s)
r = reduce(lambda x,y:x+y,list_x )
print(r)

traveler = [(1,2),(3,-2),(-1,4)]
rr = reduce(lambda x,y:x+y, traveler)
print(rr)
sr = reduce(lambda x,y:x+y,rr)
print(sr)