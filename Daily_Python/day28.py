""" Title
Implement a Singly Linked List

Difficulty: Intermediate

Challenge Description:
Create a Python class Node to represent a node in a singly linked list, and a LinkedList class to manage the list. Implement the following methods:

append(value): Add a node with the given value at the end of the list.

prepend(value): Add a node with the given value at the beginning of the list.

print_list(): Print all the values in the list in order.

Constraints:

Do not use Python’s built-in list methods for storage; use linked nodes. """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:  # empty list
            self.head = new_node
            return
        current = self.head
        while current.next:  # move to last node
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return  # empty list, nothing to delete

        # If head node needs to be deleted
        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:  # found the node
            current.next = current.next.next

    def print_list(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))


# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.print_list()  # 5 -> 10 -> 20

ll.delete(10)
ll.print_list()  # 5 -> 20
