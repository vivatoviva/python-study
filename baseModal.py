# python 基本模块

from datetime import datetime


# 时间戳

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime

print('当前时间戳', dt.timestamp())

a = datetime(2015, 4, 19, 12, 20).timestamp();

print('转化为时间戳', datetime.fromtimestamp(a))

# str转化为datetime

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

# datetime转换为str
now = datetime.now()
now.strftime('%a, %b %d %H:%M')