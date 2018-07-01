"""
主进程执行完毕后就结束, 不会等待子进程, 子进程会继续执行到程序完毕,
如果要让父进程等待, 则要在进程start后, 加入join()
"""
from multiprocessing import Process
import time


def run_proc():

    print('process 2: start')

    for i in range(5):
        print('process 2: -----%d-----' % i)
        time.sleep(1)

    print('process 2: end')


if __name__ == '__main__':
    print('process 1: start')

    p = Process(target=run_proc)

    p.start()
    p.join()

    time.sleep(1)
    print('process 1: end')
