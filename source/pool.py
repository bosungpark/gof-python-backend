import queue

class Pool:
    def __init__(self, queue):
        self._queue = queue
        self.item = self._queue.get()

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

# cache data in queue which take some time to create
q = queue.Queue()
q.put([1 for _ in range(100000000)])

with Pool(queue=q) as pool:
    print(pool)