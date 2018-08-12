import functools
import time
import functools

# 函数式编程
from functools import reduce



# map函数
def bainji(id):
    print(id)
    return id *5
a = map(bainji, [1,2,3])
print(list(a))

# reduce函数
def reduceFun(id1, id2):
    return id1 + id2
print(reduce(reduceFun, [1,2,3]))

def filterFun(id):
    return id % 2 == 1
print(list(filter(filterFun, [1,2,3,4,5,6])))

# sorted函数
sorted([36,-12,25,85,-22], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def getName(t):
    return t[1]
print(list(sorted(L, key=getName)))

# 闭包函数

def counter():
    k = 0
    def sum():
        nonlocal k
        k =  k+1
        return k
    return sum

f = counter()
print(f(),f(),f(),f())

# python 作用域恶补一波

# 匿名函数
# list(map(lambda x: x*x, [1,2,3,46,5])
# list(filter(lambda n : n % 2 == 1, range(1, 20)))


# 装饰器用法
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('ligen')
def now():
    print('2015-3-25')
now()
print(now.__name__)


def log(func):
    # 保证函数签名一致
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def hello():
    print('hello word')

print(hello.__name__)

def metric(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        start = time.time()
        fun(*args, **kw)
        stop = time.time() - start
        print('函数执行时间是 %f' % stop)
    return wrapper
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

fast(10056,45465)
slow(1025,6455,545)


# 偏函数 固定一些参数，思考下科里话
int2 = functools.partial(int, base = 2)

print(int2('1000'))


