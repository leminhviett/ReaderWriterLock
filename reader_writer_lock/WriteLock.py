from reader_writer_lock.Base import BaseLock


class WriteLock(BaseLock):
    def __init__(self, lock, cv_read, cv_write, active_read, active_write, waiting_read, waiting_write, options=0):
        super().__init__(lock, cv_write)

        self.cv_write = cv_write
        self.active_read = active_read
        self.active_write = active_write
        self.waiting_read = waiting_read
        self.waiting_write = waiting_write

        self.cv_read = cv_read
        self.waiting_cond = self.construct_waiting_cond(options)

    def construct_waiting_cond(self, options):
        if options == 1:
            return self.prefer_reading_cond

        return self.normal_cond

    def prefer_reading_cond(self):
        return self.active_write.value() > 0 or self.active_read.value() > 0 or self.waiting_read.value() > 0

    def normal_cond(self):
        return self.active_write.value() > 0 or self.active_read.value() > 0

    def acquire(self):
        with self.global_lock:
            self.waiting_write.incre()

            while self.waiting_cond():
                self.cv_write.wait()

            self.waiting_write.decre()
            self.active_write.incre()

    def release(self):
        with self.global_lock:
            self.active_write.decre()
            self.cv_write.notify_all()
            self.cv_read.notify_all()
