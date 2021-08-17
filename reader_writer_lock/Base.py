class BaseLock:
    def __init__(self, lock, condition_variable):
        self.global_lock = lock
        self.cv = condition_variable

    def acquire(self):
        pass

    def release(self):
        pass

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self.release()


class BaseInteger:
    def __init__(self):
        pass

    def incre(self):
        pass

    def decre(self):
        pass

    def value(self):
        pass
