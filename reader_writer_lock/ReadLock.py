from reader_writer_lock.Base import BaseLock


class ReadLock(BaseLock):
    def __init__(self, lock, cv_read, cv_write, active_read, active_write, waiting_read, waiting_write, options=0):
        super().__init__(lock, cv_read)

        self.cv_read = cv_read
        self.active_read = active_read
        self.active_write = active_write
        self.waiting_read = waiting_read
        self.waiting_write = waiting_write

        self.cv_write = cv_write
        self.waiting_cond = self.construct_waiting_cond(options)

    def construct_waiting_cond(self, options):
        if options == 2:
            return self.prefer_writing_cond

        return self.normal_cond

    def prefer_writing_cond(self):
        return self.active_write.value() > 0 or self.waiting_write.value() > 0

    def normal_cond(self):
        return self.active_write.value() > 0

    def acquire(self):
        with self.global_lock:
            self.waiting_read.incre()

            while self.waiting_cond():
                self.cv_read.wait()

            self.waiting_read.decre()
            self.active_read.incre()

    def release(self):
        with self.global_lock:
            self.active_read.decre()
            self.cv_write.notify_all()
