# 胶水语言python学习

# # 输出语句
# print('Hello', 'World', 'please input you name')
# # 输入语句
# name = input()

# print('you name is', name)

# # 多行输入
# print('''
# 表示多行进行输入
# ''')

# # 三种运算符 and、 or、not
# print(True and True)
# print(1 or False)
# print(not 1)

# # 空值
# None

# # 字符串表示,前面添加r为原始字符串, b为bytes，默认为ascii编码
# a = 'ABC'
# b = a
# a = 'a'


# # 两种除法
# # / 返回的数据一定是浮点类型
# # // 返回的数据一定是整数

# # 取余
# # % 两数相除所得余数，永远都是整数

# # 编码
# # 在最新的python 3版本中字符串采用 Unicode 进行编码
# # 数据在网络上进行传输时候，通常为bytes，经常使用encode()、decode() 方法

# # 格式化
# print('Hello world %d + %d = %d' %(1, 2, 3))
# print('Hello %d, %%' % 10)
# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# # 条件判断

# a = int(input('请输入一个整数'))

# if a > 100:
#     print('大于')
# else:
#     print('小于')

# # 循环

# for int in list(range(a)):
#     print(int)

# while int > 10:
#     print('init')
#     int = int -1

# # list 和 tuple

# list = [1,2,3]
# list.append(5)
# list.insert(1, 'content')
# list.pop()
# list.pop(len(list)-1)

# tuple = (1,2,3)


# # dict 和 set

# # 键必须为不可变对象
# dist = {
#     'key1': 1,
#     'key2': 2
# }
# dist.get('key1')
# dist.pop('key1')

# a = set([1,2,3])
# a.add(1)
# a.remove(1)

# b = set([3,4,5])

# a & b # 求并集
# a | b # 求交集

# # 联系list、tuple、set、dist
# tuple = (1,2,3)
# dist = {tuple: '1'}
# print(dist.get(tuple))

# # 调用内置函数的帮助，例如 hex

# help(hex)


# python 函数部分

def hexo(x = 10):
    if x > 0:
        print('大于0')
    else:
        print('小于0')

# 空函数
def null():
    pass

def return_tuple():
    return 1,2,3
(d,e,f) = return_tuple()

print('d = %d, e = %e, f = %f' % (d, e, f))

# 当函数在定义的时候，默认参数就会被计算出来，每次调用函如果改变函数的默认指向的值，则将会改变后续赋值

# 可变长度参数

def multiple_param(*params):
    for param in params:
        print(param)
    return None;

multiple_param('J', 'Q', 'K')
multiple_param(*['J', 'Q', 'K'])

# 关键字参数

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'kw', kw)
person('李根', '20', school='重庆邮电大学')
person('李根', '20', **{
    'school': '重庆邮电大学',
    'grade': '2016'
})

# 限制关键字参数传值

def person(name, age, *, school='北京大学', grade='2014'):
    print(name,age,school,grade)
person('李根', 20, school='重庆邮电大学')

# 参数组合

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def product(*params):
    sum = 1
    for value in params:
        sum = sum * value
    print('sum:', sum)
 # 计算一个或者多个数的乘积
product(*[1])


