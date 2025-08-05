class BinarySearchNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def insert_node(root, value):
    """Insert a value into the binary search tree."""
    if root is None:
        return BinarySearchNode(value)

    if value < root.value:
        if root.left is None:
            root.left = BinarySearchNode(value)
        else:
            insert_node(root.left, value)
    elif value > root.value:
        if root.right is None:
            root.right = BinarySearchNode(value)
        else:
            insert_node(root.right, value)


def pre_order_traversal(node):
    """Perform pre-order traversal of the binary search tree."""
    if node is not None:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


# Example usage of the Binary Search Tree - insert and pre-order traversal
root = BinarySearchNode(4)
insert_node(root, 2)
insert_node(root, 6)
insert_node(root, 1)
insert_node(root, 3)
insert_node(root, 5)

# this is how the binary search tree looks like:
#                                        4
#                                      /   \
#                                     2     6
#                                    / \   / \
#                                   1   3 5   None
print("Binary search tree created with root node:", root.value)
print("Pre-order (ROOT,LEFT, RIGHT) traversal of the binary search tree:")
pre_order_traversal(root)

print("\n------------Pre-order traversal completed.---------")


def search_node(node, value):
    """Search for a value in the binary search tree."""
    print("Searching for value:", value, "in the binary search tree. Current node value: ",
          node.value if node else "None")

    if node is None:  # Base case: if the root is None, the value is not found
        print("Value not found in the binary search tree.")
        return None

    if node.value == value:  # If the current node's value matches the search value.
        print("Value found in the binary search tree.")
        return node

    elif value < node.value:  # If the search value is less than the current node's value, search in the left subtree.
        return search_node(root.left, value)

    # If the search value is greater than the current node's value, search in the right subtree.
    return search_node(node.right, value)


# Example usage of searching for a value in the binary search tree.
search_value = 10
found_node = search_node(root, search_value)
if found_node:
    print(f"Node with value {search_value} found in the binary search tree.")

from typing import Optional


# Binary Search Tree Delete Node Function

# Function to find the minimum value node in a binary search tree.
def minimum_value(node: Optional[BinarySearchNode]) -> Optional[BinarySearchNode]:
    while node.left is not None:
        node = node.left
    return node


def delete_node(node: Optional[BinarySearchNode], key: int) -> Optional[BinarySearchNode]:
    if node is None:
        return node

    if key < node.val:
        node.left = delete_node(node.left, key)
    elif key > node.val:
        node.right = delete_node(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            root = None
            return temp
        elif node.right is None:
            temp = node.left
            root = temp
            return temp

        temp = minimum_value(node.right)
        node.val = temp.val
        node.right = delete_node(node.right, temp.val)

    return node
