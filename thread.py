# 线程相关知识

import time, threading, multiprocessing


# 常见线程并且运行
def loop():
    print('当前运行的进程名称是： ',threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        time.sleep(1)
    print(threading.current_thread().name, '运行结束')

print('threading %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop, name='Loop thread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

# Lock加锁

lock = threading.Lock()
def loop():
    x = 0
    lock.acquire()
    try:
        while True:
            x = x ^ 1
    finally:
        lock.release()

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。


# ThreadLocal 解决函数一层一层传递参数的问题，每个线程访问的都不一样

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 分布式进程
