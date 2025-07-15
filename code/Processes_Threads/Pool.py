from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 创建一个进程池，最多同时跑4个进程
    p = Pool(4)
    # 用apply_async 提交异步任务
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    # 一旦提交完所有任务，不再接收新任务
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
