
'''
1.用字典映射代替switch case语句
'''
DAY = 2
def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unkown'

switcher = {
    0 : get_sunday,
    1 : get_monday,
    2 : get_tuesday
}

result = switcher.get(DAY, get_default)()
print(result)
