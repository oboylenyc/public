""" Level-Order (BFS) Traversal of a Binary Tree

Difficulty: Intermediate

Challenge Description: Implement a function level_order(root) that returns a list of node values visited in breadth-first (level-order) order, from top to bottom and left to right. Assume a simple binary tree node class with attributes val, left, right. Use an explicit queue (e.g., collections.deque). Do not use recursion. If root is None, return an empty list.

Input Example
Tree structure:
1
/
2 3
/ \
4 5 7

Expected Output
[1, 2, 3, 4, 5, 7]

Bonus (optional): Write level_order_by_level(root) that returns a list of lists grouped by depth, e.g., [[1], [2, 3], [4, 5, 7]]. """
from collections import deque

# Definition of a simple binary tree node

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """Return nodes in simple level-order traversal (BFS)."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def level_order_by_level(root):
    """Return nodes grouped by levels in BFS traversal."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result


# Example usage
if __name__ == "__main__":
    # Build the example tree:
    #         1
    #       /   \
    #      2     3
    #     / \     \
    #    4   5     7
    root = Node(1,
                Node(2, Node(4), Node(5)),
                Node(3, None, Node(7)))

    print("Level Order:", level_order(root))
    print("Level Order by Levels:", level_order_by_level(root))
