class PlatedStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Return the front item of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("peek from empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)
