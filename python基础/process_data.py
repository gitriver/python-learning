#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
一个简单的demon   生产者与消费者

"""
import time
import queue

import threading
import random

# 哨兵
_sentinel = object()

class Producer(threading.Thread):
    """
    只负责产生数据
    """

    def __init__(self, name, queue):
        # python3的写法
        super().__init__(name=name)
        self.queue = queue
        print("producer启动，开始处理文件")

    def run(self):
        for i in range(15):
            print("%s is producing %d to the queue!" % (self.getName(), i))
            self.queue.put(i)
            time.sleep(random.randint(1, 10) * 0.001)

        # 设置完成的标志位
        self.queue.put(_sentinel)
        print("%s finished!" % self.getName())


class Consumer(threading.Thread):
    """
    数据处理,对数据进行消费.
    """

    def __init__(self, name, queue):
        super().__init__(name=name)
        self.queue = queue

    def processFile(self,fileName):
        #添加处理压缩文件的逻辑
        print("{} is consuming. {} in the queue is consumed!".format(self.getName(), fileName))
        pass
    
    def run(self):
        while True:
            value = self.queue.get()
            # 用来退出线程
            if value is _sentinel:
                # 添加哨兵,让其他线程有机会退出来
                self.queue.put(value)
                break
            else:
                self.processFile(value)

        print("%s finished!" % self.getName())


if __name__ == '__main__':
    queue = queue.Queue()
    producer = Producer('producer', queue)

    consumer_threads = []
    #根据需要启动多个线程处理
    for i in range(5):
        consumer = Consumer('consumer_' + str(i), queue)
        print("消费线程"+str(i)+"启动")
        consumer_threads.append(consumer)
        consumer.start()

    producer.start()
    for consumer in consumer_threads:
        consumer.join()
    producer.join()

    print('All threads  done')

