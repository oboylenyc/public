""" Reverse a Singly Linked List

Difficulty: Intermediate

Challenge Description: Build a simple singly linked list using a Node class (with fields value and next). Implement a function reverse_list(head) that reverses the list in-place and returns the new head. Do not create new nodes or use extra data structures. Aim for O(n) time and O(1) extra space. Include a small helper to print the list for checking.

Input Example
Create a list: 1 -> 2 -> 3 -> None
Call: new_head = reverse_list(head)
Print the list starting from new_head.

Expected Output
3 -> 2 -> 1 -> None

Bonus (optional): Also implement a recursive version reverse_list_recursive(head) and confirm it produces the same result. """

# Define a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Helper to print a linked list
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Iterative reversal
def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next   # store next node
        current.next = prev  # reverse link
        prev = current       # move prev forward
        current = nxt        # move current forward
    return prev

# Recursive reversal
def reverse_list_recursive(head, prev=None):
    if not head:
        return prev
    nxt = head.next
    head.next = prev
    return reverse_list_recursive(nxt, head)

# ---- Example usage ----
# Build linked list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original list:")
print_list(head)

# Iterative reversal
new_head_iter = reverse_list(head)
print("Reversed list (iterative):")
print_list(new_head_iter)

# Reverse back using recursive version
restored_head = reverse_list_recursive(new_head_iter)
print("Reversed list (recursive):")
print_list(restored_head)