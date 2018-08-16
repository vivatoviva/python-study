# 正则表但是
import re

#  python字符串本身也是使用 \ 进行转意
# 所以最好是是使用r前缀

# re.match 成功返回Match，失败返回None

print(re.match(r'^\d{3}\-\d{3,8}', '010-123456'))

# 切分字符串 
re.split(r'\s*', 'a,   b, c')


# 高级功能进行分组

# 贪婪匹配
