# 如何在列表，字典，集合中根据条件筛选数据？

from random import randint

data = [randint(-10, 10) for _ in range(10)]


class FilterList:
    # 1.使用filter函数
    def filterlist(data):
        data2 = [filter(lambda x: x >= 0, data)]
        return data2

    # 2.使用列表解析
    def list_analysis(data):
        data3 = [x for x in data if x >= 0]
        return data3


#print(FilterList.list_analysis(data))


# 3.字典使用列表解析
# 需求: 筛选出21个人中分数80及以上的
d = {x: randint(60, 100) for x in range(1, 21)}
class MapAnalysis:
    def mapanalysis(data):
        # for k,v in d.items同时迭代key value
        # if 判断value 大于等于80
        # 然后赋值给k : v
        data = {k: v for k, v in d.items() if v >= 80}
        return data

    def jihe(data):
        # 集合解析
        # 筛选出能被3整除的数
        data = {x for x in d if x % 3 ==0}
        return data

print(MapAnalysis.jihe(d))
