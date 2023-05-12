class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, curr_node, result):
        if curr_node:
            result.append(curr_node.value)
            self._pre_order_recursive(curr_node.left, result)
            self._pre_order_recursive(curr_node.right, result)

    def in_order(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, curr_node, result):
        if curr_node:
            self._in_order_recursive(curr_node.left, result)
            result.append(curr_node.value)
            self._in_order_recursive(curr_node.right, result)

    def post_order(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, curr_node, result):
        if curr_node:
            self._post_order_recursive(curr_node.left, result)
            self._post_order_recursive(curr_node.right, result)
            result.append(curr_node.value)

    def find_maximum_value(self):
        max_val = float('-inf')

        def _traverse(root):
            nonlocal max_val
            if root:
                if root.value > max_val:
                    max_val = root.value
                _traverse(root.left)
                _traverse(root.right)

        _traverse(self.root)

        return max_val


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
