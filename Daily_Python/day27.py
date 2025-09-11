""" Implement a Queue with Lists

Difficulty: Intermediate

Challenge Description:
A queue is a data structure that follows the First In, First Out (FIFO) principle. Your task is to implement a simple Queue class in Python using lists. The class should support the following methods:

enqueue(item) → adds an item to the end of the queue

dequeue() → removes and returns the item at the front of the queue (or raises an error if the queue is empty)

peek() → returns the item at the front of the queue without removing it

is_empty() → returns True if the queue is empty, otherwise False

size() → returns the number of items in the queue """

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from the front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the queue"""
        return str(self.items)


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    print(q.dequeue())   # A
    print(q.peek())      # B
    print(q.size())      # 2
    print(q.is_empty())  # False
    print(q)             # ['B', 'C']