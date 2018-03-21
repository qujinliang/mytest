# 面向对象
# 有意义的面向对象代码
# 类 = 面向对象
# 类、对象
# 类和对象

from moocseven.nine.c2 import Human

class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)
        self.score = 0

    def do_homework(self):
        print('english homework')

    # def marking(self, score):
    #     if score < 0:
    #         return '你个傻逼，怎么能打负分，能死你！'
    #     self.__score = score
    #     print(self.name + '同学本次的分数为：' + str(self.__score))

    # def print_file(self):
    #     print('name:' + self.name)
    #     print('age:' + str(self.age))

    # @classmethod
    # def plus_sum(cls):
    #     cls.i += 1
    #     print(cls.i)

student = Student('清华大学','屎大颗', 18)

print(student.name)
print(student.age)
print(student.school)
student.get_name()

# print('打印实例变量：' + student.name)
# print('打印类变量：' + str(Student.age))

