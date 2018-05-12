from random import randint
from collections import deque


NUM = randint(0,100)
D = deque([],5)

def guess(pl):
    pl = pl
    if pl == NUM:
        print('right')
        return True
    elif pl < NUM:
        print('你输入的数字小了')
        return False
    elif pl > NUM:
        print('你输入的数字大了')
        return False

while True:
    pl = input('请输入一个数字：')
    if pl.isdigit():
        k = int(pl)
        D.append(k)
        D = list(D)
        if guess(k):
            break
    elif pl == 'h?':
        print(D)