class DoubleNode:
    """
    Node belonging to a Doubly LinkedList. Contains its own value and a reference
    to the next node in the LinkedList.
    """
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


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
            curr_node = curr_node.next
        if node_strings == "NULL":
            return node_strings
        return f"{node_strings} <-> NULL"

    def insert(self, value):
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
            old_head.prev = new_node

    def includes(self, value):
        curr_node = self.head
        while curr_node:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False


class TargetError:
    pass
