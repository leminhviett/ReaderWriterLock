from multiprocessing import current_process, Value, Process
from time import sleep
from random import random

from reader_writer_lock import MultiprocessingFactory
from reader_writer_lock.MpFactory import Integer


def test(option):
    test_name = ["No priority", "Read priority", "Write priority"]

    print(f"Testing option [{test_name[option]}]")

    rw = MultiprocessingFactory(option)
    r_lock = rw.get_read_lock()
    w_lock = rw.get_write_lock()

    val = Integer(0)

    def read_val():
        nonlocal val
        with r_lock:
            sleep(random())
            print(f"Reading from {current_process().name}, val = {val.value()}")

    def write_val():
        nonlocal val
        with w_lock:
            sleep(random())
            val.incre()
            print(f"Writing from {current_process().name}, val = {val.value()}")

    r = []
    w = []
    for i in range(10):
        t_r = Process(target=read_val, name=f"read_{i}")
        t_w = Process(target=write_val, name=f"write_{i}")

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

    assert val.value() == 10
    print("===============================")


test(0)
test(1)
test(2)
