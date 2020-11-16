from philosopher import Philosopher
from chopstick import Chopstick


class Table:

    @staticmethod
    def __init_philosophers(size):
        philosophers = []
        chopstick = Chopstick()
        first_chopstick = chopstick
        for i in range(0, size):
            philosopher = Philosopher(i + 1)
            philosopher.left = chopstick
            chopstick = Chopstick()
            philosopher.right = chopstick
            philosophers.append(philosopher)

        philosophers[-1].right = first_chopstick

        return philosophers

    def __init__(self, size):
        self.philosophers = self.__init_philosophers(size)

    def run(self):
        for philosopher in self.philosophers:
            philosopher.start()


if __name__ == '__main__':
    table = Table(5)
    table.run()
