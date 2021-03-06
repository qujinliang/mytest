'''
学生信息系统中数据为固定格式：
(名字，年龄，性别，邮箱地址，......)

学生数量很大为了减小存储开销，对每个学生信息用元组表示：
('Jim',16,'male','jim8721@gamail.com')
('LiLei',17,'male','lilei8721@gamail.com')
('Lucy',16,'male','lucy8721@gamail.com')
......
访问时，我们使用索引(index)访问，大量索引降低程序可读性，
如何解决这个问题？
'''

# 为元组中的每一个元素命名，提高程序可读性

# 方案一，给每个元素赋值一个变量名
NAME, AGE, SEX, EMAIL = range(4)
class Student:
    def student(self):
        student = ('Jim',16,'male','jim8721@gamail.com')
        return student

t = Student()
print(t.student()[NAME], t.student()[AGE])
