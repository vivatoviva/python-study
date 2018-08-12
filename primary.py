# 切片

list = ['李根', '王晓奔', '李家豪', '李泽阳']
print('从第一个取，取1-2', list[1:2])
print('每两个取一个', list[::2])
print('复制一个list', list[:])
# 字符串也可以看成是一种list

def trim(str):
  if str[0] == ' ':
    return trim(str[1:])
  elif str[-1] == ' ':
    return trim(str[:-1])
  else:
    return str
print(trim('  sh begin    '))

# 遍历
dist = {
  'a': 1,
  'b': 2,
  'c': 3
}
# 遍历key值
for key in dist:
  print(key)
# 遍历值
for value in dist.values():
  print(value)
# 遍历键值、对象
for key,value in dist.items():
  print(key, value)
# 实现下标进行遍历
for i, value in enumerate(['A', 'B', 'C']):
  print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
  print(x, y)

# 联系
def list_min(list):
  if len(list) == 0:
    return None, None
  min = list[0]
  max = list[0]
  for value in list:
    if value > max:
      max = value
    if value < min:
      min = value
  return min, max

print('最大最小函数', list_min([1,2,3,4,56,7,1,2,3]))

# 列表生成器

print([x * x for x in range(1, 100) if x % 2 == 0 ])
print([m + n for m in 'ABC' for n in 'XYZ'])



# 生成器 generator

a = (x * x in range(1,10))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 生成杨辉三角

def triangles(n):
    last = [1]
    now = [1]
    i = 2
    while n >= i:
        yield last
        j = i-2
        while j > 1:
            now.append(last[j-1] + last[j-2])
            j = j - 1
        last = now
        now = []
        i = i + 1
    return None

g = triangles(100)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
    break

