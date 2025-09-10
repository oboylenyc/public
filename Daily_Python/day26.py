""" Title: Stack Implementation with Lists

Difficulty: Intermediate

Challenge Description:
Implement a simple Stack class in Python using a list internally. A stack follows the LIFO (Last In, First Out) principle. Your class should support these methods:

push(item): add an item to the top of the stack

pop(): remove and return the top item of the stack (if empty, return None)

peek(): return the top item without removing it (if empty, return None)

is_empty(): return True if the stack is empty, otherwise False

size(): return the number of items in the stack """

class Stack:
    def __init__(self):
        # internal list to store items
        self.items = []

    def push(self, item):
        # add item to top
        self.items.append(item)

    def pop(self):
        # remove and return top if not empty
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        # return top without removing
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        # check if empty
        return len(self.items) == 0

    def size(self):
        # return size of stack
        return len(self.items)

    def __str__(self):
        # bonus: print stack nicely
        return "Stack: " + str(self.items)
        

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.pop())       # 30
    print(s.peek())      # 20
    print(s.size())      # 2
    print(s.is_empty())  # False
    print(s)             # Stack: [10, 20]