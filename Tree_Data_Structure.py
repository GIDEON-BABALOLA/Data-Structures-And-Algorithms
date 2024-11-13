# This code implements tree data structures and algorithm, in accordance to the note given in class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None  # Not found

    def preorder_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

#Explanation Of Code
# insert(data):

# Creates a new node with the given data.
# If the tree is empty (root is None), the new node becomes the root.
# Otherwise, traverses the tree recursively to find the appropriate position for the new node.
#  Inserts the new node as a child of the appropriate parent node (left or right based on data comparison).

# search(data):

# Starts from the root node (current).
# Iterates down the tree, comparing data with the current node's data.
# If a match is found, returns the node containing the data.
# If no match is found after traversing all branches, returns None.

# preorder_traversal(node):

# Recursive approach that visits the node first, then its left subtree, and then its right subtree.
# Prints the node's data followed by a space for clarity.
# Calls itself recursively on the left and right subtrees to explore them further.

# inorder_traversal(node):

# Recursive approach that visits the left subtree first, then the node itself, and then the right subtree.
# More common for sorted data structures like Binary Search Trees (BSTs) where nodes are ordered in a specific way.
# Prints the node's data followed by a space for clarity.
# Calls itself recursively on the left and right subtrees to explore them further.

# postorder_traversal(node):

# Recursive approach that visits the left subtree first, then the right subtree, and then the node itself.