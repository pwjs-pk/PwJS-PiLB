from threading import Lock


class Chopstick:

    def __init__(self):
        self.lock = Lock()

    def acquire(self):
        self.lock.acquire()

    def release(self):
        self.lock.release()
