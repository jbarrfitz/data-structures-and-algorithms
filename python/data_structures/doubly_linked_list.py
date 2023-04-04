class DoubleNode:
    """
    Node belonging to a Doubly LinkedList. Contains its own value and a reference
    to the next node in the LinkedList.
    """
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    """
    Structure containing nodes. This class contains only a reference to the
    head (first) node.
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __str__(self):
        curr_node = self.head
        node_strings = "NULL"
        while curr_node:
            node_strings = f"{node_strings} <-> {{ {curr_node.value} }}"
            curr_node = curr_node.next_node
        if node_strings == "NULL":
            return node_strings
        return f"{node_strings} <-> NULL"

    def insert(self, value):
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next_node = old_head
            old_head.prev_node = new_node

    def includes(self, value):
        curr_node = self.head
        while curr_node:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next_node
        return False


class TargetError:
    pass
