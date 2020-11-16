from time import sleep
from random import random
from types import MethodType
from philosopher import Philosopher
from chopstick import Chopstick

class Table:

    @staticmethod
    def __init_philosophers(size):

        def inverted_order(self):
            while True:
                time = random()
                sleep(time)
                self.right.acquire()
                sleep(time)
                print(f"Philosopher no {self.id} acquired right chopstick")
                self.left.acquire()
                print(f"Philosopher no {self.id} acquired left chopstick")
                sleep(time)
                self.right.release()
                sleep(time)
                print(f"Philosopher no {self.id} released right chopstick")
                self.left.release()
                print(f"Philosopher no {self.id} released left chopstick")

        philosophers = []
        chopstick = Chopstick()
        first_chopstick = chopstick
        for i in range(0, size - 1):
            philosopher = Philosopher(i + 1)
            philosopher.left = chopstick
            chopstick = Chopstick()
            philosopher.right = chopstick
            philosophers.append(philosopher)

        philosopher = Philosopher('inverted')
        philosopher.left = chopstick
        philosopher.right = first_chopstick
        philosopher.run = MethodType(inverted_order, philosopher)  # change order in chopstick acquisition

        philosophers.append(philosopher)

        return philosophers

    def __init__(self, size):
        self.philosophers = self.__init_philosophers(size)

    def run(self):
        for philosopher in self.philosophers:
            philosopher.start()


if __name__ == '__main__':
    table = Table(5)
    table.run()
