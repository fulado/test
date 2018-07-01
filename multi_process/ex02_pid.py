from multiprocessing import Process
import os


def run_proc():
    print('子进程运行中, pid: %d' % os.getpid())
    print('子进程将要结束...')


if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())
    p = Process(target=run_proc)
    p.start()
