from multiprocessing import Queue


def main():
    q = Queue(3)
    q.put('msg: 1')
    q.put('msg: 2')
    print(q.full())
    q.put('msg: 3')
    print(q.full())
    q.put('msg: 4', True, 2)

    print('end')


if __name__ == '__main__':
    main()
