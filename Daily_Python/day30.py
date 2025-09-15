""" Binary Tree Traversal (Inorder, Preorder, Postorder)

Difficulty: Intermediate

Challenge Description:
Implement a simple binary tree class in Python and write three traversal methods:

Inorder Traversal (Left → Root → Right)

Preorder Traversal (Root → Left → Right)

Postorder Traversal (Left → Right → Root)

Your task is to build a binary tree with at least 5 nodes and demonstrate all three traversals by printing the order of visited nodes.

Input Example
(You don’t need to take user input; just hardcode a small tree for testing.)

Expected Output
Inorder: [values in inorder sequence]
Preorder: [values in preorder sequence]
Postorder: [values in postorder sequence]

Bonus:
Add a method to calculate the height of the tree. """

# Day 30 – Binary Tree Traversal (with Bonus: Height)
# Python 3.10+

from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

def inorder(root: Optional[Node]) -> List[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root: Optional[Node]) -> List[int]:
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root: Optional[Node]) -> List[int]:
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def height(root: Optional[Node]) -> int:
    """
    Height defined as number of levels (empty tree = 0, single node = 1).
    """
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# ---- Build a sample tree with at least 5 nodes ----
#       4
#      / \
#     2   6
#    / \   \
#   1   3   7
root = Node(4,
            left=Node(2, Node(1), Node(3)),
            right=Node(6, None, Node(7)))

# ---- Demonstrate traversals ----
print("Inorder:", inorder(root))     # Left → Root → Right
print("Preorder:", preorder(root))   # Root → Left → Right
print("Postorder:", postorder(root)) # Left → Right → Root

# ---- Bonus: Height ----
print("Height:", height(root))
