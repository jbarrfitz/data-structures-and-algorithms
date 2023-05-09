from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    def add(self, value):
        self.root = self._add(self.root, value)

    def _add(self, root, value):
        if not root:
            return Node(value)
        if value < root.value:
            root.left = self._add(root.left, value)
        elif value > root.value:
            root.right = self._add(root.right, value)
        return root

    def contains(self, value):
        curr_node = self.root
        while curr_node:
            if curr_node.value == value:
                return True
            if curr_node.value < value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return False

