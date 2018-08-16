# 错误和调试
import logging

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    logging.error('')
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy


def foo():
    raise ValueError('hahahah')


def bar():
    try:
        foo()
    except ValueError as e:
        logging.exception(e)
        raise


# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：


from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

# 断言

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
# 如果断言失败，将会抛出一个错误

# 测试这边没接触
