class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
print(f"empty? {stack.is_empty()}")

stack.push(1)
print(f"empty after push? {stack.is_empty()}")

stack.pop()
print(f"empty after pop? {stack.is_empty()}")

for i in range(0, 6):
    stack.push(i)
print(f"peek? {stack.peek()}")
print(f"size? {stack.size()}")
