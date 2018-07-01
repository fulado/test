from multiprocessing import Process
import time


def run_proc():
    """
    子进程代码
    :return:
    """
    while True:
        print("----2----")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()

    while True:
        print('----1----')
        time.sleep(1)
