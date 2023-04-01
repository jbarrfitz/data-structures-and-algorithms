class Node:
    """
    Node belonging to a LinkedList. Contains its own value and a reference
    to the next node in the LinkedList.
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    """
    Structure containing nodes. This class contains only a reference to the
    head (first) node.
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        old_head = self.head
        self.head = Node(value, old_head)

    def includes(self, value):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False


class TargetError:
    pass
