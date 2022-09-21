import queue
import threading
import itertools
from time import sleep

# multi threading

q = queue.Queue()


def worker():
    print("worker started")
    while True:
        item = q.get(block=True)
        print("doing some work")

        # sleep for 2 sec
        sleep(2)

        q.task_done()

# start one thread to add items to the queue


def add_task():
    print("add_task started")
    for c in itertools.product(range(1, 256), repeat=4):
        # print(c)
        # str to bytes inverse
        # c_bytes = bytes(''.join(c), 'utf-8')
        # c_bytes = ''.join(c).encode('utf-8')
        c_bytes = bytes(c)
        # inverse bytes
        c_bytes = c_bytes[::-1]
        # print(c_bytes)
        q.put(c_bytes)


# start one thread to add items to the queue
t = threading.Thread(target=add_task)
t.daemon = True
t.start()


print("starting worker threads")
for i in range(8):
    print("starting thread: ", i)
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# block until all tasks are done
q.join()
