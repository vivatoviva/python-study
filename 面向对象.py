import types
# 类的概念
class Student(object):
    def __init__(self, name, score, hah):
        self.__name = name  # 私有变量
        self.score = score
        self._hah = hah # 视为私有变量
    
    def print_score(self):
        print('%s 成绩是： %s' % (self.__name, self.score))

ligen = Student('ligen', 56, 'hah')
ligen.print_score()

class NStudent(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError('名称不正确!')
        self.__name = name

    def set_gender(self, gender):
        if gender not in ('male', 'female'):
            raise ValueError('性别错误')
        self.__gender = gender

# 多态


# 获取对象类型

print(type(123))

print(type(ligen) == Student)

# 获取继承关系

print(isinstance(ligen, Student))

# 判断是list或者tuple
isinstance([1, 2, 3], (list, tuple))


# 类似__len__的属性和方法在python中都是由特殊意义的，例如你试着使用len(str)方法，实际str.__len__()

# class Test(object):
#     def __haha__():
#         return 1
# a = Test();
# print(haha(a))

# 自己定义的是没有作用的

# 不知道对象内部是不是含有这个属性的时候可以使用下面三个函数
# getattr(obj, attr, defaultValue)
# hasattr(obj, attr)
# setattr(obj, attr, value)

# 实例属性和类属性
class Student(object):
    count = 0

    def __init__(self):
        Student.count +=1
a = Student()
b = Student()
print(Student.count)
    
# 限制实例属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'ligen'
s.age = 1000

#  将一个方法变成函数进行调用
class Screen(object):
    def __init__(self):
        self._width = 10
        self._height = 20

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width*self._height

a = Screen()
print(a.height)

# 多重继承MixIn

# 定制类: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000

# __str__
# __repr__
# __iter__
# __getitem__
# __getattr__
# __call__

# 元类

# type 创建动态类
def hello(self):
    print('hello word')
Hello = type('Hello', (object,), dict(print_hello=hello)) # 创建Hello类

a = Hello()
a.print_hello()

# metaclass 创建元类

