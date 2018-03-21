def city_temp(**param):
    for key, value in param.items():
        if key == 'bj':
            print(key,value)
    pass
a = {'bj':'12c'}
city_temp(bj='10c',sh='20c',sz='25c')
city_temp(**a)
