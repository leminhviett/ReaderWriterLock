from threading import Thread, currentThread
from time import sleep
from random import random

from reader_writer_lock import MultithreadingFactory


def test(option):
    test_name = ["No priority", "Read priority", "Write priority"]

    print(f"Testing option [{test_name[option]}]")

    rw = MultithreadingFactory(option)
    r_lock = rw.get_read_lock()
    w_lock = rw.get_write_lock()

    val = 0

    def read_val():
        nonlocal val
        with r_lock:
            sleep(random())
            print(f"Reading from {currentThread().getName()}, val = {val}")

    def write_val():
        nonlocal val
        with w_lock:
            sleep(random())
            val += 1
            print(f"Writing from {currentThread().getName()}, val = {val}")

    r = []
    w = []
    for i in range(10):
        t_r = Thread(target=read_val, name=f"read_{i}")
        t_w = Thread(target=write_val, name=f"write_{i}")

        w.append(t_w)
        r.append(t_r)

        if option == 1:
            # start write first, but then the read thread will be prioritized
            t_w.start()
            t_r.start()
        elif option == 2:
            # start read first, but then the write thread will be prioritized
            t_r.start()
            t_w.start()
        else:
            # random case
            t_w.start()
            t_r.start()

    for ele in r:
        ele.join()

    for ele in w:
        ele.join()

    assert val == 10
    print("===============================")


test(0)

test(1)
test(2)
