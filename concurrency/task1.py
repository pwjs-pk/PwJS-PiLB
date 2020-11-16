import random
from datetime import datetime
from threading import Lock, Thread


def gen_array(length):
    arr = []
    for i in range(length):
        arr.append(random.gauss(0, 1))
    return arr


class SynchronizedList:

    def __init__(self, length):
        self.list = [0] * length
        self.locks = [Lock()] * length

    def increment(self, n):
        self.locks[n].acquire()
        try:
            self.list[n] += 1
        finally:
            self.locks[n].release()

    def get_elements(self):
        all_released = True
        for i in range(len(self.locks)):
            if self.locks[i].locked():
                all_released = False
                break
        if all_released:
            return self.list
        else:
            raise RuntimeError("Some elements are locked by another threads")


class HistogramJob(Thread):

    def __init__(self, val_array, val_range, bucket_count, bucket_length, init_val, synchronized_list):
        super().__init__()
        self.val_array = val_array
        self.val_range = val_range
        self.bucket_count = bucket_count
        self.bucket_length = bucket_length
        self.list = synchronized_list
        self.init_val = init_val

    def run(self):
        for i in range(self.val_range[0], self.val_range[1]):
            for j in range(1, self.bucket_count + 1):
                if self.val_array[i] < j * self.bucket_length + self.init_val:
                    self.list.increment(j - 1)
                    break

    def get_values(self):
        return self.list


def compute_histogram(val_array, val_range, bucket_count, job_size):
    bucket_length = (val_range[1] - val_range[0]) / bucket_count
    synchronized_list = SynchronizedList(bucket_count)
    array_length = len(val_array)
    thread_count = array_length // job_size

    thread_list = []

    for i in range(thread_count):
        thread = HistogramJob(val_array=val_array, val_range=(i * job_size, (i + 1) * job_size),
                              bucket_count=bucket_count, bucket_length=bucket_length,
                              init_val=val_range[0], synchronized_list=synchronized_list)
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

    bucket_list = []

    for i in range(0, bucket_count + 1):
        bucket_list.append(i * bucket_length + val_range[0])

    return synchronized_list.get_elements(), bucket_list


if __name__ == '__main__':
    val_range = (-4, 4)
    array = gen_array(100_000)

    start = datetime.now()
    histogram, buckets = compute_histogram(val_array=array, val_range=val_range, bucket_count=10000, job_size=1000)
    stop = datetime.now()

    print(stop - start)
    print(histogram)
    print(buckets)
