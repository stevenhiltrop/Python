class BufferFullException(Exception):
    def __init__(self):
        raise BufferError("Buffer is full.")


class BufferEmptyException(Exception):
    def __init__(self):
        raise BufferError("Buffer is empty.")


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = list()
        self.capacity = capacity

    def read(self):
        try:
            return self.buffer.pop(0)
        except BufferEmptyException:
            return BufferEmptyException()

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException()

    def overwrite(self, data):
        self.buffer.pop(0)
        self.buffer.append(data)

    def clear(self):
        self.buffer.clear()
