from reader_writer_lock.ReadLock import ReadLock
from reader_writer_lock.WriteLock import WriteLock
from reader_writer_lock.Base import BaseInteger
from multiprocessing import RLock, Condition, Value


class Integer(BaseInteger):
    def __init__(self, init):
        super(Integer, self).__init__()
        self._value = Value('i', init)

    def value(self):
        return self._value.value

    def incre(self):
        self._value.value += 1

    def decre(self):
        self._value.value -= 1


class FactoryLock:
    '''
    options:
        0: normal
        1: read priority
        2: write priority
    '''

    def __init__(self, options):
        if options > 2 or options < 0:
            raise Exception("Options must be in [0, 1, 2]")

        self.global_lock = RLock()
        self.active_read = Integer(0)
        self.active_write = Integer(0)
        self.waiting_read = Integer(0)
        self.waiting_write = Integer(0)
        self.cv_read = Condition(self.global_lock)
        self.cv_write = Condition(self.global_lock)

        self.read_lock = ReadLock(self.global_lock, self.cv_read, self.cv_write, self.active_read, self.active_write,
                                  self.waiting_read, self.waiting_write, options)
        self.write_lock = WriteLock(self.global_lock, self.cv_read, self.cv_write, self.active_read, self.active_write,
                                    self.waiting_read, self.waiting_write, options)

    def get_read_lock(self):
        return self.read_lock

    def get_write_lock(self):
        return self.write_lock
