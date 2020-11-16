import csv
import os


class Task:
    def __init__(self, id, name, priority):
        self.id = id
        self.name = name
        self.priority = priority

    def __iter__(self):
        self.iter = 0
        self.list = [self.id, self.name, self.priority]
        return self

    def __next__(self):
        curr = self.iter
        if curr < len(self.list):
            self.iter += 1
            return self.list[curr]
        else:
            raise StopIteration

    def __len__(self):
        return 3


def menu():
    print('1. Add data')
    print('2. Delete row')
    print('3. Show data')
    print('4. Save data')
    print('0. Exit')
    return input('> ')


def print_tasks(tasks):
    column_width = max(len(word) for row in tasks for word in row) + 4
    print('-' * len(tasks[0]) * column_width)
    for row in tasks:
        print("|".join(word.ljust(column_width) for word in row))
    print('-' * len(tasks[0]) * column_width)


def load_csv(filename):
    tasks = []
    with open(filename) as csvfile:
        for row in csv.DictReader(csvfile):
            tasks.append(Task(row['id'], row['name'], row['priority']))
    return tasks


def delete_row(tasks, n):
    length = len(tasks) - 1
    i = None
    for i in range(0, length):
        if tasks[i].id == n:
            del tasks[i]
            break
    for j in range(i, length):
        tasks[j].id = str(int(tasks[j].id) - 1)


def add_task(tasks, name, priority):
    next_id = int(tasks[len(tasks) - 1].id) + 1
    tasks.append(Task(str(next_id), name, priority))


def save_data(filename, tasks):
    with open(filename, 'w') as csvfile:
        fieldnames = ['id', 'name', 'priority']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({'id': task.id, 'name': task.name, 'priority': task.priority})


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 'samples/tasks.csv')
    tasks = load_csv(file)
    print_tasks(tasks)
    result = None
    is_last_command_save = True
    while result != 'exit':
        result = menu()
        if result == '1':
            name, priority = input('name, priority: ').split(',')
            priority = priority.strip()
            add_task(tasks, name, priority)
            is_last_command_save = False
        elif result == '2':
            n = input('Which task you wanna delete?: ')
            delete_row(tasks, n)
            is_last_command_save = False
        elif result == '3':
            print_tasks(tasks)
        elif result == '4':
            save_data(file, tasks)
            is_last_command_save = True
        elif result == '0':
            if not is_last_command_save:
                choice = input('Are you want to exit without saving? [y/n]: ')
                if choice == 'y':
                    result = 'exit'
            else:
                result = 'exit'
