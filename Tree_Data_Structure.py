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
# A new node is generated and assigned the data specified in the parameters. In the event that the tree happens to be empty (root is None), the newly created node becomes the root of the tree. Otherwise, the tree is traversed recursively in search of a position for the new node. The new node is added as a child of the suitable parent node (either to the left or right depending on data comparison)      

# search(data):

# Begins at the core node (the present one). Progressively moves down the structural hierarchy thereby validating the data with that of the present node. In the event that the data is equivalent to the one stored in the node, returns the data filled node. If no similar data is found after all branches have been traversed, it returns None instead.

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

# Recursive approach that visits the left subtree first, then the right subtree, and then the node itself