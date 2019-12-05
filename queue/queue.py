class Empty(Exception):
    """Error attempting to access an item from an empty storage"""
    pass


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    _CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._storage = [None] * self._CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")

        return self._storage[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")

        ret = self._storage[self._front]
        self._storage[self._front] = None
        self._front = (self._front + 1) % len(self._storage)
        self._size -= 1

        return ret
