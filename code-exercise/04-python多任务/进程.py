# -*- coding:utf-8 -*-

"""
Name: 进程.py
Author: fengdi
Datetime: 16:28 2019-07-16
Description:

"""
import time
import multiprocessing

# 进程：多进程实现多任务，使用multiprocessing.Process()类实现。主要用于cpu密集型任务。


def print_name(name):
    for x in range(10):
        print('my name is %s.' % name)
        time.sleep(0.5)


def print_age(age):
    for x in range(5):
        print('I am %d years old.' % age)
        time.sleep(0.2)


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=print_name, args=('枫頔',))
    process2 = multiprocessing.Process(target=print_age, kwargs={'age':24})
    print('主进程启动：')
    process1.start()
    process2.start()
    time.sleep(1)
    print('主进程结束。')

# 进程独立：进程之间相互独立，不共享全局变量数据。

num = []


def add_func():
    for x in range(3):
        num.append(x)
        time.sleep(0.1)
    print("进程1:%s" % num)


def get_func():
    print("进程2：%s" % str(num))


if __name__ == "__main__":
    add_process = multiprocessing.Process(target=add_func)
    get_process = multiprocessing.Process(target=get_func)
    add_process.start()
    add_process.join()
    get_process.start()

# 进程间通信：消息队列（queue，先进先出）使用put()添加数据，get()方法取出数据

queue = multiprocessing.Queue(3)

queue.put('hello world!')
queue.put('bye bye！')
queue.put(25)

for x in range(3):
    result = queue.get()
    print(result)


def add_num(queue):
    for x in range(3):
        print('%d' % x)
        queue.put(x)
        time.sleep(0.5)


def get_num(queue):
    while True:
        if queue.empty():
            break
        value = queue.get()
        print(value)


if __name__ == '__main__':
    queue = multiprocessing.Queue(3)
    sub_process1 = multiprocessing.Process(target=add_num, args=(queue,))
    sub_process2 = multiprocessing.Process(target=get_num, args=(queue,))
    sub_process1.start()
    sub_process1.join()
    sub_process2.start()

# 进程池：可使用进程池方式，批量创建多个进程。
# 定义进程需要执行的任务


def worker(msg):
    start_time = time.time()
    print("任务%s开始执行，进程号：%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    stop_time = time.time()
    print("任务%s执行完毕， 耗时%0.2fs" % (msg, stop_time - start_time))


po = multiprocessing.Pool(3)  # 定义一个进程池，最大进程数为3

# 定义需要执行的任务数
for i in range(10):
    po.apply_async(worker, (i,))  # 表示任务异步执行

print("------start------")
po.close()   # 进程池关闭
po.join()    # 进程池中所有进程执行完成
print("-------end-------")


# 进程池间进程通信

def write(q):
    for x in 'hello':
        q.put(x)


def read(q):

    info = list()

    while True:
        data = q.get()
        info.append(data)

        if q.empty():
            break

    print(info)


if __name__ == '__main__':

    # 创建队列用于通信
    queue = multiprocessing.Manager().Queue(20)

    # 创建进程池
    pool = multiprocessing.Pool()

    # 进程池执行write任务向队列写入数据
    pool.apply_async(write, args=(queue, ))

    # 主进程休眠，等待队列写入消息
    time.sleep(1)

    # 进程池执行read任务从队列中读出数据
    pool.apply_async(read, args=(queue,))

    print("主进程%d开始执行" % os.getpid())

    # 关闭进程池
    pool.close()

    # 主进程阻塞，等待子进程执行完成
    pool.join()

    print("主进程%d结束执行" % os.getpid())
