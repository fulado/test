from multiprocessing import Process, Queue
import os, time, random


def write_process(q):
    for value in ['A', 'B', 'C']:
        print('Put %s into queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read_process(q):
    while True:
        try:
            value = q.get(True, 2)
            print('Get %s from queue...' % value)
            time.sleep(random.random())
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    q = Queue()
    p_write = Process(target=write_process, args=(q, ))
    p_read = Process(target=read_process, args=(q, ))

    p_write.start()
    # p_write.join()

    p_read.start()
    # p_read.join()

    print('all data write and read complete.')
