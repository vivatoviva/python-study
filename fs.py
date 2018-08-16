# 读取文件
from io import StringIO
from io import BytesIO
import pickle
import json


fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.readlines()
    print(s)


# StringIO和BytesIO
f = StringIO()
f.write('前端工程师')
f.write(' genluo')
print(f.getvalue())

b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

# os模板 调用系统接口的模块

# 序列化和反序列化
d = dict(name='Bob', age=20, score=88)

with open('test.txt', 'wb') as f:
    pickle.dump(d, f)
b = None
with open('test.txt', 'rb') as f:
    b = pickle.load(f)
print(b)


# json
# dumps参数： https://docs.python.org/3/library/json.html#json.dumps
print(type(json.dumps(d)))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

