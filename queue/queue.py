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

    