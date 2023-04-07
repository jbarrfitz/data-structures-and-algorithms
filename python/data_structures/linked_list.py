class Node:
    """
    Node belonging to a LinkedList. Contains its own value and a reference
    to the next node in the LinkedList.
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Structure containing nodes. This class contains only a reference to the
    head (first) node.
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        curr_node = self.head
        node_strings = ""
        while curr_node:
            node_strings += f"{{ {curr_node.value} }} -> "
            curr_node = curr_node.next
        return f"{node_strings}NULL"

    def append(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head

    def includes(self, value):
        curr_node = self.head
        while curr_node:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next
        return False

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        curr_node = self.head
        inserted = False
        if not curr_node:
            raise TargetError(f"No nodes in linked list to insert before")
        if curr_node.value == value:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
        else:
            while curr_node.next:
                if curr_node.next.value == value and not inserted:
                    old_next = curr_node.next
                    curr_node.next = new_node
                    new_node.next = old_next
                    inserted = True
                curr_node = curr_node.next
            if not inserted:
                raise TargetError(f"Value {value} not found in linked list")


class TargetError(Exception):
    pass
