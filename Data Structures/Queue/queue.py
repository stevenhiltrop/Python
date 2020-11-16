class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


a_queue = Queue()
print(f"empty? {a_queue.is_empty()}")

for i in range(5):
    a_queue.enqueue(i)
print(f"size? {a_queue.size()}")

for i in range(5):
    a_queue.dequeue()
print(f"size now? {a_queue.size()}")
