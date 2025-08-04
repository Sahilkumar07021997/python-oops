class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# for example we want to create a
# binary tree with the following structure:
#                                        4
#                                      /   \
#                                     2     6
#                                    / \   / \
#                                   1   3 5   None


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)

print(f"------------Binary tree created with root node {root.value} ---------")


# IN-Order Traversal (LEFT, ROOT, RIGHT). -> [1, 2, 3, 4, 5, 6]
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)  # Traverse the left subtree first
        print(node.value, end=' ')  # Visit the root
        in_order_traversal(node.right)  # Finally traverse the right subtree


# example usage
in_order_traversal(root)
print("\n------------In-order traversal completed.---------")


# PRE-Order Traversal (ROOT, LEFT, RIGHT). -> [4, 2, 1, 3, 6, 5]
def pre_order_traversal(node):
    if node is not None:
        print(node.value, end=' ')  # Visit the root first
        pre_order_traversal(node.left)  # Then traverse the left subtree
        pre_order_traversal(node.right)  # Finally traverse the right subtree


# example usage
pre_order_traversal(root)
print("\n------------Pre-order traversal completed.---------")


# POST-Order Traversal (LEFT, RIGHT, ROOT). -> [1, 3, 2, 5, 6, 4]
def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)  # Traverse the left subtree first
        post_order_traversal(node.right)  # Then traverse the right subtree
        print(node.value, end=' ')  # Finally visit the root


# example usage
post_order_traversal(root)
print("\n------------Post-order traversal completed.---------")
