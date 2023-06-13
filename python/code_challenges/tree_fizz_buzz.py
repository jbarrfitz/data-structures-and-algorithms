import copy
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def fizz_buzz_tree(tree):
    fb_tree = copy.deepcopy(tree)
    modify_queue = Queue()
    modify_queue.enqueue(fb_tree.root)

    def _fizz_buzz(root):
        modified_value = ""
        if root.value % 3 != 0 and root.value % 5 != 0:
            modified_value = str(root.value)
        if not root.value % 3 == 0:
            modified_value += "Fizz"
        if root.value % 5 == 0:
            modified_value += "Buzz"
        root.value = modified_value

        for child in root.children:
            _fizz_buzz(child)
