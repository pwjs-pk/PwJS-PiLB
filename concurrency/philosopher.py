from random import random
from threading import Thread
from time import sleep


class Philosopher(Thread):

    def __init__(self, id):
        super().__init__()
        self.left = None
        self.right = None
        self.id = id

    def run(self):
        while True:
            time = random()
            sleep(time)
            self.left.acquire()
            sleep(time)
            print(f"Philosopher no {self.id} acquired left chopstick")
            self.right.acquire()
            print(f"Philosopher no {self.id} acquired right chopstick")
            sleep(time)
            self.left.release()
            sleep(time)
            print(f"Philosopher no {self.id} released left chopstick")
            self.right.release()
            print(f"Philosopher no {self.id} released right chopstick")